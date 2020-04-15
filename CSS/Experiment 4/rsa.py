# https://www.geeksforgeeks.org/how-to-solve-rsa-algorithm-problems/
print("Pratik Panchal: (60004188006)")
import random
randLowerLimit = 10
randUpperLimit = 1000

def getFactors(a, l = []):
    i = 1
    aHalf = int(a/2) + 1
    while i < aHalf:
        i += 1
        if a % i == 0:
            l.append(i)
            break

    if i != aHalf:
        getFactors(a/i, l)
    else:
        l.append(int(a))
    return l

def getDistinctFactors(a):
    facts = getFactors(a, [])
    temp = []
    for i in facts:
        if not temp.__contains__(i):
            temp.append(i)
    return temp

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def isPrime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def isMultipleOf(lst, num):
    for i in lst:
        if num % i == 0:
            return True
    return False

def getE(phi):
    facts = getDistinctFactors(phi)
    e = random.randint(randLowerLimit,randUpperLimit)
    while isMultipleOf(facts, e) or e % phi == 0:
        e = random.randint(randLowerLimit,randUpperLimit)
    return e

def getD(phi, e):
    a = [1,0]
    b = [0,1]
    d = [phi, e]
    k = [None, int(phi/e)]

    while d[-1] != 1:
        ai = a[-2] - (a[-1] * k[-1])
        bi = b[-2] - (b[-1] * k[-1])
        di = d[-2] - (d[-1] * k[-1])
        # print("--",di,d,k)
        ki = int(d[-1] / di)

        a.append(ai)
        b.append(bi)
        d.append(di)
        k.append(ki)

        # print(ai,bi,di,ki)
        
    finalD = b[-1]

    if b[-1] < 0:
        finalD += phi
    finalD = finalD % phi

    return finalD

p = random.randint(randLowerLimit,randUpperLimit)
while not isPrime(p):
    p = random.randint(randLowerLimit,randUpperLimit)

q = random.randint(randLowerLimit,randUpperLimit)
while not isPrime(q) or p == q:
    q = random.randint(randLowerLimit,randUpperLimit)

n = p * q
phi = (p-1) * (q-1)

e = getE(phi)
d = getD(phi, e)

t = random.randint(randLowerLimit,randUpperLimit)
print("Let t =",t)
c = (t**e) % n
print("Calculated c =",c)
t = (c**d) % n
print("Calculated t =", t, "for c =",c)