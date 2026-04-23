
def generate_desk(matrix):
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end='')
            if j < 2:
                print('|', end='')
        print()
        if i < 2:
            print('-----')
matrix = [[5,5,5], [5,5,5], [5,5,5]]

def check_winner(matrix, symbol):
    for i in range(3):
        if matrix[i][2] == matrix[i][1] == matrix[i][0] == symbol:
            return True
        
    for i in range(3):
        if matrix[2][i] == matrix[1][i] == matrix[0][i] == symbol:
            return True
        
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == symbol:
        return True
        
    if matrix[0][2] == matrix[1][1] == matrix[2][0] == symbol:
        return True
        
    return False
    
def check_draw(matrix):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                return False
                
    return True
    
def minmax(matrix, isMaximizing):
    if check_winner(matrix, 5):
        return 1
    elif check_winner(matrix, 6):
        return -1
    elif check_draw(matrix):
        return 0
        
    if isMaximizing:
        '''
        Maximizing when player is the AI
        we want him to make the best move
        and for the player we will choose the move with
        the least potential loss for the AI bot - using recursion 
        to compute all the possibles outcomes and then all the recursive
        functions will pass backward the already computed min/max values 
        to the upper levels of the function
        Example:
        
            MIN -> RECURSION TREE OF THE ALL POSSIBLE GAME MOVES
            / \
           MAX MAX
           / \ / \ 
          -5 5 6 -66
        get max from (-5, 5) -> 5 and then max from (6, -66) -> 6
        then get the min from (5, 6) -> 5 so the left subtree
        '''
        Best = -5e5
        for i in range(3):
            for j in range(3):
                if matrix[i][j] == 0:
                    matrix[i][j] = 5
                    Best = max(Best, minmax(matrix, False))
                    matrix[i][j] = 0
            
    else:
        Best = 5e5
        for i in range(3):
            for j in range(3):
                if matrix[i][j] == 0:
                    matrix[i][j] = 6
                    Best = min(Best, minmax(matrix,  True))
                    matrix[i][j] = 0
    
    return Best

def ai_move(matrix):
    besti = -5e5
    maxi=-5
    maxj=-5
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                matrix[i][j] = 5
                '''
                The AI player has already placed
                a move, so now we are not maximimizing 
                so that's why it is False
                '''
                result = minmax(matrix, False)
                matrix[i][j] = 0
                
                if besti < result:
                    besti = result
                    maxj = j
                    maxi = i
    return maxi,maxj
    
    
def play_game():
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while True:
        if check_winner(matrix, 5):
            print("Player one wins")
        elif check_winner(matrix, 6):
            print("Player two wins")
        elif check_draw(matrix):
            print("Moone wins")
            
        print("Insert move")
        
        x = int(input("Input x: "))
        y = int(input("Input y: "))
        while x < 0 or x > 2 or y < 0 or y > 2 or matrix[x][y] != 0:
            print("Invalid")
            x = int(input("Input x: "))
            y = int(input("Input y: "))
        matrix[x][y] = 6
        ai_x, ai_y = ai_move(matrix)
        matrix[ai_x][ai_y] = 5
        generate_desk(matrix)


play_game()
