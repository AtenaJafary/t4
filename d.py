





import pyfiglet

title=pyfiglet.figlet_format("tic tac teo", font="slant")
print (title)

game_board=[[" -"],[" -"],[" -"],
            [" -"],[" -"],[" -"],
            [" -"],[" -"],[" -"]]         

for row in game_board:
    for cell in row:
         print (cell,end="")
    print()

print("player1")
row=int(input())
col=int(input())

game_board[row][col]="x"
for row in game_board:
    for cell in row:
       print(cell,end="")
    print()