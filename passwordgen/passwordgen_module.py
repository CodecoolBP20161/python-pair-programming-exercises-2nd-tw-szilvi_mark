import random
import string

strong_or_weak = input("Strong or weak password would you like to choose?")


def passwordgen():
    global strong_or_weak
    for_weak_password = ['hahika', 'hihike', 'ilovecheese']
    if strong_or_weak == "strong":
        list_password = []
        random_lenght = random.randint(8, 14)
        for i in range(0, random_lenght+1):
            random_char = random.randint(33, 127)
            list_password.append(str(chr(random_char)))
        return str(list_password)
    elif strong_or_weak == "weak":
        return random.choice(for_weak_password)


def main():
    if strong_or_weak == "strong":
        print("Your strong password is:")
    elif strong_or_weak == "weak":
        print("Your weak password is:")
    result = passwordgen()
    print(result.strip("[]"))


if __name__ == '__main__':
    main()
