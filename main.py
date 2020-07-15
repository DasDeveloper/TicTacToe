def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def checkWin():
    if myBoard["1"] == myBoard["4"] == myBoard["7"] == "X" or myBoard["2"] == myBoard["5"] == myBoard["8"] == "X" or \
            myBoard["3"] == myBoard["6"] == myBoard["9"] == "X":
        print("X won!")
        return True
    elif myBoard["1"] == myBoard["4"] == myBoard["7"] == "O" or myBoard["2"] == myBoard["5"] == myBoard["8"] == "O" or \
            myBoard["3"] == myBoard["6"] == myBoard["9"] == "O":
        print("O won!")
        return True
    elif myBoard["1"] == myBoard["2"] == myBoard["3"] == "O" or myBoard["4"] == myBoard["5"] == myBoard["6"] == "O" or \
            myBoard["7"] == myBoard["8"] == myBoard["9"] == "O":
        print("O won!")
        return True
    elif myBoard["1"] == myBoard["2"] == myBoard["3"] == "X" or myBoard["4"] == myBoard["5"] == myBoard["6"] == "X" or \
            myBoard["7"] == myBoard["8"] == myBoard["9"] == "X":
        print("X won!")
        return True
    elif myBoard["1"] == myBoard["5"] == myBoard["9"] == "O" or myBoard["3"] == myBoard["5"] == myBoard["7"] == "O":
        print("O won!")
        return True
    elif myBoard["1"] == myBoard["5"] == myBoard["9"] == "X" or myBoard["3"] == myBoard["5"] == myBoard["7"] == "X":
        print("X won!")
        return True


run = True

while run:
    myBoard = {'7': ' ', '8': ' ', '9': ' ',
               '4': ' ', '5': ' ', '6': ' ',
               '1': ' ', '2': ' ', '3': ' '}

    keys = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
    printBoard(myBoard)
    for i in keys:
        location = input("Where: ")
        myBoard['' + location + ''] = i
        printBoard(myBoard)
        if checkWin():
            break
    if not checkWin():
        print("Tie!")

    play_again = input("Want to play again (y/n) : ")
    if play_again.lower() == "y":
        pass
    if play_again.lower() != "y" or "n":
        print("Put the correct answer")
        play_again = input("Want to play again (y/n) : ")
    elif play_again == "n":
        run = False
        print("Thanks for playing!")
