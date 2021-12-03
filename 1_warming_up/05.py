#n-gram

def n_gram(n, list_target):
    list_n_gram = []

    for i in range(len(list_target) - n + 1):
        list_n_gram.append(tuple(list_target[i:i+n]))

    return list_n_gram

def main():
    str1 = "I am an NLPer"

    word_bi_gram = n_gram(2,str1.split())
    char_bi_gram = n_gram(2,list(str1))
    
    print(word_bi_gram)
    print(char_bi_gram)

if __name__=="__main__":
    main()