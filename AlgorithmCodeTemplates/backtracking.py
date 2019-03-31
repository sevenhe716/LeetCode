# Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, notably
#  constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate
#  ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
#
# backtracking vs. dfs
# traverse in solution space vs. traverse in data structure space, pruned of dfs


def backtracking(self, P, c):
    if self.reject(P, c):
        return

    if self.accept(P, c):
        return self.output(P, c)

    for s in self.all_extension(P, c):
        backtracking(s)

