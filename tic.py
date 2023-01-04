def show():
    for row in game_board :
        for coll in row :
            print(coll,end="")
    print()

game_board= [[" -"],[" -"],[" -"],
            [" -"],[" -"],[" -"],
            [" -"],[" -"],[" -"]]
show()
while True :
    print("playar1")
    while True:
        row= int(input()) 
        coll=int(input())
        if game_board [row][coll]== " -" :
            game_board [row][coll]="x"
            show()
            break
        else :
            print("khone gige entekhab kon")
        print("player2")
        while True :
            row=int(input())
            coll=int(input())
            if game_board[row][coll]==" -":
                game_board[row][coll]="o"
                show()
                break
            else:
                print("khone dige entekhab kon")


          