# 約数を求めるプログラム
import math

def divisor(n):
    result = []
    N = math.floor(math.sqrt(n))
    for i in range(1, N+1):
        if n % i == 0:
            result.append(i)
            if N != i:
                result.append(n // i)
    result.sort()
    return result

if __name__ == "__main__":
    print(divisor(5))
    print(divisor(16))
    print(divisor(256))
    print(divisor(100000))
    print(divisor(651091685081))