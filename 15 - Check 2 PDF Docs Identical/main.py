import hashlib
from difflib import SequenceMatcher

def hash_file(fileName1, fileName2):
  h1 = hashlib.sha1()
  h2 = hashlib.sha1()
  
  with open(fileName1, "rb") as file:
    chunck = 0
    while chunck != b'':
      chunck = file.read(1024)
      h1.update(chunck)
      
  with open(fileName2, "rb") as file:
    chunck = 0
    while chunck != b'':
      chunck = file.read(1024)
      h2.update(chunck)
    
    return h1.hexdigest(), h2.hexdigest()

msg1,msg2 = hash_file("pdf1.pdf", "pd1.pdf")

if(msg1 != msg2):
  print("These files are not identical")
else:
  print("These files are identical")