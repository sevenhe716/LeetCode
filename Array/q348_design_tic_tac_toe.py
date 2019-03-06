# Time:  O(n)
# Space: O(1)

# 解题思路：
#


# 不验证操作，默认都是合法的
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.size = n
        self.marks = [[0] * n for _ in range(n)]
        self.player_mark = {1: -1, 2: 1}

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.marks[row][col] = self.player_mark[player]
        if abs(sum(self.marks[row])) == self.size or \
                abs(sum(self.marks[i][col] for i in range(self.size))) == self.size or \
                row == col and abs(sum(self.marks[i][i] for i in range(self.size))) == self.size or \
                row == self.size - 1 - col and abs(sum(self.marks[i][self.size - i - 1] for i in range(self.size))) == self.size:
            return 2 if self.marks[row][col] == 1 else 1
        else:
            return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

class TicTacToe1:

    def __init__(self, n: 'int'):
        """
        Initialize your data structure here.
        """
        self.size = n
        self.players = [{
            "row": [0] * n,
            "col": [0] * n,
            "dia": 0,
            "rdia": 0
        } for _ in range(2)]

    def move(self, row: 'int', col: 'int', player: 'int') -> 'int':
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        p = self.players[player - 1]

        p["row"][row] += 1
        if p["row"][row] == self.size:
            return player

        p["col"][col] += 1
        if p["col"][col] == self.size:
            return player

        if row + col == self.size - 1:
            p["dia"] += 1
            if p["dia"] == self.size:
                return player

        if row == col:
            p["rdia"] += 1
            if p["rdia"] == self.size:
                return player