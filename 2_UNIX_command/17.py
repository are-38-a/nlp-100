#1列目の文字列の異なり

def main():
    filepath = "./popular-names.txt"

    list_data = []
    with open(filepath) as f:
        for line in f.readlines():
            line = line.rstrip()
            list_data.append(line)

    list_col1 = []
    for line in list_data:
        list_col1.append(line.split()[0])

    set_col1 = set(list_col1)

    for s in set_col1:
        print(s)

if __name__=="__main__":
    main()