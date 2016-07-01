def main():
    test_text = input ()
    print (test_text)

    s1 = test_text[0:10]
    s2 = test_text[-10:]

    s = s1 + s2

    print (s)

if __name__ == '__main__':
    main()