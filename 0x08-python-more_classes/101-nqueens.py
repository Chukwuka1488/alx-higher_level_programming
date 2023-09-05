#!/usr/bin/python3
import sys

class NQueensSolver:
    """
    NQueensSolver class for solving the N Queens problem.

    Attributes:
        n (int): The size of the chessboard (N).
        board (list of lists): A 2D list representing the chessboard.
    """

    def __init__(self, n):
        """
        Initialize a new NQueensSolver instance.

        Args:
            n (int): The size of the chessboard (N).
        """
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def is_safe(self, row, col):
        """
        Check if it's safe to place a queen at board[row][col].

        Args:
            row (int): The row to check.
            col (int): The column to check.

        Returns:
            bool: True if it's safe to place a queen, False otherwise.
        """
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve(self):
        """
        Solve the N Queens problem.

        Returns:
            list of lists: A list of solutions, where each solution is a list of queen positions.
        """
        return self._solve(0)

    def _solve(self, col):
        """
        Recursive helper function to solve the N Queens problem.

        Args:
            col (int): The current column.

        Returns:
            list of lists: A list of solutions, where each solution is a list of queen positions.
        """
        if col >= self.n:
            return [self.get_solution()]

        solutions = []
        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                partial_solutions = self._solve(col + 1)
                solutions.extend(partial_solutions)
                self.board[i][col] = 0

        return solutions

    def get_solution(self):
        """
        Get the current solution as a list of queen positions.

        Returns:
            list of lists: A list of queen positions, where each position is represented as [row, col].
        """
        solution = []
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col] == 1:
                    solution.append([row, col])
        return solution

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(N)
    solutions = solver.solve()

    for solution in solutions:
        print(solution)
