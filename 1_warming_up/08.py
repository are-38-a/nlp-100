#集合

def cipher(target):
    list_target = list(target)

    #普通に書く
    """
    list_crypt = []
    for i in range(len(list_target)):
        if list_target[i].islower():
            list_crypt.append(chr(219-ord(list_target[i])))
        else:
            list_crypt.append(list_target[i])
    """

    #1行で書く
    #list_crypt = [chr(219-ord(list_target[i])) if list_target[i].islower() else list_target[i] for i in range (len(list_target))]

    #さらに短く
    list_crypt = [chr(219-ord(x)) if x.islower() else x for x in list_target]

    str_crypt = "".join(list_crypt)

    return str_crypt

def main():
    ans = cipher("Hello World!")

    print(ans)

if __name__=="__main__":
    main()