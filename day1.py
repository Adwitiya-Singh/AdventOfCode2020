def one_1(array):
    for i in array:
        for j in array:
            if i + j == 2020:
                return i * j
def one_2(array):
    for i in array:
        for j in array:
            for k in array:
                if i + j + k == 2020:
                    return i * j * k

if __name__ == '__main__':
    with open('day1_1_input.txt') as file:
        content = file.read()
    array = content.split()
    numbers = list(map(int, array))
    print(one_1(numbers))
    print(one_2(numbers))
