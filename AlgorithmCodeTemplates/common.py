# refer to https://time.geekbang.org/course/detail/130-42710
'''
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
        print_result
        return

    # process logic in current level
    process_data(level, data...)

    # drill down
    recursion(level+1, param1, param2, ...)

    # reverse the current level status if needed
    reverse_state(level)
'''


# interval merge
# definition: interval = [start, end]
def add_interval(new_interval, intervals):
    if intervals and intervals[-1][1] >= new_interval[0]:
        if intervals[-1][1] < new_interval[1]:
            intervals[-1][1] = new_interval[1]
    else:
        intervals.append(new_interval)


