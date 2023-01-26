#______________IMPORT RSA PACKAGE________________________________________________________________
import rsa

#______________KEYS GENERATION___________________________________________________________________
ask_prompt = input("Do you have already your private and public keys generated? Y/N:")

if ask_prompt == "N":
    public_key, private_key = rsa.newkeys(2048)
    with open("public.pem", "wb") as f: 
        f.write(public_key.save_pkcs1("PEM"))
    with open("private.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM")) 
    print("Your set of keys has been successfully generated!",
     "\nYou will find the .pem keys in your current directory.")
elif ask_prompt == "Y":
    print("Your set of keys has been previously generated.", 
    "\nThe program will proceed with the existing keys.", 
    "\nRe-run the program and type 'N' in the case you need a new set of keys.")
else:
    print("Invalid input! The program will now quit.", 
    "\nGoodbye!"), 
    quit()


#______________PYTHON OPENS & READS KEYS_________________________________________________________
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


#______________MESSAGE ENCRYPTION STAGE__________________________________________________________
message = input("Please add your message here: ") 

encrypted_message = rsa.encrypt(message.encode(), public_key)

with open("encrypted message", "wb") as f: 
    f.write(encrypted_message) 

print("Your encrypted message has been created!", 
"\nEncrypted message output:",
"\n", encrypted_message, 
"\nYou will find the encrypted message file in your current directory.")


#_____________ADD SIGNATURE______________________________________________________________________
userid = input("Please add your keyword signature here to sign the encrypted file: ") 

signature = rsa.sign(userid.encode(), private_key, "SHA3-512")

with open("signature", "wb") as f: 
    f.write(signature) 

print("Your signature file has been created inside your current directory.", 
    "\nOn decryption it will be used to verify the 'encrypted message' file.")


#__________________________END OF RSA TOOL ENCRYPTOR SCRIPT________________________________________________