#集合

def n_gram(n, list_target):
    list_n_gram = []

    for i in range(len(list_target) - n + 1):
        list_n_gram.append(tuple(list_target[i:i+n]))

    return list_n_gram

def main():
    str1 = "paraparaparadise"
    str2 = "paragraph"

    X = set(n_gram(2,list(str1)))
    Y = set(n_gram(2,list(str2)))
    
    ans1 = X | Y
    ans2 = X & Y
    ans3 = X - Y
    ans4 = ("s","e") in X | Y

    print(ans1)
    print(ans2)
    print(ans3)
    print(ans4)

if __name__=="__main__":
    main()