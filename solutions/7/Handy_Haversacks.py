import re

validation = False


def check_if_bag_can_contain(bag_dict, bag_to_look_in, bag_to_look_for, bags_searched, max_depth, curr_depth):
    if curr_depth == max_depth:
        return False
    if bag_to_look_in not in bags_searched:
        bags_searched.append(bag_to_look_in)
        if bag_to_look_for in bag_dict[bag_to_look_in]:
            return True
        else:
            for bag in bag_dict[bag_to_look_in]:
                if check_if_bag_can_contain(bag_dict, bag, bag_to_look_for, bags_searched, max_depth, curr_depth + 1):
                    return True
    return False


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        bag_to_look_for = "shiny gold"
        bag_dict = {}
        containing_bags_regex = re.compile(r'\d (.*?) bags*')
        for line in file:
            bag, contains = line.split(" contain ")
            bag, _ = bag.split(' bag')
            contains = containing_bags_regex.findall(contains)
            if bag_to_look_for in contains:
                bag_dict[bag] = [bag_to_look_for]
            else:
                bag_dict[bag] = contains
        number_of_bags_with_correct_bag = 0
        for key in bag_dict:
            if check_if_bag_can_contain(bag_dict, key, bag_to_look_for, [], len(bag_dict), 0):
                number_of_bags_with_correct_bag += 1
        return number_of_bags_with_correct_bag


def check_how_many_bags_contained(bag_dict, bag_to_look_in):
    amount_of_bags_contained = 0
    if len(bag_dict[bag_to_look_in]) == 0:
        amount_of_bags_contained = 0
    for bag, value in bag_dict[bag_to_look_in].items():
        amount_of_bags_contained += value + value * check_how_many_bags_contained(bag_dict, bag)
    return amount_of_bags_contained


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        bag_to_check_contents_of = "shiny gold"
        bag_dict = {}
        containing_bags_regex = re.compile(r'([0-9]+) (.*?) bags*')
        for line in file:
            bag, contains = line.split(" contain ")
            bag, _ = bag.split(' bag')
            contains = containing_bags_regex.findall(contains)
            contains_dict = {}
            for bags_contained in contains:
                for i in range(0, len(bags_contained), 2):
                    contains_dict[bags_contained[i + 1]] = int(bags_contained[i])
            bag_dict[bag] = contains_dict
        return check_how_many_bags_contained(bag_dict, bag_to_check_contents_of)


print(f'{part_1()=} {part_2()=}')
