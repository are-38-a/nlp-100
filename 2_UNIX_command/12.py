#1列目をcol1.txtに，2列目をcol2.txtに保存

def main():

    #データ読み込み
    filename = "./popular-names.txt"

    list_data = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.rstrip()
            list_data.append(line)

    #タブをスペースに
    new_list_data = [line.replace("\t"," ") for line in list_data]

    #1列目と2列めを配列に
    col1 = [line.split()[0] for line in new_list_data]
    col2 = [line.split()[1] for line in new_list_data]

    with open('col1.txt', 'w') as f:
        for line in col1:
            f.write("%s\n" % line)

    with open('col2.txt', 'w') as f:
        for line in col2:
            f.write("%s\n" % line)

# $ cut -f 項目数 -d 区切り文字 ファイル名　(タブ区切りは-dを省略)

if __name__=="__main__":
    main()