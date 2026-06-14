import random
size = 6
bomb = 6

def create_board():
    board = [['']* size for _ in range(size)]
    bomb_positions = random.sample([(i,j) for i in range (size) for j in range (size)],bomb)
    for i,j in bomb_positions:
        board[i][j] = '*'
    return board, bomb_positions

def count_adjacent_bombs(board, row, col):
    count=0
    for i in range(max(0, row-1), min(size, row+2)):
        for j in range(max(0, col-1), min(size, col+2)):
            if board[i][j]=='*':
                count +=1
    return count

def play_game():
    board, bomb_positions = create_board()
    revealed = [['-']*size for _ in range(size)]
    safecells = size * size - bomb

    while safecells>0:
        for row in revealed:
            print(' '.join(row))
        try:
            r=int(input("enter row (0-5):"))
            c=int(input("enter col (0-5):"))
            if board [r][c] == '*':
                print("BOOM YOU HIT A BOMB LOSER YOUR GAME IS OVER")
                return
            if revealed [r][c]=='-':
                count = count_adjacent_bombs(board, r, c)
                revealed[r][c] = str(count) 
                safecells-=1

        except Exception as e:
            print("INVALID INPUT")
    print("CONGRATULATIONS YOU WON")

play_game()