import datetime


def years(age):
    return_age = 100-int(age)
    return (return_age + 2016)


def main():
    input_age = input("write here your age:")
    name = input("Write here your name:")
    print(years(input_age))


if __name__ == '__main__':
    main()
