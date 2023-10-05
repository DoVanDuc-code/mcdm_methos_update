import numpy as np
from pymcdm.methods import COMET
from pymcdm.helpers import rrankdata

matrix = np.array([[ 96, 145, 200],
                  [100, 145, 200],
                  [120, 170,  80],
                  [140, 180, 140],
                  [100, 110,  30]])
types = np.ones(3)
weights = np.ones(3)/3
cvalues = COMET.make_cvalues(matrix)
body = COMET(cvalues, COMET.topsis_rate_function(weights, types))
pref = body(matrix)
np.round(pref, 4)
ranking = rrankdata(pref)

for r, p in zip(ranking, pref):
    print(r, round(p,3))