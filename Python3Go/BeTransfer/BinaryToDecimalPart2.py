def bin2dec(binaryStr):
    Multiplier = 0
    Divider = -1
    DecimalNumber = 0
    DecimalIndex = 0
    Number = 0

    for el in binaryStr:
        if el == '.':
            DecimalNumber += 1
            if DecimalNumber > 1:
                return -1
            if DecimalNumber == 1:
                DecimalIndex = int(binaryStr.index('.'))

    if DecimalNumber == 0:
        DecimalIndex = len(binaryStr)

    for el in binaryStr[DecimalIndex::-1]:
        if el == '1':
            Number = Number + 2 ** Multiplier
            Multiplier += 1
        if el == '0':
            Multiplier += 1

    for el in binaryStr[(DecimalIndex + 1):len(binaryStr):1]:
        if el == '1':
            Number = Number + 2 ** Divider
            Divider -= 1
        if el == '0':
            Divider -= 1
    return Number


# # print( 'test string'.index('s')
print(bin2dec('11'))  # == 3 #
print(bin2dec('0.1'))  # == 0.5
print(bin2dec('1.01'))  # == 1.25
print(bin2dec('111.011'))  # == 7.375
print(bin2dec('1.1.1'))  # == -1 #
print(bin2dec('1011.011'))  # == 11.375
