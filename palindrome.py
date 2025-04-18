def is_palindrome(word):
    return word == word[::-1]

if __name__ == "__main__":
    word = "madam"  # You can change this word
    if is_palindrome(word):
        print(f"✅ {word} is a palindrome!")
    else:
        print(f"❌ {word} is not a palindrome.")
        exit(1)
