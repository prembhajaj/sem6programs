print("Prem Bhajaj: 60004188001")
print()
pt = input("ENTER PLAIN TEXT: ")
key = input("ENTER KEY: ")
ct = ""
ctr = 0
pt2 = ""


######EQUATING LENGTH OF KEY AND PLAIN TEXT#######
keylen = len(key)
while len(key) != len(pt):
    key += key[ctr]
    ctr += 1
    ctr %= keylen

#####ENCIPHERMENT######
for i in range(len(pt)):
    exor = ord(pt[i])^ord(key[i])
    exor += 65
    ct += chr(exor)
print("ENCIPHERED TEXT IS:",ct)



#####DECIPHERMENT######
for i in range(len(pt)):
    exor = ord(ct[i])
    exor -= 65
    pt2_ascii = exor^ord(key[i])
    pt2 += chr(pt2_ascii)
print("DECIPHERED TEXT IS:",pt2)
