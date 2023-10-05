from pymcdm.methods import COPRAS
from pymcdm.helpers import rrankdata
import numpy as np
body = COPRAS()
matrix = np.array([[1543, 2000, 39000, 15, 13.76, 3.86, 5, 3, 5000],
                    [1496, 3600, 43000, 14, 14, 2.5, 4, 4, 4000],
                    [1584, 3100, 24500, 10, 13.1, 3.7, 2, 2, 3500],
                    [1560, 2700, 36000, 12, 13.2, 3.2, 3, 3, 3500],
                    [1572, 2500, 31500, 13, 13.3, 3.4, 3, 2, 3500],
                    [1580, 2400, 20000, 12, 12.8, 3.9, 2, 2, 3000]])
weights = np.array([0.2027, 0.1757, 0.1622, 0.1351, 0.1081, 0.0946, 0.0676, 0.0405, 0.0135])
types = np.array([-1, -1, -1, 1, 1, -1, 1, 1, 1])
[round(preference, 4) for preference in body(matrix, weights, types)]
pref = body(matrix, weights, types)
rank = rrankdata(pref)
for r, p in zip(rank, pref):
    print(r,round(p,3))
