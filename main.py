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