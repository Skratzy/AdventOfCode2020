import math


def check_instruction(bottom, top, letter, letter_to_check):
    #print(f'{bottom=} {top=} {letter=} {letter_to_check=}')
    if letter_to_check == letter:
        bottom += math.ceil((top - bottom) / 2)
    else:
        top -= math.ceil((top - bottom) / 2)
    #print(f'{bottom=} {top=}')
    return bottom, top


def get_row_and_column(instruction):
    #print(f'{instruction=}')
    bottom, top = 0, 127
    for row_check in range(6):
        bottom, top = check_instruction(bottom, top, instruction[row_check], 'B')
    row = 0
    if instruction[6] == 'F':
        row = bottom
    else:
        row = top

    bottom, top = 0, 7
    for column_check in range(7, 9):
        bottom, top = check_instruction(bottom, top, instruction[column_check], 'R')
    column = 0
    if instruction[9] == 'L':
        column = bottom
    else:
        column = top

    return row, column


def part_1():
    with open("1.txt", "r") as file:
        highest_seat_id = -1
        for line in file:
            row, column = get_row_and_column(line)
            seat_id = row * 8 + column
            #print(f'{row=} {column=} {seat_id=}')
            if seat_id > highest_seat_id:
                highest_seat_id = seat_id
        return highest_seat_id


def part_2():
    with open("1.txt", "r") as file:
        seat_ids = []
        for line in file:
            row, column = get_row_and_column(line)
            seat_id = row * 8 + column
            #print(f'{row=} {column=} {seat_id=}')
            seat_ids.append(seat_id)
        seat_ids.sort()

        for i in range(len(seat_ids) - 1):
            if seat_ids[i] + 2 == seat_ids[i + 1]:
                return seat_ids[i] + 1


print(f'{part_1()=} {part_2()=}')
