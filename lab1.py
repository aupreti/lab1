import pdb
import numpy as np
'''
Matrix Implementation

'''
num_pigs = 6



def matrix_creation(size):
    matrix = np.zeros((size, size), dtype = int)
    directions = [[-1,0],[1,0],[0,-1],[0,1],[1,1],[-1,1],[1,-1],[-1,-1]]
    location_list = []

    for i in range(num_pigs):
        pig_location = np.random.choice(size,2, replace = True)
        while [pig_location[0],pig_location[1]] in location_list:
            pig_location = np.random.choice(size,2, replace = True)
        matrix[pig_location[0],pig_location[1]] = 1
        location_list.append([pig_location[0],pig_location[1]])
    pdb.set_trace()

    return location_list


if __name__ == '__main__':
      matrix_creation(4)
