import math


def at_bash(str):
    return str[::-1]

def affine(str):
    encrypted = ""
    key1 = 17
    key2 = 20
    for i in range(len(str)):
        if str[i] != ' ':
            encrypted = encrypted + chr((((key1*(ord(str[i])-ord('A')) + key2))%26)+ord('A'))
        else:
            encrypted = encrypted + str[i]
    print("encrypted")
    return encrypted

def caesarEncrypt(text, shift):
    encrypted = ""
    for i in range(len(text)):
        if(ord(text[i])+int(shift)>90):
            encrypted = encrypted + chr(ord(text[i])+int(shift)-26)
        else:
            encrypted = encrypted + chr(ord(text[i])+int(shift))
            
    print(encrypted)
    return encrypted


def caesarDecrypt(text, shift):
    decrypted = ""
    for i in range(len(text)):
        if(ord(text[i])-int(shift)<65):
            decrypted = decrypted + chr(ord(text[i])-int(shift)+26)
        else:
            decrypted = decrypted + chr(ord(text[i])-int(shift))
            
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
                encrypted = encrypted + arr[i][keyList[j]]
            except IndexError:
                pass
    
    print(encrypted)
    return(encrypted)

def columnarDecrypt(text, key):
    decrypted = ""

    # Create and fill array with null value
    rows, cols = (len(key), int(len(text)/len(key)))
    arr = [["" for i in range(rows)] for j in range(cols)]

    # Create list representing string:key as list of ascii
    keyList = []
    for i in range(len(key)):
        keyList.append(ord(key[i]))

    # Convert ascii to sorted number for future exporting
    for i in range(len(key)):
        keyList[keyList.index(min(j for j in keyList if j>(i-1)))] = i

    # Add character to array based on key
    for j in range(rows):
        for i in range(cols):
            try:
                arr[i][keyList[j]] = text[i+(j*(rows))]
                print(text[i+(j*(rows))])
            except IndexError:
                pass

    # Fill the actual character to array
    for i in range(cols):
        for j in range(rows):
            decrypted = decrypted + arr[i][j]
    
    print(decrypted)
    return(decrypted)

def encrypt(str):
    print(affine(str))

def decrypt(str):
    print('Has not been implemented')

def main():
    str = input('Enter the string: ')
    opt = input('Choose 1 to encrypt or 2 to decrypt')
    if opt == '1':
        encrypt(str)
    elif opt == '2':
        decrypt(str)


if __name__ == '__main__':
    main()
