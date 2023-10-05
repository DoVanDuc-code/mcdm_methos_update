import normalization as normalization
import numpy as np
from pymcdm import normalizations, helpers
from pymcdm.helpers import rrankdata

def _mairca(data, weights, types, normalization):
    normalization = normalizations.minmax_normalization
    n, _ = data.shape
    # tao ma tran xep hang ly thuyet
    # Creating theoretical ranking matrix
    Tp = 1 / n * weights
    # tạo ma tran danh gia thuc
    # Creating real rating matrix
    nmatrix = helpers.normalize_matrix(data, normalization, types)
    Tr = nmatrix * Tp

    # Calculation of Total Gap Matrix
    G =  Tr - Tp

    # Calculation the final values of criteria functions
    return np.sum(G, axis=1)
if __name__ == "__main__":
    data = np.array([
                    [5, 8, 4],
                    [7, 6, 8],
                    [8, 8, 6],
                    [7, 4, 6],
                ], dtype='int')

    # Trọng số ứng với mỗi tiêu chí (giả định)
    weights = np.array([0.3, 0.4, 0.3])
    types = np.array([1, 1, 1])
    pref = _mairca(data, weights, types, normalization)
    ranking = rrankdata(pref)
    for r, p in zip(ranking, pref):
        print(r, round(p, 3))
