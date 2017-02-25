import pdb
import numpy as np
'''
Matrix Implementation

'''

def matrix_creation(size):
    matrix = np.zeros((size, size), dtype = int)
    #pdb.set_trace()
    directions = [[-1,0],[1,0],[0,-1],[0,1],[1,1],[-1,1],[1,-1],[-1,-1]]
    pig_location = np.random.choice(size,2, replace = True)
    #matrix[pig_location]
    pdb.set_trace()


if __name__ == '__main__':
      matrix_creation(4)
     