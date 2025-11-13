def build_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        matrix.append(row)
    return matrix