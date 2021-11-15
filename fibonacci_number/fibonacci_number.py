n = input('Please enter the nth term of Fibonacci:')

class Solution():
    def fibonacci(self, n):
        fibonacci = [0, 1]
        for i in range(2, n + 1):
            fibonacci.append(fibonacci[i - 1] + fibonacci [i - 2])
            last = fibonacci[-1]
        return last
    # fill this in.

#n = 9
print(Solution().fibonacci(int(n)))
# 34
