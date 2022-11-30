prime1 = 7
prime2 = 17
decimalEq = {"a": '28', 'b':'29','c':'30',"d": '31', 'e':'32','f':'33',"g": '34', 'h':'35','i':'36',
             "j": '10', 'k':'11','l':'12',"m": '13', 'n':'14','o':'15',"p": '16', 'q':'17','r':'18',
             "s": '19', 't':'20','u':'21',"v": '22', 'w':'23','x':'24',"y": '25', 'z':'26',' ':'27'}
# prime1 = generateNum((1<<1023),(1<<1024)) #61
# prime2 = generateNum((1<<1023),(1<<1024)) #53 
# prime1 = 59
# prime2 = 53
n = (prime1)*(prime2)
eulerTotient = ((prime1-1)*(prime2-1))
# cLambda = ((prime1-1)*(prime2-1))//gcd(prime1-1,prime2-1)
# e = random.SystemRandom().randrange(2,eulerTotient)
# e = 17
# while (gcd(e, eulerTotient) != 1):
#     e = random.SystemRandom().randrange(2,eulerTotient-2)
# d= inverseMod(e,eulerTotient)
e = 5
d = 77
print("7-1 and 7^1", 100-1, 100^1)
print("Prime number 1:\n", prime1)
print("Prime number 2:\n", prime2)
print("Public key E:\n", e)
print("Private Key D:\n", d)
print("Second part of each key, 'n': \n", n)
print("mod euler totient", (e*d) % eulerTotient)
# d=pow(e,-1,eulerTotient)
while True:
    message = input("Please enter the message to encrypt, only use lowercase characters and a space: ")
    messageToEncrypt=""
    for i,v in enumerate(message):
        messageToEncrypt+=decimalEq.get(v)
    # for i in range(0,len(messageToEncrypt),2):
    #     print("i", messageToEncrypt[i], messageToEncrypt[i+1])
        
    messageToEncrypt = int(messageToEncrypt)
    print("messageToEncrypt: ", messageToEncrypt)

    message =  pow(messageToEncrypt, e, n)
    # print("Encrypted message using D: ", pow(messageToEncrypt, d, n))
    print("Encrypted Message: ", message, type(message))
    decryptedMessage =""
    decryptedInt = pow(message, d,n)
    decryptedInt = str(decryptedInt)
    print("Decrypted messsage before convert: ", decryptedInt)
    # print("Decrypted int: ", decryptedInt)
    for i in range(0, len(decryptedInt), 2):
        op, code = decryptedInt[i:i+2]
        for i in decimalEq:
            if decimalEq[i]== op+code:
                decryptedMessage+=i
    print("Decrypted messsage: ", decryptedMessage)


# prime1 = 22

# n = 55

# print("1<<0", 1<<0)
# print("1^0", 1^0)
# print("1<<7, 1<<8", 1<<7 , 1<<8)
# print("1<<7", 1<<7)
# print("1^2", 1^2)
# with open('readme.txt', 'w') as f:
#     f.write(str(prime1) + "," + str(n))
#     f.close



# # import time
# # import timeit

# # a = 20
# # while (a & 1 != 1):
# #     print(bin(a))
# #     print(bin(1))
# #     a>>=1

# # # print(bin(a))
# # # print(bin(1))
# # def bitwiseNeg(b):
# #     start= time.time()
# #   #  print(b)
# #     mask = b>> (32*31)
# #     b = b + mask ^ mask
# #     elapsed = time.time()
# #     print(b)
# #     return elapsed - start

# # def absolutes(b):
# #     start = time.time()
# #     abs(b)
# #     elapsed = time.time()
# #     return (elapsed - start)
# # #c = 20

# # def timesNeg(b):
# #     start = time.time()
# #     b = b*(-1)
# #     elapsed = time.time()

# # #print(bin(b))
# # #print(bin(c))
# # b = -5818634380714526832816272921419528201286760130754006761446205722245428804940267595458187590475683880656662183079367250849228145393866630230421028725762269695671916283774611755702036450043886640182166356879918045309123348596891704021700144885647022260243377127844776634069236057183072917531728699714260929586978816454764247486751189449604612515426307848992262160299679624964530613435467608540775424315610087942418360785906246362225894919115069729006727998097371688023580514423175383516575381409674216882943480060767478498993446456003222286471617092822496106177725729968075603047211360056536478072874127212596081344321
# # b = ~b
# # #print(b)
# # test = -58186343

# # # print(~test+1)
# # # print(test^1)
# # # print(test ^0)
# # # bit = bitwiseNeg(b)
# # # absolute = absolutes(b)
# # # tn = timesNeg(b)
# # # if bit > absolute and bit > tn:
# # #     print("bit wis")
# # # elif absolute > bit and absolute >tn:
# # #     print("abs wins")
# # # elif tn > bit and tn > absolute:
# # #     print("tn wins")

# # #if(3188441830 & 1 == 0):
# #    # print("here")
        
# # #print(2<<31)
# # #print(2**32)


# # a = 13
# # print(7^2)
# # # def inverseMod(17, cLambda):
# # #     a = 0
# # #     b = 1
# # #     lIN=cLambda 
# # #     while (e != 0):
# # #         quotient = lIN//e
# # #         remainder = lIN%e
# # #         lIN = e
# # #         e = remainder
# # #         c = a-b*quotient
# # #         a = b
# # #         b = c
# # #     if (a > 0):
# # #         d = (cLambda+a)
# # #     else:
# # #         print("negative D ", cLambda-a)
# # #         d = cLambda-(abs(a))
        
# # #     return d

# # print(1 & 1)
# z = 135498697598393551077960432563595610387295103370752544428442015616065423085822191904818365249464173960979552732664447929503432374101315074087784288190828557236249092766592975665156227432541498547260753062632029262401822649379174984937574774803587661763463625844806367751590599681237012084557427200230383723151
# b = 174847122920827129747364256284219310776797220328074402057175273776101755532783024462341400928879257991168637740039226092688722881010603849764838622942128629313850258225924626907342623672176794738797265484087796773068616573503040092951910999836545302109395547184636583124678367229961988360174379816995506144947
# x = 2
# g = b//b
# while(x <= g):
#     if (b%x == 0):
#         print("False")
#     else:
#         print("true")
#         x+=1