# Write an algorithm to determine if a number is happy.
#
# A happy number is a number defined by the following
# process: Starting with any positive integer,
# replace the number by the sum of the squares of
# its digits, and repeat the process until the number
# equals 1 (where it will stay), or it loops
# endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1
# are happy numbers.

# Example
# 19 is a happy number
#
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

def isHappy(n):

    test = set()

    while n !=1:
        s = 0
        N = str(n)
        for i in range(len(N)):
            s = int(N[i])**2 + s
        if s in test:
            return "unhappy"
        else:
            if s == 1:
                return "happy"
            else:
                test.add(s)
        n = s

print (isHappy(4))
