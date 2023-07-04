#include "encryption.h"
#include "stdlib.h"
#include <stdio.h>
#include <openssl/md5.h>


int main(void){
    char* encryption_key="c56b2fa8d1a21183a185f7c1e526a0b8";
    char* auth_password_enc="8c6e2f34df08e2f879e61eeb9e8ba96f8d9e96d8033870f80127567d270d7d96";
    char *auth_password = decrypt(encryption_key, auth_password_enc);
    printf("Found: %s\n", auth_password);
}