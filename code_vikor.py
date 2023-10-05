import numpy as np
from objective_weighting.mcda_methods import VIKOR
from objective_weighting import weighting_methods as mcda_weights
from objective_weighting import normalizations as norms
from objective_weighting.additions import rank_preferences

matrix = np.array([
        [5, 8, 4],
        [7, 6, 8],
        [8, 8, 6],
        [7, 4, 6],
    ], dtype='int')

weights = np.array([0.3, 0.4, 0.3])
types = np.array([1, 1, 1])
# weights = mcda_weights.entropy_weighting(matrix)

# Create the VIKOR method object
vikor = VIKOR(normalization_method=norms.minmax_normalization)
# Calculate alternatives preference function values with VIKOR method
pref = vikor(matrix, weights, types)
# Rank alternatives according to preference values
rank = rank_preferences(pref, reverse = False)
for r, p in zip(rank, pref):
    print(r, p)