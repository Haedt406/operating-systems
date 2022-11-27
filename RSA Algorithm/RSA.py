from math import gcd
import random

# primeList = [2]
primeList = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,1279,1283,1289,1291,1297,1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,1399,1409,1423,1427,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483,1487,1489,1493,1499,1511,1523,1531,1543,1549,1553,1559,1567,1571,1579,1583,1597,1601,1607,1609,1613,1619,1621,1627,1637,1657,1663,1667,1669,1693,1697,1699,1709,1721,1723,1733,1741,1747,1753,1759,1777,1783,1787,1789,1801,1811,1823,1831,1847,1861,1867,1871,1873,1877,1879,1889,1901,1907,1913,1931,1933,1949,1951,1973,1979,1987,1993,1997,1999,2003,2011,2017,2027,2029,2039,2053,2063,2069,2081,2083,2087,2089,2099,2111,2113,2129,2131,2137,2141,2143,2153,2161,2179,2203,2207,2213,2221,2237,2239,2243,2251,2267,2269,2273,2281,2287,2293,2297,2309,2311,2333,2339,2341,2347,2351,2357,2371,2377,2381,2383,2389,2393,2399,2411,2417,2423,2437,2441,2447,2459,2467,2473,2477,2503,2521,2531,2539,2543,2549,2551,2557,2579,2591,2593,2609,2617,2621,2633,2647,2657,2659,2663,2671,2677,2683,2687,2689,2693,2699,2707,2711,2713,2719,2729,2731,2741,2749,2753,2767,2777,2789,2791,2797,2801,2803,2819,2833,2837,2843,2851,2857,2861,2879,2887,2897,2903,2909,2917,2927,2939,2953,2957,2963,2969,2971,2999,3001,3011,3019,3023,3037,3041,3049,3061,3067,3079,3083,3089,3109,3119,3121,3137,3163,3167,3169,3181,3187,3191,3203,3209,3217,3221,3229,3251,3253,3257,3259,3271,3299,3301,3307,3313,3319,3323,3329,3331,3343,3347,3359,3361,3371,3373,3389,3391,3407,3413,3433,3449,3457,3461,3463,3467,3469,3491,3499,3511,3517,3527,3529,3533,3539,3541,3547,3557,3559,3571]
decimalEq = {"a": '89', 'b':'92','c':'93',"d": '94', 'e':'95','f':'96',"g": '97', 'h':'98','i':'99',
             "j": '10', 'k':'11','l':'12',"m": '13', 'n':'14','o':'15',"p": '16', 'q':'17','r':'18',
             "s": '19', 't':'20','u':'21',"v": '22', 'w':'23','x':'24',"y": '25', 'z':'26',' ':'27'}

def rabinMiller(possiblePrime):
    k = possiblePrime^1
    t = 0
    while k & 1 != 1:
        k >>=1
    for i in range(32):
        a = random.SystemRandom().randint(2,possiblePrime^1)
        while (k < possiblePrime^1):
            toCheck = pow(a,k,possiblePrime)
            if (toCheck == 1 or toCheck == possiblePrime^1):
                t+=1
                break
            k<<=1
    if t ==32:
        return True
    else:
        print(t)
        return False

def generateNum(n, n1):
    while (True):
        possiblePrime = random.SystemRandom().randrange(n,n1)
        # possiblePrime = 294409
        for i in primeList:            
            if(possiblePrime % i == 0):
                break
        else:
            if rabinMiller(possiblePrime):
                return possiblePrime
            # else:
            #     print("false")

def inverseMod(e, cLambda):
    a = 0
    b = 1
    lIN=cLambda 
    while (e != 0):
        quotient = lIN//e
        remainder = lIN%e
        lIN = e
        e = remainder
        c = a-b*quotient
        a = b
        b = c
    if (a > 0):
        d = (cLambda+a)
    else:
        d = cLambda-(abs(a))   
    return d
            
def getKeys(prime1, prime2):
    n = (prime1)*(prime2)
    eulerTotient = ((prime1-1)*(prime2-1))
    e = random.SystemRandom().randrange(2,eulerTotient)
    while (gcd(e, eulerTotient) != 1):
        e = random.SystemRandom().randrange(2,eulerTotient-2)
    d= inverseMod(e,eulerTotient)
    return (e,d,n)

def menuOptions():
    print("Welcome to RSA key generator, encryptor, and decryptor.")
    print("Enter 1 to generate a random prime number")
    print("Enter 2 to generate new keys")
    print("Enter 3 to save the public and private keys to a text file")
    print("Enter 4 to load a key into the program")
    print("Enter 5 to encrypt a message using the generated keys")
    print("Enter 6 to decrypt a message using the generated keys")
    print("Enter 7 to run a demonstration of RSA")
    print("Enter 9 to print the menu")
    print("Enter 0 to exit the program")

