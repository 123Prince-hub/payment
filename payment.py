from hashlib import md5
from base64 import b64decode
from base64 import b64encode
import base64

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

sample_string = "VniFPhhrEVhg4oOX"
sample_string_bytes = sample_string.encode("ascii")
  
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")

class AESCipher:
    def __init__(self, key):
        self.key = md5(key.encode('utf8')).digest()

    def encrypt(self, data):
        iv = bytes("VniFPhhrEVhg4oOX", 'utf-8')
        key = bytes("xhzsSHf3O9i7hA59", 'utf-8')
        self.cipher = AES.new(key, AES.MODE_CBC, iv)
        return b64encode(self.cipher.encrypt(pad(data.encode('utf-8'), 
            AES.block_size)))

    def decrypt(self, data):
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
        return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)

if __name__ == '__main__':
    print('TESTING ENCRYPTION')
    msg = input("Enter : ")
    pwd = 'xhzsSHf3O9i7hA59'
    print('Ciphertext:', AESCipher(pwd).encrypt(msg).decode('utf-8'),":",base64_string)

msg = None
spDomain = "https://securepay.sabpaisa.in/SabPaisa/sabPaisaInit"   
username = "BinShr9905@sp"  
password = "mdniUrw948VF"      
programID="5666"             
clientCode = "SIIPL"       
authKey = "xhzsSHf3O9i7hA59"                          
authIV = "VniFPhhrEVhg4oOX" 		  
txnId="XYZ0115092020789654"
txnAmt = "10"                
URLsuccess = ""   
URLfailure = ""
payerFirstName ="Mukesh"                        
payerLastName ="Kumar"                          
payerContact = "8796541230"                     
payerEmail = "test@gmail.com"                   
payerAddress = ""



msg ="?clientName=", clientCode, "&usern=", username, "&pass=", password, "&amt=", txnAmt, "&txnId=", txnId, "&firstName=", payerFirstName, "&lstName=", payerLastName, "&contactNo=", payerContact, "&Email=", payerEmail, "&Add=", payerAddress, "&ru=", URLsuccess, "&failureURL=", URLfailure


AesCipher = AesCipher()
msg = AesCipher->encrypt(authKey, authIV, msg)
# spURL = replace("+", "%2B")
msg="?query=", spURL, "&clientName=", clientCode  
msg = spDomain, msg
print("\n")
print(msg)

