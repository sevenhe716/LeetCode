# Time:  O(n)
# Space: O(1)

# Ideas:
# cache in every trie
# trie['#'] = count
# 比较容易实现的方式是，维护整个queue，或sort
import heapq


class HeapItem:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    # 解决ASCII-code排序问题
    def __lt__(self, other):
        if self.count != other.count:
            return self.count < other.count
        else:
            return self.word > other.word

    def __repr__(self):
        return self.word + ',' + str(self.count)

    def clone(other):
        return HeapItem(other.count, other.word)


class AutocompleteSystem:
    def __init__(self, sentences: 'List[str]', times: 'List[int]'):
        self.trie = {}
        self.size = 3
        self.cur_trie = self.trie
        self.cur_word = ''

        for s, t in zip(sentences, times):
            cur = self.trie
            for c in s:
                cur = cur.setdefault(c, {})
            cur['#'] = HeapItem(t, s)

        def dfs(trie):
            heap = []
            if '#' in trie:
                # ASCII-code order
                heapq.heappush(heap, HeapItem.clone(trie['#']))

            for c in trie:
                if c != '#' and c != '*':
                    # cache prioirty queue here
                    cur_heap = dfs(trie[c])
                    for item in cur_heap:
                        if len(heap) < self.size:
                            heapq.heappush(heap, HeapItem.clone(item))
                        else:
                            heapq.heappushpop(heap, HeapItem.clone(item))
            trie['*'] = heap
            return heap

        dfs(self.trie)

    def add_word(self):
        cur = self.trie
        for c in self.cur_word:
            if c not in cur:
                cur[c] = {}
                cur[c]['*'] = []
            cur = cur[c]
        if '#' not in cur:
            cur['#'] = HeapItem(1, self.cur_word)
        else:
            cur['#'].count += 1

        word_item = cur['#']

        cur = self.trie
        for c in self.cur_word:
            cur = cur[c]
            heap = cur['*']
            for i in range(len(heap)):
                if heap[i].word == word_item.word:
                    heap[i].count += 1
                    # heapq.heapify(heap)
                    heapq._siftup(heap, i)
                    break
            else:
                if len(heap) < self.size:
                    heapq.heappush(heap, HeapItem.clone(word_item))
                else:
                    heapq.heappushpop(heap, HeapItem.clone(word_item))

    def input(self, c: str) -> 'List[str]':
        res = []

        if c == '#':
            self.add_word()
            self.cur_trie = self.trie
            self.cur_word = ''
        else:
            self.cur_word += c

            if not self.cur_trie:
                return []
            if c not in self.cur_trie:
                self.cur_trie = None
                return []

            if c in self.cur_trie:
                self.cur_trie = self.cur_trie[c]
                if self.cur_trie['*']:
                    res = [item.word for item in sorted(self.cur_trie['*'], reverse=True)]

        return res

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
