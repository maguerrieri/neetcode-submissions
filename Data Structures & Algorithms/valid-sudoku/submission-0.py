class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [[set[str]() for _ in range(3)] for _ in range(3)]
        columns = [set[str]() for _ in range(9)]
        for i, row in enumerate(board):
            row_set = set()
            for j, cell in enumerate(row):
                # print(f"checking {i}, {j}")
                if cell != ".":
                    column = columns[j]
                    square = squares[i // 3][j // 3]
                    if cell in row_set:
                        # print(f"{cell} in row {i}: {row_set})")
                        return False
                    if cell in column:
                        # print(f"{cell} in column {j}: {column})")
                        return False
                    if cell in square:
                        # print(f"{cell} in square {i % 3}, {j % 3}: {square})")
                        return False
                    row_set.add(cell)
                    column.add(cell)
                    square.add(cell)
        return True