class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1.0

        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        current = x

        while n > 0:
            if n % 2 == 1:
                result *= current
            current *= current
            n //= 2

        return result

