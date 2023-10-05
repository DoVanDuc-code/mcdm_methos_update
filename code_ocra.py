from pymcdm.methods import OCRA
import numpy as np
from pymcdm.helpers import rrankdata
body = OCRA()
matrix = np.array([[7.7, 256, 7.2, 7.3, 7.3],
                    [8.1, 250, 7.9, 7.8, 7.7],
                    [8.7, 352, 8.6, 7.9, 8.0],
                    [8.1, 262, 7.0, 8.1, 7.2],
                    [6.5, 271, 6.3, 6.4, 6.1],
                    [6.8, 228, 7.1, 7.2, 6.5]])
weights = np.array([0.239, 0.225, 0.197, 0.186, 0.153])
types = np.array([1, -1, 1, 1, 1])
[round(preference, 3) for preference in body(matrix, weights, types)]
pref = body(matrix, weights, types)
np.round(pref, 4)
ranking = rrankdata(pref)

for r, p in zip(ranking, pref):
    print(r, round(p,3))

#==============================================     CODE XAY HAM    =======================================

