my_str = 'aaasaaa aaasaaa'

if my_str == my_str[::-1]:
    print('Palindrome detected: {}'.format(my_str))
else:
    print('"{}" is not a palindrome'.format(my_str))