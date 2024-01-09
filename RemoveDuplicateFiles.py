import hashlib
import os
#Returns the hash string of the given file name

def hashFile(filename):
  BLOCKSIZE = 65536
  #For large files, if we read it all together it can lead to memory overflow, so we take a blocksize to read at a time
  hasher = hashlib.md5()
  with open(filename, 'rb') as file:    #Reads the particular blocksize from file
    buf = file.read(BLOCKSIZE)
    while(len(buf) > 0):
      hasher.update(buf)
      buf = file.read(BLOCKSIZE)
  return hasher.hexdigest()

if __name__ == "__main__":
  hashMap = {}    #Dict to store the hash and filename
  deletedFiles = []    #List to store deleted files
  filelist = [f for f in os.listdir() if os.path.isfile(f)]
  for f in filelist:
    key = hashFile(f)
    #If key already exists, it deletes the file
    if key in hashMap.keys():
      deletedFiles.append(f)
      os.remove(f)
    else:
      haspMap[key] = f
  if len(deletedFiles) != 0:
    print('Deleted Files')
    for i in deletedFiles:
      print(i)
  else:
    print('No duplicate files found')
