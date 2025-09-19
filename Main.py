def encryet(text,key):

    for i in len(text):
        num= ord(text[i])
        bin_num=bin(num)
        xord=bin(bin_num)^key

    print(xord)