import re
from codecs import strict_errors


def validate_count(low, high, letter, string):
    if string.count(letter) in range(low, high+1):
        return 1
    return 0


def validate_position(first, second, letter, string):
    if second >= len(string):
        return 0
    if (string[first] == letter) != (string[second] == letter):
        return 1
    return 0


if __name__ == '__main__':
    with open("day2_input.txt") as file_in:
        valid_count = 0
        valid_position = 0
        for line in file_in:
            line = line.replace(" ", "")
            r = re.search("(\d+)-(\d+)([a-z]):([a-z]+)", line)
            valid_count = valid_count + validate_count(int(r.group(1)), int(r.group(2)), r.group(3), r.group(4))
            valid_position = valid_position + validate_position(int(r.group(1))-1, int(r.group(2))-1, r.group(3), r.group(4))
        print(valid_count)
        print(valid_position)