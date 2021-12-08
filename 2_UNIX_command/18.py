#各行を3コラム目の数値の降順にソート

def main():
    filepath = "./popular-names.txt"

    list_data = []
    with open(filepath) as f:
        for line in f.readlines():
            line = line.rstrip()
            list_data.append(line)

    sorted_list_data = sorted(list_data, key=lambda x:int(x.split()[2]), reverse=True)

    for line in sorted_list_data:
        print(line)

if __name__=="__main__":
    main()