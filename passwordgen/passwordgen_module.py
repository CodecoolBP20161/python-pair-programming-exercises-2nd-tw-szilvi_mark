import random
import string


def passwordgen():
    list_password = []
    random_lenght = random.randint(8, 14)
    for i in range(0, random_lenght+1):
        random_char = random.randint(33, 127)
        list_password.append(str(chr(random_char)))
    return str(list_password)


def main():
    print(passwordgen())


if __name__ == '__main__':
    main()
