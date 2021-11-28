validation = False


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        total_number_of_yes = 0
        group_responses = [group_response.replace('\n', '') for group_response in file.read().split('\n\n')]
        for group_response in group_responses:
            responses = {}
            for response in group_response:
                responses[response] = 0
            total_number_of_yes += len(responses)
        return total_number_of_yes


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        group_responses = [group_response.split('\n') for group_response in file.read().split('\n\n')]
        sum_of_correct_number_of_yes = 0
        # Response for each group
        for group_response in group_responses:
            responses = {}
            # Response for each person in group
            for person_response in group_response:
                # Each response for each person
                for response in person_response:
                    # If the response already exists in dict, add 1
                    if response in responses:
                        responses[response] += 1
                    # If response doesn't exist, set to 1
                    else:
                        responses[response] = 1
            for key, value in responses.items():
                # Check if the number of yes for each response is equal to the number of responses
                if value == len(group_response):
                    sum_of_correct_number_of_yes += 1
        return sum_of_correct_number_of_yes


print(f'{part_1()=} {part_2()=}')
