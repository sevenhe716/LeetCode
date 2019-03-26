# Time:  O(n)
# Space: O(1)

# 解题思路：
# 因为step=1-9，可以每次只移动一步，建立索引加快查找速度


class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """

        # north = 0, east = 1, south = 2, west = 3
        dir = 0
        curx, cury = 0, 0
        int32_max = 2147483647
        int32_min = -2147483648
        max_dist = 0

        def turn_left():
            nonlocal dir
            dir -= 1
            if dir < 0:
                dir += 4

        def turn_right():
            nonlocal dir
            dir += 1
            if dir > 3:
                dir -= 4

        def find(is_x, greater):
            if is_x:
                if greater:
                    xs = [o[0] for o in obstacles if o[1] == cury and o[0] > curx]
                    if xs:
                        return min(xs), cury
                    else:
                        return int32_max, cury
                else:
                    xs = [o[0] for o in obstacles if o[1] == cury and o[0] < curx]
                    if xs:
                        return max(xs), cury
                    else:
                        return int32_min, cury
            else:
                if greater:
                    ys = [o[1] for o in obstacles if o[0] == curx and o[1] > cury]
                    if ys:
                        return curx, min(ys)
                    else:
                        return curx, int32_max
                else:
                    ys = [o[1] for o in obstacles if o[0] == curx and o[1] < cury]
                    if ys:
                        return curx, max(ys)
                    else:
                        return curx, int32_min

        def go_forward(dist):
            nonlocal curx, cury
            if dir == 0:
                ox, oy = find(False, True)
                if cury < oy <= cury + dist:
                    cury = oy - 1
                else:
                    cury = cury + dist
            elif dir == 1:
                ox, oy = find(True, True)
                if curx < ox <= curx + dist:
                    curx = ox - 1
                else:
                    curx = curx + dist
            elif dir == 2:
                ox, oy = find(False, False)
                if cury - dist <= oy < cury:
                    cury = oy + 1
                else:
                    cury = cury - dist
            elif dir == 3:
                ox, oy = find(True, False)
                if curx - dist <= ox < curx:
                    curx = ox + 1
                else:
                    curx = curx - dist

        for command in commands:
            print(curx, cury)

            if command == -2:
                turn_left()
            elif command == -1:
                turn_right()
            else:
                go_forward(command)
                max_dist = max(max_dist, curx * curx + cury * cury)

        return max_dist

    def robotSim2(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        self.p = (0, 0)
        self.d = (0, 1)
        self.r = 0
        self.obstacles = set(tuple(obstacle) for obstacle in obstacles)
        for command in commands:
            if command == -2:
                self.turnLeft()
            elif command == -1:
                self.turnRight()
            else:
                self.move(command)
        return self.r

    def turnLeft(self):
        self.d = (-self.d[1], self.d[0])

    def turnRight(self):
        self.d = (self.d[1], -self.d[0])

    def move(self, steps):
        for _ in range(steps):
            nextp = tuple(a + b for a, b in zip(self.p, self.d))
            if nextp not in self.obstacles:
                self.p = nextp
            else:
                break
        self.r = max(self.r, sum(d ** 2 for d in self.p))