import datetime


def years(age):
    return_age = 100-int(age)
    return (return_age + 2016)


def main():
    input_age = input("write here your age:")
    name = input("Write here your name:")
    returned_age = years(input_age)
    print(years(input_age))
    number = int(input("add me a number:"))
    for i in range(0, number):
        print(returned_age)


if __name__ == '__main__':
    main()
