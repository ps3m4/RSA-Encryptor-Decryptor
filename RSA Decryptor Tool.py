#______________IMPORT RSA PACKAGE__________________________________________________________
import rsa

#______________PYTHON OPENING AND READING PUBLIC & PRIVATE KEYS____________________________
try:
    with open("public.pem", "rb") as f: 
        public_key = rsa.PublicKey.load_pkcs1(f.read())
except:
    print("Error! The public key was not found in the directory.",
    "\nPlease make sure the public key exists in the current directory under the name 'public.pem'.",
    "\nProgram will now quit.", 
    "\nGoodbye!"), 
    quit()

try:
    with open("private.pem", "rb") as f: 
        private_key = rsa.PrivateKey.load_pkcs1(f.read()) 
except:
    print("Error! Your private key was not found in the directory.",
    "\nPlease make sure the private key exists in the current directory under the name 'private.pem'.",
    "\nProgram will now quit.", 
    "\nGoodbye!"), 
    quit()


#______________MESSAGE DECRYPTION STAGE____________________________________________________
try:
    encrypted_message = open("encrypted message", "rb").read() 
except:
    print("The file 'encrypted message' was not found in the current directory.",
    "\nPlease make sure the file 'encrypted message' exists in the current directory.",
    "\nProgram will now quit.",
    "\nGoodbye!"), 
    quit()

clean_message = rsa.decrypt(encrypted_message, private_key)

#______________MESSAGE SIGNATURE VERIFICATION STAGE________________________________________
message = input("Please add the owner's signature to verify the message is not corrupted: ")

try:
    with open("signature", "rb") as f: 
        signature = f.read() 
except:
    print("The file 'signature' was not found in the current directory.",
    "\nPlease make sure the file 'signature' exists in the current directory.",
    "\nProgram will now quit.",
    "\nGoodbye!"), 
    quit()

try:
    verification = rsa.verify(message.encode(), signature, public_key) 
    print("Your signature is legitimate. Hash Function:", 
    verification, 
    "\nEncrypted Message:",
    "\n",
    clean_message.decode())
except:
    print("Attention!!! The encrypted file is corrupted!") 

#______________________END OF RSA TOOL DECRYPTOR SCRIPT______________________________________________________