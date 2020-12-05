import ast


def validate(passports, required):
    valid = 0
    valid_pass = []
    for passport in passports:
        valid_pass.append(passport)
        for str in required:
            if str not in passport:
                valid -= 1
                valid_pass.remove(passport)
                break
        valid += 1
    print(valid)
    return valid_pass


def validate_better(passports):
    valid =0
    for passport in passports:
        if val_byr(passport) and val_iyr(passport) and val_eyr(passport) and val_hgt(passport) and val_hcl(passport) and val_ecl(passport) and val_pid(passport):
            valid += 1
    print(valid)


def val_byr(passport):
    return len(passport["byr"]) == 4 and int(passport["byr"]) in range(1920, 2003)


def val_iyr(passport):
    return len(passport["iyr"]) == 4 and int(passport["iyr"]) in range(2010, 2021)


def val_eyr(passport):
    return len(passport["eyr"]) == 4 and int(passport["eyr"]) in range(2020, 2031)


def val_hgt(passport):
    if (passport["hgt"][-2:] == "in"):
        return int(passport["hgt"][:-2]) in range(59, 77)
    if (passport["hgt"][-2:] == "cm"):
        return int(passport["hgt"][:-2]) in range(150, 194)
    return False


def val_hcl(passport):
    if passport["hcl"][0] != '#':
        return False
    try:
        int(passport["hcl"][1:], 16)
        return True
    except ValueError:
        return False


def val_ecl(passport):
    return passport["ecl"] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def val_pid(passport):
    return len(passport["pid"]) == 9 and passport["pid"].isnumeric()


if __name__ == '__main__':
    with open("day4_input.txt") as f:
        lines = f.read()

    passports = lines.split("\n\n")
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_p = validate(passports, required)
    passport_json = []
    for passport_val in valid_p:
        passport_val = "{" + passport_val + "}"
        output = ""
        quoting = False
        for char in passport_val:
            if char.isalnum() or char == "#":
                if not quoting:
                    output += '"'
                    quoting = True
            elif quoting:
                output += '"'
                quoting = False
            output += char
        passport_json.append(output)
    passport_json = [ast.literal_eval(passp.replace(" ", ", ").replace("\n", ", ")) for passp in passport_json]
    validate_better(passport_json)