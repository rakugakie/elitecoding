def reverse_bits(x: int, lenInBits: int) -> int:
    reversed = 0
    for i in range(0, lenInBits):
        reversed = reversed << 1 ^ (x & 1)
        x >>= 1
    return reversed