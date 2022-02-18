def add(a: int, b: int) -> int:
    while (b):
        carry = (a & b) << 1
        a ^= b
        b = carry
    return a

def computeProduct(x: int, y: int) -> int:

    sum = 0
    count = 0
    while x:
        if x & 1:
            sum = add(sum, y << count)
        count += 1
        x >>= 1
    return sum


if __name__ == '__main__':
    print(computeProduct(4, 5))

