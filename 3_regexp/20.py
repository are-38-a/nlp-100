#JSONデータの読み込みPermalink

import json
def main():
    json_filepath = "./jawiki-country.json"

    with open(json_filepath, mode='r') as f:
        for line in f:
            country = json.loads(line)
            if country['title'] == 'イギリス':
                text_uk = country['text']
                break

    # 確認
    print(text_uk)

if __name__=="__main__":
    main()