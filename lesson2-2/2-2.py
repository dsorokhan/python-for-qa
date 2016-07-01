import re

def main():
    test_text = input ()

    if ',' not in test_text:
        print (test_text)
    else:
        c = ','
        a = [pos for pos, char in enumerate(test_text) if char == c]
        res = test_text[max(a) + 1:]
        print (res)

if __name__ == '__main__':
    main()


