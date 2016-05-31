import random


def listoverlap(list1, list2):
    c = set(list1)
    d = set(list2)
    return list(c & d)


def main():
    random_a = random.randint(1, 20)
    random_b = random.randint(1, 20)
    a = []
    b = []
    for i in range(0, random_a+1):
        a.append(random.randint(0, 20))
    print(a)
    for i in range(0, random_b+1):
        b.append(random.randint(0, 20))
    print(b)
    result = listoverlap(a, b)
    print(result)

if __name__ == '__main__':
    main()
