#テンプレートによる文生成

def template(x,y,z):

    ans = str(x) + "時の" + str(y) + "は" + str(z)

    return ans

def main():
    ans = template(12, "気温", 22.4)

    print(ans)

if __name__=="__main__":
    main()