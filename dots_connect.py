def generate_populated_matrix(no_coordinates,grid_height,grid_width):
    """
    param 1: total number of points in the matrix
    param 2: number of indeces wide (x-axis)
    param 3: number of indeces tall (y-axis)
    """
    from random import randint
    #set comprehension
    #generate random points for grid
    cross_coordinates = {tuple((randint(0,grid_width-1),randint(0,grid_height-1))) for i in range(no_coordinates)}
    while True:
        if len(cross_coordinates) != no_coordinates:
            non_duplicate = tuple((randint(0,grid_width-1),randint(0,grid_height-1)))
            if non_duplicate not in cross_coordinates:
                cross_coordinates.add(non_duplicate)
            continue
        else:
            break

    #generate and populate matrix one pass
    matrix = []
    for row in range(grid_height):
        # print(row)
        matrix.append([])
        for col in range(grid_width):
            # print(col)
            if (row,col) in cross_coordinates:
                matrix[row].append('x')
            else:    
                matrix[row].append('o')
    
    
    return matrix,list(cross_coordinates) #converted to an iterable




def dot_connect(matrix, coordinates):
    """
    DP solution iterative
    input matrix to modify inplace
    iterable of coordinates (x,y)
    """
    print(coordinates)

    def calc_jump(diff):
        if diff>0:
            return -1
        elif diff==0:
            return 0
        else:
            return 1

    def draw_path(coord1,coord2):
        nonlocal matrix
     
        y_diff=  coord1[0]-coord2[0]# negtive if destination further right
        x_diff = coord1[1]-coord2[1] # negative if destination further down
        
        #units to navigate grid
        x_jump = calc_jump(x_diff)
        y_jump = calc_jump(y_diff)
        
        
            
        next_row,next_col= coord1[0],coord1[1]
        moves_left = abs(x_diff)+abs(y_diff)
        y_moves,x_moves=abs(y_diff),abs(x_diff)
       
        #this will folow a zigzag motion until one column or row matches with destination then it will take a straight path
        while moves_left>0:
            # print(moves_left)
            if moves_left%2 ==0:
                if y_moves ==0:
                    next_col= next_col+x_jump
                    x_moves-=1
                else:
                    next_row= next_row+y_jump
                    y_moves-=1
            else:
                if x_moves ==0:
                    next_row= next_row+y_jump
                    y_moves-=1
                else:
                    next_col= next_col+x_jump
                    x_moves-=1

            # + signifies a cross that has a line in its square
            if matrix[next_row][next_col] == 'x':
                pass
            else:
                matrix[next_row][next_col] = '.'
            moves_left-=1

            
        # print(x_moves,y_moves)
        # print(next_row,next_col)
        return matrix

    #contains list of indeces of dots connected
    connected=[False for x in range(len(coordinates))]

    for n in range(len(coordinates)):
        for m in range(len(coordinates)):
            if m == n or connected[m] is True:
                continue
            else:
                draw_path(coordinates[n],coordinates[m])
    return matrix

