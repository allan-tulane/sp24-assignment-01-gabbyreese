"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        return foo(x-1) + foo(x-2)

def longest_run(mylist, key):
    seq_len = 0
    longest = 0
    for v in mylist:
        if v == key:
            seq_len += 1
        else:
            if seq_len > longest:
                longest = seq_len
            seq_len = 0
    return max(longest, seq_len)


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    if len(mylist) == 1:
        if mylist[0] == key:            
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)

    # each thread spawns more threads
    result1 = _longest_run_recursive(mylist[:len(mylist)//2], key)
    result2 = _longest_run_recursive(mylist[len(mylist)//2:], key)
    return combine_results(result1, result2)



