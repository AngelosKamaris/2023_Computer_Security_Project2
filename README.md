## 2023 Project 2

Ο στόχος σας είναι να επιτεθείτε στον server `project-2.csec.chatzi.org`.
Γνωρίζετε ότι στο url http://project-2.csec.chatzi.org:8000
τρέχει o pico webserver, ο κώδικας του οποίου
υπάρχει στο [πακάτω repository](https://github.com/chatziko/pico).
Εχετε επίσης ήδη υποκλέψει:
- το username του site: `admin`
- το password: `8c6e2f34df08e2f879e61eeb9e8ba96f8d9e96d8033870f80127567d270d7d96`  
  (ο συγκεκριμένος webserver το δέχεται μόνο σε encrypted μορφή)

Tasks:

1. Βρείτε το MD5 digest του plaintext password
1. Βρείτε το plaintext password
1. Βρείτε το περιεχόμενο του αρχείου `/etc/secret` στον server
1. Βρείτε το αποτέλεσμα της εντολής `lspci` στον server




### Παρατηρήσεις

- Οι ίδιες ομάδες με την εργασία 1
- Εγγραφή στο github: https://classroom.github.com/a/HxmDkdtS

- Η ταχύτητα επίλυσης __δεν__ έχει βαθμολογική σημασία, αλλά θα υπάρχει "leaderboard"
  με τους 3 πρώτους που λύνουν κάθε task καθαρά για λόγους "flexing". Αν είστε στους
  πρώτους στείλτε claim στο `ys13@chatzi.org` (αλλιώς δεν χρειάζεται).

- Τα βήματα μπορούν να λυθούν με οποιαδήποτε σειρά, δεν χρειάζεται
  η λύση του ενός για το επόμενο (αλλά προτείνεται η σειρά που δίνεται).

- Hints:
  - Task 1: πρέπει να χρησιμοποιήσετε μια απλή ευπάθεια στον C κώδικα
  - Task 2: πρέπει να σπάσετε το encryption χρησιμοποιώντας μια ευπάθεια της υλοποίησης. __Δεν__
       πρέπει να κάνετε invert το digest από το task 1 (δεν θα το βρείτε
       σε MD5 databases, εκτός και αν κάποια άλλη ομάδα το βρει και το προσθέσει).
  - Tasks 3/4: buffer overflow attack. Το attack στο task 4 είναι λίγο πιο δύσκολο (αν θέλετε μπορείτε να κάνετε τα δύο tasks μαζί, αλλά στο 3 υπάρχει και λίγο πιο εύκολη λύση).

- Βαθμολογία μαθήματος
    - Εργασία 1: 4 μονάδες
    - Εργασία 2:
      - Task 1: 1 μονάδα
      - Task 2: 1 μονάδα
      - Task 3: 2 μονάδες
      - Task 4: 1 μονάδα
      - Docker: 1 μονάδα

- Στο τέλος του `README.md`: αναφέρετε τις απαντήσεις, και περιγράψτε τα βήματα που ακολουθήσατε. Μην ξεχάσετε να κάνετε commit μαζί με οποιοδήποτε κώδικα χρησιμοποιήσατε.
    Για ό,τι δεν ολοκληρώσετε περιγράψτε (και υλοποιήστε στο πρόγραμμα) την πρόοδό σας και πώς θα μπορούσατε να συνεχίσετε.

- Για όλα τα βήματα απαιτείται να γράψετε ένα πρόγραμμα που να αυτοματοποιεί την εύρεση της λύσης.
  Μπορείτε να χρησιμοποιήσετε ό,τι γλώσσα προγραμματισμού θέλετε, αλλά θα πρέπει να μπορώ να το τρέξω
  σε Ubuntu 22.04 χρησιμοποιώντας software που είναι διαθέσιμο στο Ubuntu. Θα πρέπει επίσης
  να φτιάξετε ένα script `run.sh` που εκτελεί το πρόγραμμα με ό,τι παραμέτρους χρειάζονται.

- Η πλήρης λύση της εργασίας απαιτεί να φτιάξετε ένα Docker container που να αυτοματοποιεί πλήρως την επίθεση. Ένα script ουσιαστικά, που απλά να εκτελείται σε container
ώστε να μπορεί να τρέξει οπουδήποτε. Πάραδειγμα `Dockerfile` υπάρχει στο repository,
και θα πρέπει να τρέχει με:
  ```
  docker build --tag attack . && docker run attack
  ```
  Λύσεις χωρίς docker γίνονται δεκτές, απλά χάνετε 1 μονάδα.

- Deadline: __20/7__ (μέχρι το τέλος της ημέρας)
  - Μπορείτε να παραδώσετε την εργασία και το Σεπτέμβρη, με μόνη διαφορά
  ότι το docker τότε θα πιάνει 3 μονάδες γιατί έχετε παραπάνω χρόνο
  (και πάλι όμως μπορείτε να πάρετε 10).

- __Οχι spoilers__

- __Οχι DoS__ ή brute force. Μπορείτε να χρησιμοποιείτε scripts που να κάνουν μια επίθεση με έναν λογικό αριθμό από requests (να μπορεί να τελειώσει σε μία ώρα max). Aλλά όποιος βαράει στα τυφλά μηδενίζεται
   (θέλουμε οι servers να είναι accessible από όλους). Αν δεν είστε σίγουροι αν κάτι επιτρέπεται, απλά ρωτήστε.

- Είναι σαφώς προτιμότερο να υλοποιήσετε πρώτα όλα τα attacks locally πριν τα τρέξετε στον server.

- Ο pico server έχει γίνει compile στο `linux03.di.uoa.gr`, οπότε μπορείτε εκεί να φτιάξετε
  ένα executable ακριβώς σαν αυτό που εκτελείται στον server.

- Αν θέλετε hints ρωτήστε privately (χωρίς βαθμολογική συνέπεια, σε λογικά πλαίσια).




### Report

Προς συμπλήρωση:

Απαντήσεις:

1. Απάντηση: ef281a07091268a0d779cf489d00380c

 Αφού ανοίξαμε την σελίδα στο ίντερνετ και κοιτάξαμε μήπως υπήρχε τίποτα στο περιεχόμενό της, αποφασίσαμε να δούμε τον κώδικα από το pico repository που μας δινόταν από την εργασία. Εκεί είδαμε ότι αν κάναμε ένα post με Aythorization Basic στον server, αυτός θα πήγαινε σε μια συνάρτηση η οποία λέγεται check_auth, η οποία δέχεται ένα string μετά την Basic της μορφής <username>:<encrypted-password> και ελέγχει αν ο χρήστης είναι σε μια λίστα χρηστών,και αν υπάρχει σώζει τον κωδικό του σε μια μεταβλητή που κρατάει τους md5 κωδικούς των χρηστών, αν αυτή η μεταβλητή παραμείνει άδεια σημαίνει οτι ο χρήστης δεν υπάρχει και εκτυπώνει το όνομα του χρήστη λέγοντας πως είναι invalid. Αλλιώς ελέγχει αν ο κωδικός είναι σωστός.

Εμείς λοιπόν πήγαμε να κάνουμε make τον κώδικα του pico και μας βγάζει warning:
format not a string literal and no format arguments [-Wformat-security]
  127 |     printf(auth_username);

  Βλέποντάς το αυτό αναζητήσαμε γιατί μας βγάζει αυτό το warning και βρήκαμε ότι αυτή η μέθοδος εκτύπωσης του ονόματος είναι ευάλωτη. Συγκεκριμένα έχουμε Format String Vulnerability. Αυτό σημαίνει ότι αυτή η printf δεν φιλτράρει το όνομα του χρήστη πριν το εκτυπώσει και έτσι ένας χρήστης μπορεί να βάλει μεταβλητές όπως %x, %s, για να εκτυπώσει το περιεχόμενο της στοίβας. Γνωρίζουμε ότι το όνομα και ο md5-κωδικός είναι στην στοίβα, καθώς είναι το πρώτο όρισμα της συνάρτησης check_auth, και αφού γνωρίζουμε ήδη το περιεχόμενο της Line user[], στον pico που είναι test:098f6bcd4621d373cade4e832627b4f6, θα περάσω στον header authority μετά το basic ένα string που τα κατάλληλα %x και ένα %s για να εμφανιστεί η μεταβλητή.Αυτό μας δίνει το string: JXgleCV4JXgleCV4ICAgLSAgICVz, που αν το κάνουμε base64 decode είναι το %x%x%x%x%x%x   -   %s, το οποίο βγάζει σαν αποτέλεσμα στην κλήση του από  το attack.py στον φάκελο 1 οπού βρίσκεται και το script που τρέξαμε,
  Error: {'WWW-Authenticate': 'Basic realm="Invalid user: 56d75330155663e94bf7a7ada0f79f438056d653df   -   test:098f6bcd4621d373cade4e832627b4f6"'}, όπου τα δεδομένα 
  μετά την - έχουν το όνομα και την md5 μορφή του κωδικού.

   Αφού πέτυχε λοιπόν στον τοπικό μου σέρβερ δοκίμασα την ίδια επίθεση και στον κανονικό από όπου πήρα αποτέλεσμα:

   Error: {'WWW-Authenticate': 'Basic realm="Invalid user: 57deb330155658fcdff7cc7d20f7c5238057ddb3ef   -   admin:ef281a07091268a0d779cf489d00380c"'},
    άρα ο md5 password είναι ο: ef281a07091268a0d779cf489d00380c
   

2.Απάντηση: aCEDIsRateRe
  
Στο δεύτερο ερώτημα εφαρμόζουμε το padding oracle attack που βρήκαμε εδώ, έχοντας κάνει κατάλληλες αλλαγές για να τρέχει στον server: https://github.com/TheCrowned/padding-oracle-attack.

  Κοιτόντας τον κώδικα του φακέλου encryption, μπορούμε να διακρίνουμε ότι η μέθοδος που χρησιμοποιήται για το encryption των κωδικώνείναι AES, CBC χρησιμοποιώντας για padding pkcs7. Αυτή η μέθοδος γνωρίζουμε ότι χωρίζει το μύνημα σε block των 16 byte και ξεκινάει χρησιμοποιώντας για αρχή ένα IV(σε αυτή την περίπτωση ένα block γεμάτο 0) και κάνει xor το πρώτο μπλοκ με το IV και ύστερα το κάνει eνcrypt με το κλειδί. Δημιουργεί έτσι το πρώτο block του ciphertext. Ύστερα χρησιμοποιεί το πρώτο block του ciphertext για να κάνει xor το δεύτερο block του plaintext, το οποίο κάνει eνcrypt για να δημιουργήσει το 2ο block ciphertext και αυτό επαναλαμβάνεται εως ότου να φτάσει στο τελευταίο block. Για να πετύχει αυτό όμως πρέπει το plaintext να έχει μέγεθος πολλαπλάσιο του 16, κάτι το οποίο για να το επιτύχει, προσθέτει padding στο τέλος των block της μορφής 0, 1, 22, 333 ,..., 255*255.

  Αυτό μπορεί να κάνει το πρόγραμμα πολύ ευάλωτο σε περίπτωση που έχουμε έναν τρόπο να μάθουμε αν ο κωδικός που δώσαμε έχει θέμα με το padding. Κοιτόντας τον κώδικα λοιπόν, μπορούμε να δούμε ότι όταν υπάρχει θέμα με το padding, η συνάρτηση decrypt επιστρέφει null, κάτι το οποίο οδηγεί στην αποστολή ERROR 500 στον χρήστη, το οποίο δεν εμφανίζεται όταν ο χρήστης έχει απλά λάθος κωδικό ή έχει συνδεθεί σωστά (401, 200). Επομένως βάζοντας σαν oracle μια συνάρτηση που κάνει request στον server, δίνοντας ένα ciphertext τροποποιημένο κατάλληλα ωστε να ισχύουν αυτά που θα πω μετά, και επιστρέφοντας λάθος όταν έχω status 500, μπορώ να κάνω padding oracle attack.

  Η επίθεσή μου εκμεταλλεύεται το γεγονός ότι ισχύει  a (xor) b = c <=> a (xor) c = b και αφού C1 XOR P2 = P2', όπου P2'  είναι το block2 πριν το encryption, C1 είναι το ciphertext 1 και P2 είναι το plaintext 2. Έτσι εμείς αν έχουμε 2 block, θα πηγαίναμε στο block 1 και θα δοκιμάζαμε paddings μέχρι να έχουμε το σωστό. Έτσι μπορούμε να μάθουμε το τελευτταίο byte του P2, κάνοντας xor με το padding από το C1, και να το επαναλάβουμε αυτό από το πρότελευταίο εως το πρώτο byte του P2, ώστε να πάρουμε το P2 ολόκληρο. αν επαναλάβουμε αυτό για κάθε μπλοκ, τότε θα έχουμε το plaintext σε λιγότερο από 4096 προσπάθειες ανα block, κάτι το οποίο είναι πιο γρήγορο από τις 2^128 προσπάθειες ανα block που θα χρειαζόμασταν για να σπάσουμε το ciphertext.


3. Απάντηση:

⠀⠀⠀  ⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀  ⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣦⣴⣶⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⣀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⠿⠟⠛⠛⠋⠉⠉⠉⠉⠉⠉⠛⠛⠛⠿⢷⣦⣤⣀⡹⠿⠿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣴⣶⣶⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣶⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣿⠟⠉⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠟⠀⠀⠀⠉⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢦⣽⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣷⠀⠀⠀⠀⠀
⠀⠀⢰⣿⡏⣤⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣻⡀⠀⠀⢤⢠⣼⣿⡆⠀⠀⠀⠀
⠀⠀⠀⢿⣿⠁⠀⠀⠀⠀⣴⡾⠁⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣀⠀⠀⠀⠀⠀⠈⢻⣇⠀⠀⠈⣇⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⠀⡀⣀⠀⢠⣿⠃⠀⠀⢀⣾⣿⣿⡿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡷⠀⠀⠀⠀⠀⢸⣿⠀⢠⣠⣿⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢿⣷⣇⣽⠀⢈⡏⠀⠀⠀⠸⣿⣿⣿⣦⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣧⣤⠥⠀⠀⠀⠀⣿⣿⣧⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠛⠿⣿⣧⣾⣿⡄⠀⠀⠀⠙⠿⠿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠋⠀⠀⠀⠀⠀⢸⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣿⡇⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢶⣼⣿⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀
⠀⠀⣠⣶⣾⠿⠛⠛⠻⢷⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡿⠋⠉⠉⠉⠛⢿⣦⡀⠀⠀
⢀⣾⡿⠋⠀⠀⠀⠀⠀⠀⠙⣿⡆⢀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣿⡟⠀⠀⠀⠀⠀⠀⠀⠹⣿⡆⠀
⣼⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣸⣷⣿⣷⣧⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⢠⡾⣠⣇⣠⣿⣿⣿⡇⠀⢀⠀⠀⠀⢀⠀⠀⢹⣷⠀
⣿⣷⡀⠀⣷⠀⠀⠀⣼⣦⣴⣿⠏⠙⠻⠿⣷⡿⠷⣶⣶⡾⠿⠿⠷⢶⣶⣦⣤⣾⣿⣷⣿⣿⠿⠿⠛⠛⠙⠻⣿⣤⣾⣇⠀⢀⣸⣇⣀⣼⣿⠃
⠘⢿⣿⣾⣿⣷⣴⣾⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠻⠿⠿⠿⠟⠛⠛⠁⠀


            You guessed it... puppies!

  Για ο ερώτημα 3 ήταν ξεκάθαρο ότι έπρεπε να κάνουμε buffer overflow. Βλέποντας τις συναρτήσεις μπορούμε να δούμε ότι η μόνη συνάρτηση ευάλωτη σε buffer overflow είναι η post_param. Αυτό γίνεται γιατί η συνάρτηση αυτή χρησιμοποιεί strcpy, όμως στο όρισμα του δέχεται την post_data η οποία έχει μέγεθος post_size το οποίο μπορούμε να θέσουμε στα request μας, με το header Content-Length: 0. Έτσι όταν αντιγράφουμε τo περιεχόμενο του payload, το οποίο έχει τα δεδομένα που περνάμε με το request μας, θα λόγω του μεγέθους, η συνάρτηση strcpy θα κάνει overwrite στον buffer.
  
  Έχοντας αυτό σαν στόχο τρέξαμε τον pico server στον linux3.di.uoa.gr και ετοιμάσαμε μια επίθεση παρόμοια με την 1η, για να δούμε τι τιμές θα έχει το stack, σε gdb, θέτοντας set follow-fork-mode child, με break στην γραμμή 127. Τρέξαμε τον σέρβερ, τρέξαμε και την επίθεσή μας, εκτελέσαμε  
x/28wx $esp για να δούμε τι περιέχει ο buffer και πήραμε σαν αποτέλεσμα:

  ![εικόνα](https://github.com/chatziko-ys13/2023-project-2-psarotaverna-o-takis/assets/79763769/459a42d5-ea9f-4e67-b24e-cedf9fd3c0d0)

  Ελέγχοντας τις τιμές στον buffer, διαπιστώσαμε ότι η τελευταία τιμή είναι η return της check auth, η δεύτερη από το τέλος είναι η τιμή της ebp που δείχνει στο τέλος του buffer και η 3 θέσεις πριν το ebp είναι το canary, καθώς είναι η μόνη που έχει 00 στο τέλος. Όλες αυτές τις τιμές μπορούμε να τις λάβουμε, χρησιμοποιόντας την επίθεση που είδαμε και στο Βήμα 1, δηλαδή string formating. Επομένως έτσι θα πάρουμε το canary, μια διεύθυνση στον buffer και μια διεύθυνση σε συναρτήσεις, για να φτιάξουμε το payload μας.

  Για να φτιάξουμε το payload, πρέπει να βρούμε πως είναι αποθηκευμένα τα δεδομένα, όταν μπαίνουμε στην post_param. Για να το επιτύχουμε αυτό κάναμε άλλο ένα κανονικό request, αυτή τη φορά προσθέτοντας δεδομένα στο body και με gdb, βάζοντας break στην γραμμή 184 και εκτυπώνοντας 22 λέξεις από τον esp με το x/22wx $esp παίρνουμε: 

  ![εικόνα](https://github.com/chatziko-ys13/2023-project-2-psarotaverna-o-takis/assets/79763769/03eedce1-ca80-436c-9e3d-47a6804228f4)

  Σε αυτή την εικόνα πρέπει να βρούμε ποιά διεύθυνση είναι η return της post_param, ποιά είναι η διεύθυνση της post_data, και που είναι το canary. Αυτό το κάνουμε γιατί στο payload το οποίο θα κάνουμε, χρειάζεται να ξαναβάλουμε τιμές όπως το canary, για να μην βγάλει error stack smashing, την τιμή post_data, για να γίνουν σωστά processed τα δεδομένα του payload από τις for που γίνονται κάτω από την strcpy της post_param και για να αντικαταστήσουμε την return της post_param, θα χρειαστούμε την send_file, καθώς αντί να τερματίσει το πρόγραμμα θέλουμε να πάει σε μια συνάρτηση η οποία επιστρέφει το αρχείο και αυτή είναι η send_file.Έτσι στην εικόνα βρήκαμε ότι μετά από 104 bytes (στην 14η word), ανήκει η post_data, μετά από 120 bytes (στην 16η word) πρέπει να μπει το canary και μετά από 144 bytes (στη 18η word), πρέπει να μπει η διεύθυνση στην οποία θέλουμε να πάμε μόλις τελειώσει η post_param.  Έχοντας αυτό στο μυαλό μας έπρεπε απλά να βρούμε τα offet των διευθύνσεων που είχαμε σε σχέση με αυτές που θέλαμε.

  Έχοντας τον ebp, υπολογίσαμε ότι:
    ebp-post_data=120 <=> post_data=ebp-120
    return check_auth address-send_file address=-1581 <=> send_file address=check_auth address+1581

  Αφού βρήκαμε τα offset, το μόνο που μένει είναι να τρέξουμε ένα Format String Vulnerability με 31 %08x το οποίο είχαμε βρει ότι θα μας επιστρέψει το canary, τον ebp και το return address από τον global server, να δώσουμε τα offset στον ebp και return check_auth address, για να φτιάξουμε τα post_data και send_file address, ώστε να τα βάλουμε στο payload και να αντικαταστήσουμε όλα τα 00 σε 3D που είναι η δεκαεξαδική τιμή του =. Δεν έχουμε τελειώσει ακόμα όμως με το payload, καθώς θα πρέπει να προσθέσουμε και τα ορίσματα για την send file. συγκεκριμένα στην αρχή του payload θα προσθέσουμε το string "/etc/secret" σε 16-δική μορφή και να βάλουμε στο τέλος του 3D, καθώς επίσης πρέπει να προσθέσουμε και την διεύθυνση του πρώτου argument. Γνωρίζουμε ότι στον stack, σε μια διεύθυνση το πρώτο word, περιέχει την διεύθυνση της συνάρτησης, το δεύτερο περιέχει την διεύθυνση επιστροφής από αυτή την συνάρτηση και από το 3 εως το n βάζουμε τα arguments. Επομένως απλά πρέπει 8 bytes μετά την διεύθυνση του send file (αφού δεν μας ενδιαφέρει που θα επιστρέψει η συνάρτηση), να προσθέσω πάλι την διεύθυνση της post_data, καθώς το argument μου είναι αποθηκειμένο στην αρχή του buffer. έτσι το payload θα μοιάζει:

  "/etc/secret"(σε 16-αδική μορφή) + 3D + 40 φορές το 90 (16-δική αξία του NOP)+ post_data + 4 φορές το 90 + canary + 12 φορές το 90 + send_file address + 4 φορές το 90 + post_data (η διεύθυνση του arg1).

Αφού αντικαταστήσουμε όλα τα 00 σε 3D, αποθηκεύουμε το payload σε ένα αρχείο και στέλνουμε με curl το αρχείο στον server με το όνομα, τον encrypted κωδικό του admin και  Content-Length = 0.

  Έτσι το payload μπαίνει στην post_param, κάνει χάρη στην strcpy buffer overflow, τα 3D μετατρέπονται σε 00 με την for που είχαμε αναφερθεί πιο πάνω η οποία έχει αυτή την δουλειά και όταν τελειώνει, πηγαίνει στην send_file, η οποία θα μας στείλει την απάντηση. Ύστερα από 3 δεύτερα κάνουμε αποσύνδεση από τον server. 

!Η από πάνω επίθεση δοκιμάστικε και πέτυχε πρώτα στον τοπικό μας server στα linux03 της σχολής!
  

4. Απάντηση:
  00:01.0 ISA bridge: Intel Corporation 82371SB PIIX3 ISA [Natoma/Triton II]
  00:01.3 Non-VGA unclassified device: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 08)
  00:03.0 VGA compatible controller: Amazon.com, Inc. Device 1111
  00:04.0 Non-Volatile memory controller: Amazon.com, Inc. Device 8061
  00:05.0 Ethernet controller: Amazon.com, Inc. Elastic Network Adapter (ENA)

  Όπως και η προηγούμενη επίθεση έτσι και αυτή χρειάστηκε buffer overflow. Σε αυτή την επίθεση όμως αντί να πηγαίνουμε στην send_file συνάρτηση πρέπει να βρούμε μια συνάρτηση που να μπορεί να τρέξει το lspci. Η συνάρτηση που αναζητούμε είναι η system(), της βιβλιοθήκης stdlib.h. Η system αν και δεν καλείτε στο ίδιο το πρόγραμμα, επειδή ανήκει στην βιβλιοθήκη stdlib.h, θα έχει διεύθυνση στο πρόγραμμά μας.

  Πήγαμε λοιπόν πάλι στον τοπικό σέρβερ μας linux03 και τρέχοντας τον server με gdb, βρήκαμε την διεύθυνση της system. Κάναμε offset την διεύθυνση αυτή με την return της check_auth και βρήκαμε πολυ μεγάλη διαφορά. Αλλάξαμε την send_file address στέλνοντας πλεον την διεύθυνση της system και ετοιμάσαμε πάλι όπως και πριν το payload, αλλάζοντας το argument σε lspci και προσθέτοντα 3D και μερικά 90 μετά για να καλύψουμε την διαφορά σε σχέση με το προηγούμενο payload που είχε μεγαλύτερο argument.

  Τρέχοντάς το παρατηρούσαμε ότι η επίθεση αποτύγχανε. Αυτό γινόταν επειδή η διεύθυνση της system ήταν εσφαλμένη. Ο λόγος που ήταν εσφαλμένη είναι ότι αν και όταν γίνεται η ίδια make στο αρχείο μας, όταν αυτό τρέχει με gdb ή χωρίς, η διευθύνσεις συναρτήσεων από βιβλιοθήκες ήταν πολύ διαφορετικές. Πήγαμε λοιπόν πίσω στο πρώτο request και με gdb, είδαμε αν υπάρχει κάποια άλλη διεύθυνση που θα μπορούσαμε να χρησιμοποιήσομε. Πράγματι 8 θέσεις πίσω από το canary, υπήρχε μια διεύθυνση αρκετά κοντά στην διεύθυνση της system. Μπορούσαμε να υποθέσουμε λοιπόν ότι αυτή η διεύθυνση ανήκει σε κάποια συνάρτηση της βιβλιοθήκης stdlib.h, επομένως δεν θα υπήρχε μεγάλη διαφορά στο offset σε σχέση με το αρχικό. Υπολόγισα λοιπόν το offset της system σε σχέση με την καινούργια διεύθυνση που βρήκα (found address) και είδα ότι είναι:
  found address-system address=-45228 <=> system address = found address+45228.

  Ξαναδοκίμασα λοιπόν να τρέξω το curl με το καινούργιο payload και πάλι υπήρχε θέμα. Αυτή την φορά όμως το πρόβλημα ήταν ότι όταν το πρόγραμμα πήγαινε στην system, το περιεχόμενο του argument μου που είχα στην αρχή του buffer γινόταν ovewrite. Επομένως έβαλα το argument μου στο τέλος του payload αντί για την αρχή, έβαλα τον δείκτη του argument να δείχνει σε αυτό και το payload μου τώρα ήταν κάπως έτσι:
  
  52 φορές το 90 (16-δική αξία του NOP)+ post_data + 4 φορές το 90 + canary + 12 φορές το 90 + send_file address + 4 φορές το 90 + post_data+88 (η διεύθυνση του arg1)+ "lspci"(σε 16-αδική μορφή) + 3D

  και έτρεξα το curl όπως την προηγούμενη φορά και πέτυχε. Δοκίμασα την επίθεση και στον global server και πήρα την απάντηση που έδωσα επάνω.


Run sh scriptάκια:

  Tα attacks μας είναι όλα σε python (τα 3 και 4 έχουν και bash) και τρέχουν  χωρίς ορίσματα καθώς είναι hardcoded οι διευθύνσεις του server της εργασίας.
  Αν το run.sh βγάλει permision denied κάντε chmod.
  
  Docker. Ο ντόκερ απλώς εκτελεί ένα αρχείο ex.py που εκτελεί το κάθε scipt με την σειρά για την εκτέλεση του θα χρειαστεί:
  sudo dockerd
  sudo docker build --tag attack . && sudo  docker run attack (σε άλλο terminal)
  (ενδεχομένως να μην χρειάζονται τα sudo στα μηχανήματα μας χρειαζόντουσαν)
  
  
  Τα ερωτήματα 3 και 4 ενδεχομένως να αποτύχουν σε κάποια προσπάθεια λόγω μεγάλου φόρτου μυνημάτων στον server. Αν γίνει αυτό και θέλετε να ξανατρέξετε τον docker
  χωρίς να περιμένετε το χρονοβόρο ερώτημα 2 απλά πηγαίντε στο docker-run.sh και κάντε comment out τα :
  
  chmod +x 2/attack.py
  python3 2/attack.py
  
  Kαι έπειτα ξανατρέξτε το docker

