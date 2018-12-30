import numpy as np


def make_grid(lambda_start, lambda_end, resolution=None, oversample=None):

    # check keywords
    if oversample == None: oversample = 40.0
    if resolution == None: resolution = 1500.0
    lambda_start = np.float128(lambda_start)
    lambda_end = np.float128(lambda_end)

    # produce grid
    R = resolution * oversample
    n_points = round( (np.log(lambda_end/lambda_start)) / (np.log(-(1 + 2 * R)/(1-2*R))) ) + 1
    f =  -(1 + 2 * R) / (1 - 2 * R)
    factor =  f ** np.arange(n_points)

    wave = np.full(int(n_points), lambda_start, dtype=np.float)
    grid = wave * factor

    return grid



'''
1- make a grid
2-
'''