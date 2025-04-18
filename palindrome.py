def is_palindrome_loop():
    s = input("Enter a string: ").lower() 
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]: 
            print(False)
            return
    print(True)


is_palindrome_loop()
