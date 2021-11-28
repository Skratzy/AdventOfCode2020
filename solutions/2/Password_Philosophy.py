import re


def part_1():
    with open("1.txt", "r") as f:
        pw_policy_regex = re.compile(r'(\d*)-(\d*) ([a-z]): (.*)')
        valid_pws = 0
        for line in f:
            res = pw_policy_regex.search(line)
            # print(f'{line=} {res=}')
            min, max, letter, password = res.groups()
            if int(min) <= password.count(letter) <= int(max):
                valid_pws += 1
            # print(f'{min=} {max=} {letter=} {password=} {valid_pws=}')
        return valid_pws


def part_2():
    with open("1.txt", "r") as f:
        pw_policy_regex = re.compile(r'(\d*)-(\d*) ([a-z]): (.*)')
        valid_pws = 0
        for line in f:
            res = pw_policy_regex.search(line)
            # print(f'{line=} {res=}')
            min, max, letter, password = res.groups()
            if (password[int(min) - 1] == letter) != (password[int(max) - 1] == letter):
                valid_pws += 1
            # print(f'{min=} {max=} {letter=} {password=} {valid_pws=}')
        return valid_pws


print(f'{part_1()=} {part_2()=}')
