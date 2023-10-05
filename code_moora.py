from pymcdm.helpers import rrankdata
from pymcdm.methods import MOORA
import numpy as np
body = MOORA()
matrix = np.array([[1.5, 3, 5, 3.3],
                    [2, 7, 5, 3.35],
                    [3, 1, 5, 3.07],
                    [2.2, 4, 5, 3.5],
                    [2, 5, 3, 3.09],
                    [3.2, 2, 3, 3.48],
                    [2.775, 3, 5, 3.27]])
weights = np.array([0.3, 0.2, 0.1, 0.4])
types = np.array([-1, 1, 1, 1])
[round(preference, 4) for preference in body(matrix, weights, types)]
pref = body(matrix, weights, types)
rank = rrankdata(pref)
for r, p in zip(rank, pref):
    print(r, round(p,3))

# ==========================================    CODE XÂY HÀM    =======================================#
'''
import numpy as np
from pymcdm.helpers import rrankdata

def _moora(matrix, weights, cryteria_types):
    nmatrix = matrix / np.sqrt(np.sum(matrix ** 2, axis=0))

    # Difficult normalized decision making matrix
    wmatrix = nmatrix * weights
    # Calculate the composite score
    cscore = np.sum(wmatrix[:, cryteria_types == 1], axis=1) - np.sum(wmatrix[:, cryteria_types == -1], axis=1)
    return cscore
if __name__ == "__main__":
    data = np.array([
        [5,8,4],
        [7,8,6],
        [8,8,6],
        [7,4,6]
    ], dtype='int')
weights = np.array([0.3, 0.4, 0.3])
types = np.array([1,1,1])
a = _moora(data, weights, types)
rank = rrankdata(a)
for r,p in zip(rank,a):
    print(r, p)
'''