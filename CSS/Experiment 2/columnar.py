plainText = input("Enter plain Text: ")
key = input("Enter key: ")
matrixPlainText = [list(key)]
matrixPlainText.append([])



def convertIntoMatrix(plainText,key,matrixPlainText):
    i = 0
    j = 0
    global rowCount
    rowCount = 1

    while(j<len(plainText)):
        if i < len(key):
            matrixPlainText[rowCount].append(plainText[j])
            i += 1    
            j += 1
        
        else:
            i = 0
            matrixPlainText.append([])
            rowCount += 1
            matrixPlainText[rowCount].append(plainText[j])
            i += 1
            j += 1
            
        if j == len(plainText):
            while i < len(key):
                matrixPlainText[rowCount].append("-")
                i += 1
    #print(matrixPlainText)
    return matrixPlainText


matrixPlainText = convertIntoMatrix(plainText,key,matrixPlainText)

def encipher(key):
    
    sortedKey = list(key)
    enc_text = list()
    

    for count1 in range(len(key)):
        min1_val = sortedKey[0]
        min1 = 0
        
        for i in range(len(key)):
            if min1_val > sortedKey[i]:
                min1 = i
        # print(sortedKey)
        sortedKey[min1] = "Z"
        # print("I is ",min1)
        
                

        for j in range(1,rowCount+1):
            enc_text.append(matrixPlainText[j][min1])
        # matrixPlainText[0][i] = "z"
    str_enc_text = ""    
    str_enc_text = str_enc_text.join(enc_text)
    print("Cipher Text is:",str_enc_text)

encipher(key)




