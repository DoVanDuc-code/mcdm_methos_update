import numpy as np
from pymcdm.methods import MABAC
from pymcdm.helpers import rrankdata
def marba(data, weights):

    # Chuẩn hóa các giá trị của mỗi tiêu chí
    normalized_data = data / np.max(data, axis=0)

    # Tính điểm MarBA cho từng lựa chọn
    marba_scores = np.dot(normalized_data, weights)

    return marba_scores

# Ví dụ sử dụng phương pháp MarBA với dữ liệu giả định
if __name__ == "__main__":
    # Ma trận dữ liệu MCDM với 5 tiêu chí và 8 lựa chọn
    data = np.array([
        [5, 8, 4],
        [7, 6, 8],
        [8, 8, 6],
        [7, 4, 6],
    ], dtype='int')

    # Trọng số ứng với mỗi tiêu chí (giả định)
    weights = np.array([0.3, 0.4, 0.3])
    types = np.array([1, 1, 1])
    marbac = MABAC()
    pref = marba(data, weights)
    ranking = rrankdata(pref)
    for r, p in zip(ranking, pref):
        print(r, round(p, 3))
