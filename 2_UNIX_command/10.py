#行数のカウント

def main():
    filepath = "./popular-names.txt"

    list_data = []
    with open(filepath) as f:
        for line in f.readlines():
            line = line.rstrip()
            list_data.append(line)

    print(len(list_data))

if __name__=="__main__":
    main()