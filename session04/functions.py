def decrypt(code):
    decrypted_message = ''
    for char in code:
        unicode = ord(char)
        if (unicode != ord(' ')):
            decrypted_char = chr(unicode + 2)
            decrypted_message += decrypted_char
        else:
            decrypted_message += ' '

    return decrypted_message

# print(decrypt("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."))


def my_abs(n):
    if n < 0:
        return -n
    else:
        return n

# my_abs(-5)

def give_a_break():
    return 'break'

# print(give_a_break())

def give_me_another_break():
    str = 'break'
    print('another break')
    return str


# print(give_me_another_break())

def quadratic(a, b, c):
    
