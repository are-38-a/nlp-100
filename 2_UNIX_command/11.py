#タブをスペースに置換

def main():
    filename = "./popular-names.txt"

    list_data = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.rstrip()
            list_data.append(line)

    new_list_data = [line.replace("\t"," ") for line in list_data]

    with open('test.txt', 'w') as f:
        for line in new_list_data:
            f.write("%s\n" % line)

if __name__=="__main__":
    main()