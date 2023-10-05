import numpy as np
from pymcdm.methods import COPRAS
from pymcdm.helpers import rrankdata
alts = np.array([
    [5, 8, 4],
    [7, 6, 8],
    [8, 8, 6],
    [7, 4, 6]
], dtype='int')
weights = np.array([0.3, 0.4, 0.3])
types = np.array([1, 1, 1])
topsis = COPRAS()
pref = topsis(alts, weights, types)
ranking = rrankdata(pref)
for r, p in zip(ranking, pref):
    # print(r, round(p,3))
    print(r,p)