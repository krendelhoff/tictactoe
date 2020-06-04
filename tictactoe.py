field = [[" ", " ", " "] for i in range(0, 9, 3)]
counter = 0

while True:

    print("---------")
    for one, two, three in field:  # unpacking bro

        print(f"| {one} {two} {three} |")

    print("---------")

    empty = len([column for row in field for column in row if column in ["_", " "]])

    x_win = False
    o_win = False

    columns = []
    rows = field

    diag1 = [field[j][j] for i in range(3) for j in range(3) if i == j]
    diag2 = [field[2][0], field[1][1], field[0][2]]

    test_x = ["X" for i in range(3)]
    test_o = ["O" for i in range(3)]

    for i in range(3):

        tmp = []
        for j in range(3):

            tmp.append(field[j][i])

        columns.append(tmp)

    x_win = test_x in rows or test_x in columns or test_x == diag1 or test_x == diag2
    o_win = test_o in rows or test_o in columns or test_o == diag1 or test_o == diag2

    if x_win is True:
        print("X wins")
        break

    elif o_win is True:

        print("O wins")
        break

    elif empty == 0:

        print("Draw")
        break

    else:

        while True:
            print("Enter the coordinates: ", end="")
            coordinates = input().split()
            digit = True

            for c in coordinates:

                if not c.isdigit():

                    digit = False
                    break

            if digit is True:
                coordinates = [int(x) for x in coordinates]
                coordinates[0] = coordinates[0] - 1
                coordinates[1] = 3 - coordinates[1]

            if digit is False:

                print("You should enter numbers!")

            elif not(2 >= coordinates[0] >= 0 and 2 >= coordinates[1] >= 0):

                print("Coordinates should be from 1 to 3!")

            elif field[coordinates[1]][coordinates[0]] not in [" ", "_"]:

                print("This cell is occupied! Choose another one!")

            else:
                counter += 1

                if counter % 2:
                    field[coordinates[1]][coordinates[0]] = "X"
                else:
                    field[coordinates[1]][coordinates[0]] = "O"

                break






