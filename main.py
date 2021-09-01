import math


def at_bash(str):
    return str[::-1]


def affineEncrypt(text, a, b):
    encrypted = ""
    for i in range(len(str)):
        if str[i] != ' ':
            encrypted = encrypted + chr(((a * (ord(text[i]) - ord('A')) + b) % 26) + ord('A'))
        else:
            encrypted = encrypted + text[i]
    print(encrypted)
    return encrypted


def affineDecrypt(text, a, b):
    inv_a = 0
    for i in range(26):
        flag = (a * i) % 26
        if flag == 1:
            inv_a = i
    decrypted = ""
    for i in range(len(text)):
        if text[i] != ' ':
            decrypted = decrypted + chr((inv_a * (ord(text[i]) + ord('A') - b) % 26) + ord('A'))
        else:
            decrypted = decrypted + text[i]
    print(decrypted)
    return decrypted


def caesarEncrypt(text, shift):
    encrypted = ""
    for i in range(len(text)):
        if (ord(text[i]) + int(shift) > 90):
            encrypted = encrypted + chr(ord(text[i]) + int(shift) - 26)
        else:
            encrypted = encrypted + chr(ord(text[i]) + int(shift))

    print(encrypted)
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
                encrypted = encrypted + arr[i][keyList[j]-1]
            except IndexError:
                pass
    
    print(encrypted)
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


def encrypt(str):
    print('Test')


def decrypt(str):
    print('Test')


def main():
    str = input('Enter the string: ')
    opt = input('Choose 1 to encrypt or 2 to decrypt: ')
    if opt == '1':
        encrypt(str)
    elif opt == '2':
        decrypt(str)


if __name__ == '__main__':
    main()
