print("Name: Prem Bhajaj, Sap ID:60004188001\n")

def encipher():
    pt = input("Enter plain text:  ")

    dis = int(input("Enter Displacement: "))

    ct = ""

    for i in range(0, len(pt)):
        temp = ord(pt[i])-65
        temp = ((temp + dis) % 26)
        ct += chr(temp+65)

    
    print( "The enciphered Text is:",ct)

    print()
    print()



def decipher(ct2,dis2):

    

    pt2 = ""


    for i in range(0, len(ct2)):
        temp = ord(ct2[i])-65
        if (temp-dis2)<0:
            temp = 26+(temp-dis2)
        else:
            temp = temp-dis2

        pt2 += chr(temp+65)

    print("Deciphered Text is:",pt2)


def bruteForce():
    ct2 = input("Enter enciphered text: ")
    for i in range(0,26):
        decipher(ct2,i)


choice = int(input("1.Encipher  2.Decipher  3.Brute-Force :  "))

if choice == 1:
    encipher()

elif choice == 2:
    ct2 = input("Enter enciphered text: ")
    dis2 = int(input("Enter displacement: "))
    decipher(ct2,dis2)

elif choice == 3:
    bruteForce()








