def calculate_dynamic(lines, x_step = 3, y_step = 1):
    x_pos = 0
    tree = 0
    line_len = len(lines[0])
    for y_pos in range(0, len(lines), y_step):
        # print("Line: " + str(y_pos) + " Pos: " + str(x_pos % line_len) + " Val: " + str(lines[y_pos][x_pos % line_len]))
        if lines[y_pos][x_pos % line_len] == '#':
            tree += 1
        x_pos += x_step
    return tree


if __name__ == '__main__':
    lines = []
    with open('day3_input.txt') as f:
        for line in f:
            lines.append(line.rstrip())
    print(calculate_dynamic(lines))
    print(calculate_dynamic(lines, 1, 1))
    print(calculate_dynamic(lines, 5, 1))
    print(calculate_dynamic(lines, 7, 1))
    print(calculate_dynamic(lines, 1, 2))

