#ファイルをN分割する
import sys

def main(filename, N):
    #ファイル読み込み
    list_data = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.rstrip()
            list_data.append(line)

    #N分割するときの行数を取得
    num_lines = len(list_data) // N

    for i in range(N):
        start = i * num_lines
        end = start + num_lines

        list_output_data = list_data[start:end]

        #書き込み
        filename_for_output = "{:03d}".format(i) + ".txt"
        with open(filename_for_output, 'w') as f:
            for line in list_output_data:
                f.write("%s\n" % line)

if __name__=="__main__":
    args = sys.argv

    filename = args[1]
    N = int(args[2])
    
    main(filename, N)