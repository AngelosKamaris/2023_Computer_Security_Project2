from oracle import is_padding_ok
import binascii

BLOCK_SIZE=16

def attack( ciphertext ):
	guessed_clear = b''

	split_string = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)]
	blocks = split_string( ciphertext, BLOCK_SIZE )
	
	for block_n in range( len( blocks ) - 1, 0, -1 ): #build pair of blocks starting from end of message
		spliced_ciphertext = blocks[block_n - 1] + blocks[block_n]

		decoded_bytes = b'?' * BLOCK_SIZE #output of block cipher decoding values

		##GET VALUE OF SECRET BYTE byte
		for byte in range( BLOCK_SIZE - 1, -1, -1 ):
			new_pad_len = BLOCK_SIZE - byte

			#Build hacked ciphertext tail with values to obtain desired padding
			hacked_ciphertext_tail = b''
			for padder_index in range( 1, new_pad_len ):
				hacked_ciphertext_tail += bytearray.fromhex('{:02x}'.format( new_pad_len ^ decoded_bytes[byte + padder_index] ) )
			
			for i in range( 0, 256 ):
				attack_str = bytearray.fromhex( '{:02x}'.format( ( i ^ spliced_ciphertext[byte] ) ) )
				hacked_ciphertext = spliced_ciphertext[:byte] + attack_str + hacked_ciphertext_tail + spliced_ciphertext[byte + 1 + new_pad_len - 1:]

				if( is_padding_ok( hacked_ciphertext ) ):

					test_correctness = hacked_ciphertext[:byte - 1] + bytearray.fromhex( '{:02x}'.format( ( 1 ^  hacked_ciphertext[byte] ) ) )  + hacked_ciphertext[byte:]
					if( not is_padding_ok( test_correctness ) ):
						continue
					
					decoded_bytes = decoded_bytes[:byte] + bytearray.fromhex('{:02x}'.format( hacked_ciphertext[byte] ^ new_pad_len ) ) + decoded_bytes[byte + 1:]
					guessed_clear = bytearray.fromhex('{:02x}'.format( i ^ new_pad_len ) ) + guessed_clear
					break
	
	return guessed_clear[:-guessed_clear[-1]] #remove padding!


def test_the_attack():
    msg=binascii.unhexlify('8c6e2f34df08e2f879e61eeb9e8ba96f8d9e96d8033870f80127567d270d7d96')
    cracked=attack(msg)
    print("cracked: "+cracked.decode())

if __name__ == '__main__':
    test_the_attack()