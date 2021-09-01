import math

def at_bash(text):
    encrypted = ""
    for i in range (len(text)):
        if (ord(text[i]) >= ord('A') and ord(text[i]) <= ord('Z')):
            encrypted = encrypted + chr(ord('A') + ord('Z')-ord(text[i]))
        else:
            encrypted = encrypted + text[i]
    return encrypted

def affineEncrypt(text, a, b):
    encrypted = ""
    for i in range(len(text)):
        if (ord(text[i]) >= ord('A') and ord(text[i]) <= ord('Z')):
            encrypted = encrypted + chr(((a * (ord(text[i]) - ord('A')) + b) % 26) + ord('A'))
        else:
            encrypted = encrypted + text[i]
    return encrypted

def affineDecrypt(text, a, b):
    inv_a = 0
    for i in range(26):
        flag = (a * i) % 26
        if flag == 1:
            inv_a = i
    decrypted = ""
    for i in range(len(text)):
        if (ord(text[i]) >= ord('A') and ord(text[i]) <= ord('Z')):
            decrypted = decrypted + chr((inv_a * (ord(text[i]) + ord('A') - b) % 26) + ord('A'))
        else:
            decrypted = decrypted + text[i]
    return decrypted

def caesarEncrypt(text, shift):
    encrypted = ""
    for i in range(len(text)):
        # if (ord(text[i]) < 65):
        #     pass
        if (ord(text[i]) + int(shift) > 90):
            encrypted = encrypted + chr(ord(text[i]) + int(shift) - 26)
        else:
            encrypted = encrypted + chr(ord(text[i]) + int(shift))

    return encrypted

def caesarDecrypt(text, shift):
    decrypted = ""
    for i in range(len(text)):
        if (ord(text[i]) - int(shift) < 65):
            decrypted = decrypted + chr(ord(text[i]) - int(shift) + 26)
        else:
            decrypted = decrypted + chr(ord(text[i]) - int(shift))

    print(decrypted)
    return decrypted

def columnarEncrypt(text, key):
    encrypted = ""

    # Create and fill array with "_"
    rows, cols = (len(key), math.ceil(len(text)/len(key)))
    arr = [["_" for i in range(rows)] for j in range(cols)]

    # Structure:
    # cols   rows -->          arr[cols][rows]
    #  |
    #  |
    #  v

    # Fill the actual character to array
    for i in range(cols):
        for j in range(rows):
            try:
                arr[i][j] = text[j+(i*(rows))]
            except IndexError:
                pass
    
    # Create list representing string:key as list of ascii
    keyList = []
    for i in range(len(key)):
        keyList.append(ord(key[i]))

    # Convert ascii to sorted number for future exporting
    for i in range(len(key)):
        keyList[keyList.index(min(j for j in keyList if j>(i-1)))] = i

    # Add character to encrypted, per column based on keylist
    for j in range(rows):
        for i in range(cols):
            try:
                encrypted = encrypted + arr[i][keyList.index(j)]
            except IndexError:
                pass
    
    return(encrypted)

def columnarDecrypt(text, key):
    decrypted = ""

    # Create and fill array with null value
    rows, cols = (len(key), math.ceil(len(text)/len(key)))
    arr = [["" for i in range(rows)] for j in range(cols)]

    # Create list representing string:key as list of ascii
    keyList = []
    for i in range(len(key)):
        keyList.append(ord(key[i]))

    # Convert ascii to sorted number for future exporting
    for i in range(len(key)):
        keyList[keyList.index(min(j for j in keyList if j>(i-1)))] = i

    print(rows, cols)
    # Add character to array based on key
    for j in range(rows):
        for i in range(cols):
            try:
                arr[i][keyList[j]-1] = text[i+(j*(cols))]
            except IndexError:
                pass

    # Add character to decrypted
    for i in range(cols):
        for j in range(rows):
            decrypted = decrypted + arr[i][j]
    
    print(decrypted)
    return(decrypted)

def encrypt(text,shift,key,a,b):
    step1 = caesarEncrypt(text,shift)
    step2 = columnarEncrypt(step1,key)
    step3 = at_bash(step2)
    final = affineEncrypt(step3,a,b)
    print("\nInitial message: ",text,"\nProccess: Caesar--> Columnar --> Atbash --> Affine\n")
    print("Caesar   : ", text , "  -->  ", step1)
    print("Columnar : ", step1 , "  -->  ", step2)
    print("At Bash  : ", step2 , "  -->  ", step3)
    print("Affine   : ", step3 , "  -->  ", final)
    print("\n\nFinal Result : ",final)

def decrypt(text):
    print('Undedr Development')

def main():
    print("////// CLASSIC CIPHER //////")
    while(True):
        opt = input('Option:\n1. Encrypt\n2. Exit\n>>')
        if(opt=='2'):
            print('Thankyou for using our app!! :D')
            return False
        elif(opt=='1'):
            opt = input('Option:\n1. Default encryption\n2. Custom Encryption\n>>')
            if opt == '1':
                (shift, key, a, b) = (3, 'FMIPA', 3, 5)
                text = input("\nInput message to encrypt:\n>>").upper()
                encrypt(text,shift,key,a,b)
                input("\nThats it\n\n\n")
            elif opt == '2':
                decrypt(text)
        else:
            print('Please...')


if __name__ == '__main__':
    main()
