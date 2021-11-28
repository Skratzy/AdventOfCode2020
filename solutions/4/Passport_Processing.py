import re


def part_1():
    with open("1.txt", "r") as file:
        substrings = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        valid_passports = 0
        passports = file.read().split('\n\n')
        for passport in passports:
            if all([substring in passport for substring in substrings]):
                valid_passports += 1
    return valid_passports, len(passports)


def part_2():
    with open("1.txt", "r") as file:
        substrings = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        valid_passports = 0
        passports = [passport.replace('\n', ' ').split() for passport in file.read().split('\n\n')]
        for passport in passports:
            passport_dict = {}
            for key_value_field in passport:
                key, value = key_value_field.split(':')
                passport_dict[key] = value

            if len(passport_dict) == 8 or (len(passport_dict) == 7 and 'cid' not in passport_dict):
                # Valid
                #print(passport_dict)
                checks = []

                # Check byr
                byr = int(passport_dict['byr'])
                checks.append(1920 <= byr <= 2002)

                # Check iyr
                iyr = int(passport_dict['iyr'])
                checks.append(2010 <= iyr <= 2020)

                # Check eyr
                eyr = int(passport_dict['eyr'])
                checks.append(2020 <= eyr <= 2030)

                # Check hgt
                hgt = 0
                if 'cm' in passport_dict['hgt']:
                    hgt = int(passport_dict['hgt'].split('cm')[0])
                    checks.append(150 <= hgt <= 193)
                elif 'in' in passport_dict['hgt']:
                    hgt = int(passport_dict['hgt'].split('in')[0])
                    checks.append(59 <= hgt <= 76)
                else:
                    checks.append(False)

                # Check hcl
                hcl = passport_dict['hcl']
                hcl_regex = re.compile(r'^#[0-9a-f]{6}$')
                checks.append(hcl_regex.search(hcl) is not None)

                # Check ecl
                ecl = passport_dict['ecl']
                ecl_substrings = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                ecl_checks = iter([substring in ecl for substring in ecl_substrings])
                # Find the first true and then check if there are any other true in ecl_checks
                checks.append(any(ecl_checks) and not any(ecl_checks))

                # Check pid
                pid = passport_dict['pid']
                pid_regex = re.compile(r'^[0-9]{9}$')
                checks.append(pid_regex.search(pid) is not None)

                #print(f'{checks=}')
                #print(f'{byr=} {iyr=} {eyr=} {hgt=} {hcl=} {ecl=} {pid=}\n')
                if all(checks):
                    valid_passports += 1

        return valid_passports, len(passports)


print(f'{part_1()=} {part_2()=}')
