# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """

        cur_fuel = startFuel
        cur_dist = 0

        stations.sort()

        count = 0

        while cur_dist + cur_fuel < target:
            if len(stations) == 0:
                return -1

            reach_dist = cur_dist + cur_fuel

            available_index = 0

            for i in range(len(stations)):
                if stations[i][0] > reach_dist:
                    available_index = i
                    break

            if stations[-1][0] <= reach_dist:
                available_index = len(stations)

            if available_index == 0:
                return -1

            max_i = 0
            max_f = 0
            for i in range(available_index):
                if stations[i][1] > max_f:
                    max_f = stations[i][1]
                    max_i = i

            cur_station = stations[max_i]

            cur_fuel -= cur_station[0] - cur_dist
            cur_fuel += cur_station[1]
            cur_dist = cur_station[0]

            count += 1

            stations = stations[:max_i] + stations[max_i+1:]

        return count
