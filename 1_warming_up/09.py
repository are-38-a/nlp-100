#TypoglycemiaPermalink

import random

def randomize_word(target):

    if 3 < len(target):
        list_target = list(target)

        ans = ""
        ans += target[0]
        ans += "".join(random.sample(target[1:-1], len(target[1:-1])))
        ans += target[-1:]

    else:
        ans = target

    return ans

def main():
    str1 = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

    list_str1 = str1.split()

    list_ans = [randomize_word(x) for x in list_str1]

    ans = " ".join(list_ans)

    print(ans)

if __name__=="__main__":
    main()