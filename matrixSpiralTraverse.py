class Directions:
    def __init__(self):
        self.left  = 0
        self.down  = 1
        self.right = 2
        self.up    = 3

class a:
    def __init__(self):
        directions = Directions()
        self.event_map = {directions.left  : 'left_dir',
                          directions.down  : 'down_dir',
                          directions.right : 'right_dir',
                          directions.up    : 'up_dir',
                         }
        self.clockwise_event_list = [directions.left, directions.down, directions.right, directions.up]
        self.anticlockwise_event_list = [directions.down, directions.left, directions.up, directions.right]
        self.answer = []

    def left_dir(self, min_row, max_row, min_col, max_col, direction):
        row = min_row if direction==0 else max_row-1
        j = min_col
        while j < max_col:
            self.answer.append(matrix[row][j])
            j+=1
        if direction == 0:
            self.min_row += 1
        else:
            self.max_row-=1
        
    def down_dir(self, min_row, max_row, min_col, max_col, direction): 
        col = max_col if direction==0 else min_col+1
        i = min_row
        while i < max_row:
            self.answer.append(matrix[i][col-1])
            i +=1
        if direction == 0:
            self.max_col-=1
        else:
            self.min_col +=1

    def right_dir(self, min_row, max_row, min_col, max_col, direction):
        row = max_row if direction==0 else min_row+1
        j = max_col-1
        while j >= min_col:
            self.answer.append(matrix[row-1][j])
            j -=1
        if direction == 0:
            self.max_row-=1
        else:
            self.min_row += 1
        
    def up_dir(self, min_row, max_row, min_col, max_col, direction):
        col = min_col if direction==0 else max_col-1
        i = max_row-1
        while i>=min_row:
            self.answer.append(matrix[i][col])
            i-=1
        if direction == 0:
            self.min_col += 1
        else:
            self.max_col -= 1

    def spiral_matrix(self, matrix, direction, position):
        row = len(matrix)
        col = len(matrix[0])
        self.min_row = 0
        self.max_row = row
        self.min_col = 0
        self.max_col = col
        if direction == 1: # adjusting position, if 1, then first down; 2, then first right;...
            position = 1-position+1

        while self.min_row<self.max_row and self.min_col<self.max_col:
            if direction == 0:
                event = self.clockwise_event_list[position-1]
            else: # if direction == 1
                event = self.anticlockwise_event_list[position-1]
            method = getattr(self, self.event_map[event])
            method(self.min_row, self.max_row, self.min_col, self.max_col, direction)
            position += 1
            position %= 4
        print self.answer
                
matrix = [[1,2,3,4], [5,6,7,8], [9, 10,11, 12], [13,14,15,16]]        
a().spiral_matrix(matrix, 0, 1)
a().spiral_matrix(matrix, 0, 2)
a().spiral_matrix(matrix, 0, 3)
a().spiral_matrix(matrix, 0, 4)

a().spiral_matrix(matrix, 1, 1)
a().spiral_matrix(matrix, 1, 2)
a().spiral_matrix(matrix, 1, 3)
a().spiral_matrix(matrix, 1, 4)
# 1 LT, 2 RT, 3 RB, 4 LB

# sampleArray = [[1,2,3,4],
#                [5,6,7,8],
#                [9,10,11,12],
#                [13,14,15,16]]
#
#
# spiral = 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10