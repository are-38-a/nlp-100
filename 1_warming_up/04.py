#元素記号

def main():
    str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    str1 = str1.replace(",","").replace(".","")
    list_str1 = str1.split()

    #1文字取り出す単語のリスト
    list_one =[1, 5, 6, 7, 8, 9, 15, 16, 19]

    ans = {}
    for i in range(len(list_str1)):
        if i + 1 in list_one:
            word = list_str1[i][:1]
        else:
            word = list_str1[i][:2]
        
        ans[word] = i + 1

    print(ans)

if __name__=="__main__":
    main()