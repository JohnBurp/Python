import random
import math

w = 5
h = 5
playfair = [[0 for i in range(w)] for x in range(h)]
letter = 97
unvalidcharacters = []
characters = []
letpos = []
cipher = []
appendable = True
appendable2 = True
publicKey = []
privateKey = []
result = []
ordresults = []

#Simple method to check if the given number is prime
def isPrime(a):
    return all(a % i for i in range(2, a))

#Turn the output's string back into a list
def listifyDecrypt(list):
    newlist = []
    numstring = ""
    yy = 0
    while yy < len(list):
        if ord(list[yy]) > 47 and ord(list[yy]) < 58:
            for i in range(yy, len(list)):
                if ord(list[i]) < 47 or ord(list[i]) > 58:
                    for n in range(yy, i):
                        numstring += list[n]
                        newn = n + 1
                    break
            newlist.append(numstring)
            yy = newn
            numstring = ""
        else:
            yy += 1
    return newlist

#just turns both lists of keys back to blank
def resetKeys():
    publicKey = []
    privateKey = []


#Generates p and q used to calculate n. Because of CPU limitations, this will not be over 512 bits
def genpq(minnum, maxnum):
    i = random.randint(minnum, maxnum)
    while not isPrime(i):
        i = random.randint(minnum, maxnum)
    return i

#Another simple method of checking whether a number is a int or float by dividing by 1 and searching the remainder
def isWhole(num):
    if num % 1 == 0:
        return True
    else:
        return False

#Pretty simple
def genN(p, q):
    return p * q

#For RSA to be crytographically secure, e must be coprime with n (share only one prime factor). Since every number shares the factor of one, it must only share one.
def genE(n, p, q):
    egened = False
    while not egened:
        egened = True
        e = random.randint(1, (p - 1) * (q - 1))
        for x in range(2, n):
            if e % x == 0 and n % x == 0:
                egened = False
    return e

#Instead of using the extended Euclidian algorithm to find the value of (inverse e mod (p-1)(q-1)), I go through the possible answers until one works
def invMod(n, e, p, q):
    while True:
        for x in range(((p - 1) * (q - 1)) - 1):
            if (e * x) % ((p - 1) * (q - 1)) == 1:
                de = [x, e]
                return de
        e = genE(n, p, q)

#More cleaning up
def fillKeys(n, d, e):
    publicKey.append(n)
    publicKey.append(e)
    privateKey.append(n)
    privateKey.append(d)

#The actual encrypting (C = P^e)
def encryptRSA(pt, e, n):
    encryptedtwice = []
    for x in range(len(pt)):
        encryptedtwice.append(pow((pt[x]), e) % n)
    return encryptedtwice

#The actual decrypting P = C^d
def decryptRSA(et, d, n):
    decrypted = []
    for x in range(len(et)):
        decrypted.append((pow(int(et[x]), int(d)) % int(n)))
    return decrypted

#Find the value of each variable to help debug
def printVars(p, q, n, e, d):
    print("p " + str(p))
    print("q " + str(q))
    print("n " + str(n))
    print("e " + str(e))
    print("d " + str(d))

#The actual program, I always prefer putting it in it's own function then calling that function because it's visually appealing to see many lines of code get run from one line.
#Besides asking the user for it's plaintext and whatnot, mostly just calls the functions made above.
def main():
    cryption = input("Do you want to encrypt or decrypt?")
    if cryption == "encrypt":
        minimum = input("Enter the minimum number for n's primes")
        maximum = input("Enter the maximum number for n's primes")
        p = genpq(int(minimum), int(maximum))
        q = genpq(int(minimum), int(maximum))
        n = genN(p, q)
        e = genE(n, p, q)
        de = invMod(n, e, p, q)
        d = de[1]
        e = de[0]
        printVars(p, q, n, e, d)
        fillKeys(n, d, e)
        pt2 = []
        plaintext = input("Enter your message")
        for i in range(len(plaintext)):
            pt2.append(ord(plaintext[i]))
        doubleencrypted = encryptRSA(pt2, e, n)
        print("Your encrypted message is ", end = "")
        print(doubleencrypted)
        print("Public Key: ", end = "")
        print(publicKey)
        print("Private Key: ", end = "")
        print(privateKey)
    elif cryption == "decrypt":
        decrypt = input("Enter the message to decrypt")
        n = input("Enter n from the public key")
        d = input("Enter d from the private key")
        decrypted = decryptRSA(listifyDecrypt(decrypt), d, n)
        for i in range(len(decrypted)):
            print(chr(decrypted[i]), end = "")
        print("")
    resetKeys()

#Continuously repeat
while True:
    main()