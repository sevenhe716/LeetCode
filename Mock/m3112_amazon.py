# Time:  O(k)
# Space: O(k)

# Ideas:
# simulation will be too slow
# bit manipulation and loop dectect, string operator is more fast to code than bit


class Solution:
    def prisonAfterNDays(self, cells: 'List[int]', N: int) -> 'List[int]':
        cell_index = {}
        repeat_index = -1

        cell_bit = 0
        for c in cells:
            cell_bit = (cell_bit << 1) + c
        cell_index[cell_bit] = 0

        for i in range(N):
            new_cell_bit = 0
            mask = 2 ** 6
            for _ in range(1, len(cells) - 1):
                if (cell_bit & (mask << 1) == 0) == (cell_bit & (mask >> 1) == 0):
                    new_cell_bit = (new_cell_bit << 1) + 1
                else:
                    new_cell_bit <<= 1
                mask >>= 1
            new_cell_bit <<= 1

            if new_cell_bit not in cell_index:
                cell_index[new_cell_bit] = i + 1
            else:
                repeat_index = cell_index[new_cell_bit]
                break

            cell_bit = new_cell_bit

        if repeat_index == -1:
            return list(map(int, list('{:08b}'.format(new_cell_bit))))
        else:
            repeat_count = len(cell_index) - repeat_index
            idx = (N - repeat_index) % repeat_count + repeat_index
            for k, v in cell_index.items():
                if v == idx:
                    return list(map(int, list('{:08b}'.format(k))))


