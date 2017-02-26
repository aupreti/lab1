import pdb
import numpy as np
from pig import Pig

'''
Matrix Implementation

'''
num_pigs = 6
tx_delay = 0.9


def matrix_creation(size):
    matrix = np.zeros((size, size), dtype = int)
    directions = [[-1,0],[1,0],[0,-1],[0,1],[1,1],[-1,1],[1,-1],[-1,-1]]
    location_list=[]
    pig_list = []
    stone_list = []
    
    num_stones = int(size/4)
    
    #Place pigs in the matrix
    
    for i in range(num_pigs):
        pig_location = np.random.choice(size,2, replace = True)
        while [pig_location[0],pig_location[1]] in location_list:
            pig_location = np.random.choice(size,2, replace = True)
        matrix[pig_location[0],pig_location[1]] = 1
        location_list.append([pig_location[0],pig_location[1]])
        pig_list.append(Pig((pig_location[0],pig_location[1]), len(pig_list)))
        
    
    #Place stones in the matrix:
    for i in range(num_stones):
        stone_location = np.random.choice(size,2, replace = True)
        while [stone_location[0],stone_location[1]] in stone_list and [stone_location[0],stone_location[1]] in location_list:
            stone_location = np.random.choice(size,2, replace = True)
        matrix[stone_location[0],stone_location[1]] = 2
        stone_list.append([stone_location[0],stone_location[1]])
    pdb.set_trace()
    
    
if __name__ == '__main__':
      matrix_creation(4)
