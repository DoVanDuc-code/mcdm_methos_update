from pymcdm.methods import MARCOS
import numpy as np
from pymcdm.helpers import rrankdata
body = MARCOS()
matrix = np.array([[660, 1000, 1600, 18, 1200],
                    [800, 1000, 1600, 24, 900],
                    [980, 1000, 2500, 24, 900],
                    [920, 1500, 1600, 24, 900],
                    [1380, 1500, 1500, 24, 1150],
                    [1230, 1000, 1600, 24, 1150],
                    [680, 1500, 1600, 18, 1100],
                    [960, 2000, 1600, 12, 1150]])
weights = np.array([0.1061, 0.3476, 0.3330, 0.1185, 0.0949])
types = np.array([-1, 1, 1, 1, 1])
[round(preference, 4) for preference in body(matrix, weights, types)]
pref = body(matrix, weights,types)
rank = rrankdata(pref)
for r, p in zip(rank, pref):
    print(r, round(p,3))


    #================================================== CODE XAY HAM ==================================#
"""
import normalization as normalization
import numpy as np
from pymcdm import normalizations, helpers
from pymcdm.helpers import rrankdata
from pymcdm.methods.marcos import _marcos_normalization


def _marcos(matrix, weights, types, normalization):
    normalization = _marcos_normalization

    n, m = matrix.shape

    # Extended initial decision matrix
    exmatrix = np.zeros((n + 2, m))
    exmatrix[:-2] = matrix

    max_maxes = matrix.max(axis=0)
    min_values = matrix.min(axis=0)

    for i in range(m):
        if types[i] == 1:
            exmatrix[-2, i] = max_maxes[i]
            exmatrix[-1, i] = min_values[i]
        else:
            exmatrix[-2, i] = min_values[i]
            exmatrix[-1, i] = max_maxes[i]

    # Normalization
    n_exmatrix = helpers.normalize_matrix(exmatrix, normalization, types)

    # Weighting
    weighted_matrix = n_exmatrix * weights

    # Utility degree
    S = weighted_matrix.sum(axis=1)
    k_neg = (S / S[-1])[:-2]
    k_pos = (S / S[-2])[:-2]

    # Utility functions
    f_k_pos = k_neg / (k_pos + k_neg)
    f_k_neg = k_pos / (k_pos + k_neg)
    f_k = (k_pos + k_neg) / (1 + (1 - f_k_pos) / f_k_pos + (1 - f_k_neg) / f_k_neg)
    return f_k
if __name__ == "__main__":
    data = np.array([
                    [5, 8, 4],
                    [7, 6, 8],
                    [8, 8, 6],
                    [7, 4, 6],
                ], dtype='int')
weights = np.array([0.3, 0.4, 0.3])
types = np.array([1, 1, 1])
pref = _marcos(data, weights, types, normalization)
rank = rrankdata(pref)
for r, p in zip(rank , pref):
    print(r,round(p,3))
"""
