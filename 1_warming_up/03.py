#円周率

def main():
    str1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

    str1 = str1.replace(",","")
    str1 = str1.replace(".","")

    list_str1 = str1.split()

    ans = []
    for i in range(len(list_str1)):
        ans.append(len(list_str1[i]))

    print(ans)

if __name__=="__main__":
    main()