#各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
import collections

def main():
    filepath = "./popular-names.txt"

    list_data = []
    with open(filepath) as f:
        for line in f.readlines():
            line = line.rstrip()
            list_data.append(line)

    list_col1 = [x.split()[0] for x in list_data]

    dict_counter = collections.Counter(list_col1)
    
    sorted_counter = sorted(dict_counter.items(), key=lambda x:x[1], reverse=True)
    
    for t in sorted_counter:
        print("{} {}".format(t[0], t[1]))

if __name__=="__main__":
    main()