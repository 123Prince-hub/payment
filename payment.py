from hashlib import md5
from base64 import b64decode
from base64 import b64encode
import base64

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

sample_string = "0QvWIQBSz4AX0VoH"
sample_string_bytes = sample_string.encode("ascii")
  
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")

class AESCipher:
    def __init__(self, key):
        self.key = md5(key.encode('utf8')).digest()

    def encrypt(self, data):
        iv = bytes("0QvWIQBSz4AX0VoH", 'utf-8')
        key = bytes("rMnggTKFvmGx8y1z", 'utf-8')
        self.cipher = AES.new(key, AES.MODE_CBC, iv)
        return b64encode(self.cipher.encrypt(pad(data.encode('utf-8'), 
            AES.block_size)))

    def decrypt(self, data): 
        iv = bytes("0QvWIQBSz4AX0VoH", 'utf-8')
        key = bytes("rMnggTKFvmGx8y1z", 'utf-8')
        raw = b64decode(data)
        self.cipher = AES.new(key, AES.MODE_CBC, raw[:AES.block_size])
        return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)

if __name__ == '__main__':
    

    spDomain = "https://uatsp.sabpaisa.in/SabPaisa/sabPaisaInit?query="   
    username = "nishant.jha_2885"  
    password = "SIPL1_SP2885"      
    programID="5666"                
    clientCode = "SIPL1"              
    authKey = "rMnggTKFvmGx8y1z"                          
    authIV = "0QvWIQBSz4AX0VoH" 		  
    txnId="XYZ0115092020789657"
    txnAmt = "10"                 
    URLsuccess = "https://eleit.in/success.php"   
    URLfailure = "https://eleit.in/fail.php"  
    payerFirstName ="Mukesh"                          
    payerLastName ="Kumar"                           
    payerContact = "8796541230"               
    payerEmail = "test@gmail.com"                  
    payerAddress = "jaipur"

    spURL ="?clientName="+clientCode+"&usern="+username+"&pass="+password+"&amt="+txnAmt+"&txnId="+txnId+"&firstName="+payerFirstName+"&lstName="+payerLastName+"&contactNo="+payerContact+"&Email="+payerEmail+"&Add="+payerAddress+"&ru="+URLsuccess+"&failureURL="+URLfailure
    
    print('TESTING ENCRYPTION')
    finalDATA = (AESCipher(authKey).encrypt(spURL).decode('utf-8'))
    finalDATA = finalDATA+":"+base64_string
    finalDATA = finalDATA.replace('+', '%2B')
    finalDATA = spDomain+finalDATA+"&clientName="+clientCode
    #print(finalDATA)

    response = "uzjRY3LL/iiodo9WiHqDvdIoyo/fI49nux5gUnZtAew1tWpJzGheqYqZl2wWCymU6Gz3a2Z5RZY1XCd5ID7boJkozQcXDyenlciVUy6rbYb8s%2BjV4/a6/dJbbNAWgeUABP8IJ1pSgenmQcG7bVVeBjUmZjuKxztuZqOx1%2BGY6mLeD4A0ZLasAcCN/l49zVOIfkd7uU/TvXtogkg/sxUB%2B9wp7OJOKXkYZyEw%2Blwj%2BraZA1zT%2B9KI3FL75bERZRVlPnCMDuBO8E55iEYzVD0me9C1zhWdfD2O/M38gbWkooemNUy6GLkOxCTSnIXJois2lZXYn5ZOXQmHqZ3P2Sf08CK9Suv2WkvXbB45llGTWTbwuKN7%2Btfmj2iTABupj2GJ/cDabVQpn9ilvd19rGT0uTquWQeVn8RfsQC31W9sO3SIVXKFxkLomuIPFUMBh2l7KefWOyf0xyexEnjXnjKvDUXlcKa80eS/VvNMMdGfLFjyUxmtqtUseH6tz5fiQq7sNkESSdosbqD%2BFz%2B2kAonXtPI/dWBkJqjQf4js2OcDWf7ONBD7KdSf2aDJ%2BG7GOz7k9Nwr9eqKvz720WgWUYVkwRPX0ng9sK78SMa2L6gs//bYm2R/1DM%2BGOLAg1dI9LdKMOFL38ve2raQ41/OLpypZNfhIUx2kKJ1SIbyLJrAzCTvI/rFq8A6RiI53R00AwLEw7pnAkdk2T2MbvR/50SUbEqHc1jCwv%2BzaW7QNTbljzPJtPal8ttan3FQoJhljWlIiUTZb/zd6UtK8ReuX6hhFP4T46s0vZv%2BuJjdlDmqvSYoeh8n2iFtc732%2BjqisPYRJFytrMTG9sXM%2BpBu%2BTIH0MmbhP8q63KYeHEZ135%2BOjIHAzoJEknuqU0o%2BnT9i/5EZ6/BuPL0dBpOV8vk6SviQ==&clientCode=SIPL1&transDate=Sat%20Apr%2010%2012:53:41%20IST%202021"
    response = response.replace("%2B","+")
    print('Message...:', AESCipher(authKey).decrypt(response).decode('utf-8'))



