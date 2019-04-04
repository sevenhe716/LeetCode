# Time:  O(n)
# Space: O(1)

# 解题思路：
# 贪吃蛇用deque来存储效率更高
from collections import deque


class SnakeGame:
    def __init__(self, width: int, height: int, food: 'List[List[int]]'):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.food, self.food_idx = food, 0
        self.snake = deque([[0, 0]])
        self.size = (height, width)
        self.dirs = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}
        self.res = 0

    def move1(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        # print()
        # print(direction)
        # for i in range(self.size[0]):
        #     for j in range(self.size[1]):
        #         if self.food_idx < len(self.food) and [i, j] == self.food[self.food_idx]:
        #             print('F', end='')
        #         elif [i, j] in self.snake:
        #             print('S', end='')
        #         else:
        #             print('-', end='')
        #     print()

        pos = [self.snake[0][0] + self.dirs[direction][0], self.snake[0][1] + self.dirs[direction][1]]
        if pos[0] < 0 or pos[0] >= self.size[0] or pos[1] < 0 or pos[1] >= self.size[1]:
            return -1
        if self.food_idx < len(self.food) and pos == self.food[self.food_idx]:
            self.snake.appendleft(pos)
            self.food_idx += 1
        else:
            self.snake.pop()
            # 注意需要在这里判断，先将尾部移除再判断是否碰撞
            if pos in self.snake:
                return -1
            else:
                self.snake.appendleft(pos)
        return len(self.snake) - 1

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        pos = [self.snake[-1][0] + self.dirs[direction][0], self.snake[-1][1] + self.dirs[direction][1]]
        if pos[0] < 0 or pos[0] >= self.size[0] or pos[1] < 0 or pos[1] >= self.size[1]:
            return -1
        if self.food_idx < len(self.food) and pos == self.food[self.food_idx]:
            self.snake.append(pos)
            self.food_idx += 1
            self.res += 1
        else:
            self.snake.popleft()
            # 注意需要在这里判断，先将尾部移除再判断是否碰撞
            if pos in self.snake:
                return -1
            else:
                self.snake.append(pos)
        return self.res


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
