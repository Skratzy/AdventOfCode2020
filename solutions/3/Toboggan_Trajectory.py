def is_at_position(letter, posX, string):
    print(f'{posX % len(string)=} {posX} {len(string)=} {string[posX % len(string)]=}')
    return string[posX % len(string)] == letter


def part_1():
    with open("1.txt", "r") as file:
        numTrees = 0
        posX = 0
        for line in file:
            if is_at_position('#', posX, line.strip()):
                numTrees += 1
            posX += 3
        return numTrees


def part_2():
    with open("1.txt", "r") as file:
        file_contents = file.readlines()
        traversals = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
        product = 1
        for traversal in traversals:
            numTrees = 0
            posX, posY = 0, 0
            for posY in range(0, len(file_contents), traversal[1]):
                if is_at_position('#', posX, file_contents[posY].strip()):
                    numTrees += 1
                posX += traversal[0]
            product *= numTrees
        return product


print(f'{part_1()=} {part_2()=}')
