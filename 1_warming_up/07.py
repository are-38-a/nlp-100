#集合

def template(x, y, z):
    str1 = str(x) + "時の" + str(y) + "は" + str(z)
    
    return str1

def main():
    ans = template(12,"気温", 22.4)

    print(ans)

if __name__=="__main__":
    main()