def example():
    prime1 = generateNum((1<<31),(1<<32)) #61
    prime2 = generateNum((1<<31),(1<<32)) #53
    n = (prime1)*(prime2)
    eulerTotient = ((prime1-1)*(prime2-1))
    cLambda = ((prime1-1)*(prime2-1))//gcd(prime1-1,prime2-1)
    e = random.SystemRandom().randrange(2,cLambda)
    while (gcd(e, cLambda) != 1):
        e = random.SystemRandom().randrange(2,cLambda-2)
    d= inverseMod(e,eulerTotient)
    print("Prime number 1:\n", prime1)
    print("Prime number 2:\n", prime2)
    print("Carmichaels Lambda:\n", cLambda)
    print("Public key E:\n", e)
    print("Private Key D:\n", d)
    print("Second part of each key, 'n': \n", n)
    print("mod tot", e*d % cLambda)
    message = input("Please enter the message to encrypt, only use lowercase characters and a space: ")
    messageToEncrypt=""
    for i,v in enumerate(message):
        messageToEncrypt+=decimalEq.get(v)
    messageToEncrypt = int(messageToEncrypt)
    message =  pow(messageToEncrypt, e, n)
    print("Encrypted Message: ", message)
    decryptedMessage =""
    decryptedInt = pow(message, d,n)
    decryptedInt = str(decryptedInt)
    for i in range(0, len(decryptedInt), 2):
        op, code = decryptedInt[i:i+2]
        for i in decimalEq:
            if decimalEq[i]== op+code:
                decryptedMessage+= i
    print("Decrypted messsage: ", decryptedMessage)

def encrypt(e,n, message):
    messageToEncrypt=""
    for i,v in enumerate(message):
        messageToEncrypt+=decimalEq.get(v)
    messageToEncrypt = int(messageToEncrypt)
    print("Message to encrypt ", messageToEncrypt)
    messageToWrite =  pow(messageToEncrypt, e, n)
    print("Message has been encrypted and sent to file 'EM.txt'")
    with open('EM.txt', 'w') as f:
        f.write(str(messageToWrite))
    f.close()
    
def decrypt(d,n,message):
    decryptedMessage =""
    decryptedInt = pow(message, d,n)
    decryptedInt = str(decryptedInt)
    for i in range(0, len(decryptedInt), 2):
        op, code = decryptedInt[i:i+2]
        for i in decimalEq:
            if decimalEq[i]== op+code:
                decryptedMessage+= i
    print("Decrypted messsage: ", decryptedMessage)

def main():
    menu = 1
    menuOptions()  
    # size = 1024
    # prime = generateNum((2<<size-2), (2<<size-1))
    # print("Random prime number generated: ", prime)  
    while (menu != 0):
        menu = int(input("Choice: "))
        if menu == 1:
            print("Please enter how big the prime number should be, your input will be used as the exponent of 2, so if you enter 16 then a key will be generated between 2^15 and 2^16, only use numbers larger then 13: ")
            size = int(input())
            print("2^size",1<<size)
            prime = generateNum((1<<size-1), (1<<size))
            print("Random prime number generated: ", prime)

        elif menu == 2:
            print("Please enter how big the prime numbers should be, only use numbers larger then 13 and less then 3020: ")
            size = int(input())
            prime1 = generateNum((1<<size-1), (1<<size)) #61
            prime2 = generateNum((1<<size-1), (1<<size)) #53
            e,d,n = getKeys(prime1,prime2)
            print("e",e)
            print("d",d)
            print("n", n)
        
        elif menu == 3:
            with open('public.txt', 'w') as publicKey:
                publicKey.write(str(e) + "," + str(n))
                publicKey.close()
            with open('private.txt', 'w') as privateKey:
                privateKey.write(str(d) + "," + str(n))
                privateKey.close()

        elif menu == 4:
            option = int(input("Will this key be set as the public key (enter 1) or private key (enter 2)? "))
            keyToLoad = input("Please enter the key that will be loaded: ")
            with open(keyToLoad, 'r') as f:
                for l in f:
                    if option ==1:
                        key = l.split(",")
                        e = key[0]
                        n = key[1]
                    elif option ==2:
                        key = l.split(",")
                        d = key[0]
                        n = key[1]
                    else:
                        print("You did not enter 1 or 2. Try again.")
                f.close()

        elif menu == 5:
            message = input("This will use the public key located in 'public.txt'\nPlease enter the message to encrypt, only use lowercase characters and space: ")
            with open("public.txt", 'r') as f:
                key = f.read()
                key = key.split(",")
                e = int(key[0])
                n = int(key[1])
            encrypt(e,n,message)
            f.close()

        elif menu == 6:
            message = input("This will use the private key located in 'public.txt' and a message saved in 'EM.txt', hit 'enter'")
            with open("private.txt", 'r') as f:
                key = f.read()
                key = key.split(",")
                d = int(key[0])
                n = int(key[1])
            with open("EM.txt") as f:
                message = f.read()
            f.close()
            decrypt(d,n,int(message))    

        elif menu == 7:
            example()
        elif menu == 9:
            menuOptions()
        
main()
