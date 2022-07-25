class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows,cols=len(matrix),len(matrix[0])
        # Intervrting elements diagonally
        for r in range(rows):
            for c in range(r,cols):
                matrix[r][c],matrix[c][r]=matrix[c][r],matrix[r][c]
                
            # reversing the rows
        for r in range(rows):
            matrix[r]=matrix[r][::-1]
                
       