# Time:  O(n)
# Space: O(k)

# Ideas:
# simulator or find pattern (simulator only in one big loop)
# simulator word by word is too slow, find loop pattern is a good idea


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
                remain -= word_len[idx] + 1
                idx = idx + 1
                if idx == len(word_len):
                    count += 1
                    idx = 0
            else:
                remain = cols
                line_count.append(count)

                # find it already
                if rows == len(line_count):
                    return line_count[-1]

                # find a loop to exit
                for i, f in enumerate(firsts):
                    if idx == f:
                        start = i
                        condition = False
                        break
                else:
                    firsts.append(idx)

        # start = firsts.index(repeat_index)
        c, r = divmod(rows - 1 - start, len(line_count) - start)
        repeat_count = line_count[-1] - (line_count[start - 1] if start > 0 else 0)
        return line_count[r + start] + c * repeat_count


class Solution1:
    # simulation
    def wordsTyping(self, sentence, rows, cols):
        s = ' '.join(sentence) + ' '
        start, l = 0, len(s)
        for i in range(rows):
            start += cols
            while s[start % l] != ' ':
                start -= 1
            start += 1
        return start // l

    # backtrack table
    def wordsTyping1(self, words, rows, cols):
        sentence = " ".join(words) + ' '
        sentence_len = len(sentence)

        prev = -1
        backtrack = [0] * sentence_len
        for i in range(sentence_len):
            if sentence[i] == ' ':
                prev = i
            backtrack[i] = i - (prev + 1)

        pos = 0
        for _ in range(rows):
            pos += cols
            pos -= backtrack[pos % sentence_len]

        return (pos + 1) // sentence_len
