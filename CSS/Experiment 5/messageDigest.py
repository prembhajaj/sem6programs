import hashlib 
print("Prem Bhajaj: 60004188001")
dataF = "data.txt"
verifyF = "test.txt"

def readF(name):
    f = open(name, "r")
    data = f.read()
    f.close()
    return data

algoChoice = input("Algorithm: MD5(1) / SHA1(2): ")
flowChoice = input("Digest: Generate(a) / Verify(b): ")
data = ""
result = None
hexHash = ""

if flowChoice == 'a':
    data = readF(dataF)
else:
    hexHash = input("Enter hash of data: ")
    data = readF(verifyF)

if algoChoice == "1":
    result = hashlib.md5(data.encode())
else:
    result = hashlib.sha1(data.encode())

if flowChoice == 'a':
    print("The generated hash is:",result.hexdigest())
else:
    if hexHash == result.hexdigest():
        print("The file is intact")
    else:
        print("Tampered FIle")