# Time:  O(n)
# Space: O(1)

# Ideas:
# simulator or find pattern (simulator only in one big loop)


class Solution:
    def wordsTyping(self, sentence: 'List[str]', rows: int, cols: int) -> int:
        word_len = list(map(len, sentence))

        # try to find pattern, record result in every line
        line_count = []
        idx = 0
        condition = True
        remain = cols
        count = 0
        firsts = [0]
        while condition:
            if remain >= word_len[idx]:
                print(sentence[idx], end=' ')
                remain -= word_len[idx] + 1
                idx = idx + 1
                if idx == len(word_len):
                    count += 1
                    idx = 0
                # idx = (idx + 1) % len(word_len)
            else:
                print()
                remain = cols
                line_count.append(count)

                # find a loop to exit
                if idx in firsts:
                    condition = False
                    repeat_index = idx
                else:
                    firsts.append(idx)

        print(repeat_index)
        print(line_count)
        print(firsts)

        rows -= 1
        if rows < len(line_count):
            return line_count[rows]
        else:
            start = firsts.index(repeat_index)
            c, r = divmod(rows - start, len(line_count) - start)
            repeat_count = line_count[-1] - (line_count[start-1] if start > 0 else 0)
            return line_count[r + start] + c * repeat_count
