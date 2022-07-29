# iven an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of hash(t)
# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.


# Sample Input
# 2
# 1 2

# Sample Output
# 3713081631934410656



n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))
    print(hash(integer_list))
