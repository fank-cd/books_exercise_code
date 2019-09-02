# 回溯法
# 题目：请设计一个函数，用来判断一个矩阵中是否存在一条包含
# 某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以
# 在矩阵中向左、右、上、下移动一格。如果一条路径绕过了矩阵的某一格，
# 那么该路径不能再次进入该格子。例如，在下面 3*4 的矩阵中包含一条
# 字符串"bfce"的路径。但矩阵中不包含字符串"abfb"的路径，因为字符串
# 的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该
# 格子
"""

a   b   t   g
c   f   c   s
j   d   e   h

"""

def find_path_in_matrix(matrix, string):
    if not isinstance(matrix, list) or len(matrix) == 0 or len(matrix[0]) == 0 or \
            not isinstance(string, str) or len(string) == 0:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    for r in matrix:
        if not isinstance(r, list) or len(r) != cols:
            return False

    visited = [[False] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            # 遍历矩阵找到字符头
            if matrix[i][j] == string[0]:
                visited[i][j] = True
                # 递归寻找下一个字符
                found = find_recursively(matrix, string[1:], visited, (i, j))
                if found:
                    # 打印一下路径
                    for r in visited:
                        print(r)
                    return True
                visited[i][j] = False
    return False


def find_recursively(matrix, string, visited, matrix_indices):
    if len(string) <= 0:
        return True

    m_i, m_j = matrix_indices
    indices = []

    # 找到合法的上下左右indices
    for delta in (-1, 1):
        if 0 <= m_i + delta < len(matrix) and not visited[m_i + delta][m_j]:
            indices.append((m_i + delta, m_j))

        if 0 <= m_j + delta < len(matrix[0]) and not visited[m_i][m_j + delta]:
            indices.append((m_i, m_j + delta))

    # 看上下左右的字符哪一个与string的下一个字符相同，找到相同则继续递归
    for next_m_i, next_m_j in indices:
        if matrix[next_m_i][next_m_j] == string[0]:
            visited[next_m_i][next_m_j] = True
            found = find_recursively(matrix, string[1:], visited, (next_m_i, next_m_j))
            if found:
                return True
            visited[next_m_i][next_m_j] = False
    return False


if __name__ == "__main__":
    matrix = [
        ["a", "b", "t", "g"],
        ["c", "f", "c", "s"],
        ["j", "d", "e", "h"]
    ]
    string = "bfce"
    print(find_path_in_matrix(matrix=matrix, string=string))