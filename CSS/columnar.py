plainText = "MEETMETOMORROW"
key = "GOOD"
matrixPlainText = [list(key)]
matrixPlainText.append([])



def convertIntoMatrix(plainText,key,matrixPlainText):
    i = 0
    j = 0
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
    print(matrixPlainText)
    return matrixPlainText


matrixPlainText = convertIntoMatrix(plainText,key,matrixPlainText)

def encipher(key):
    sortedKey = list(key)
    for i in range(len(key)-1):
        

    print(sortedKey)

    print(max(sortedKey))

encipher(key)




