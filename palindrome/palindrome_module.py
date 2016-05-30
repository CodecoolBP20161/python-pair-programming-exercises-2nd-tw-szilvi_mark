def palindrome(str1):
    str1 = str1.lower()
    str1 = str1.replace(" ", "")
    print(str1[::-1])
    print(str1)
    if str1 == str1[::-1]:
        return True
    else:
        return False


def main():
    print(palindrome("Anna"))

if __name__ == '__main__':
    main()
