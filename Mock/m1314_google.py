# Time:  O(n)
# Space: O(1)

# Ideas:
# cache in every trie
# trie['#'] = count
import heapq


class AutocompleteSystem:
    def __init__(self, sentences: 'List[str]', times: 'List[int]'):
        self.trie = {}
        self.size = 3
        self.cur_trie = self.trie
        self.cur_word = ''

        for s, t in zip(sentences, times):
            cur = self.trie
            for w in s:
                if w not in cur:
                    cur[w] = {}
                cur = cur[w]
            cur['#'] = (t, s)

        def dfs(trie):
            heap = []
            if '#' in trie:
                # ASCII-code order
                heapq.heappush(heap, trie['#'])

            for c in trie:
                if c != '#' and c != '*':
                    print(c)
                    # cache prioirty queue here
                    cur_heap = dfs(trie[c])
                    for item in cur_heap:
                        if len(heap) < self.size:
                            heapq.heappush(heap, item)
                        else:
                            heapq.heappushpop(heap, item)

            cur['*'] = heap
            return heap

        dfs(self.trie)

    def add_word(self):
        cur = self.trie
        for c in self.cur_word:
            if c not in cur:
                cur[c] = {}
                cur['*'] = [(-1, self.cur_word)]



        pass

    def input(self, c: str) -> 'List[str]':
        res = []
        if self.cur_trie and c in self.cur_trie:
            self.cur_trie = self.cur_trie[c]
            if self.cur_trie['*']:
                res = [item[1] for item in self.cur_trie['*']]

        if c == '#':
            self.add_word()
        else:
            self.cur_word += c

        return res




# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)