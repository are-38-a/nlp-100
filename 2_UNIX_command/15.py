#末尾のN行を出力
import sys

def main(filename, count_lines):
    list_data = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.rstrip()
            list_data.append(line)

    #N行を表示
    list_data_for_display = list_data[-count_lines:]

    for line in list_data_for_display:
        print(line)

if __name__=="__main__":
    args = sys.argv

    filename = args[1]
    count_lines = int(args[2])
    
    main(filename, count_lines)