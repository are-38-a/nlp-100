#col1.txtとcol2.txtをマージ

def main():

    #データ読み込み
    filename_col1 = "./col1.txt"
    filename_col2 = "./col2.txt"

    list_col1 = []
    with open(filename_col1) as f:
        for line in f.readlines():
            line = line.rstrip()
            list_col1.append(line)

    list_col2 = []
    with open(filename_col2) as f:
        for line in f.readlines():
            line = line.rstrip()
            list_col2.append(line)
    
    #1列目と2列めをマージして配列に
    list_data = []
    for i in range(len(list_col1)):
        list_data.append("{}\t{}".format(list_col1[i],list_col2[i]))

    #書き込み
    with open('marge.txt', 'w') as f:
        for line in list_data:
            f.write("%s\n" % line)

if __name__=="__main__":
    main()