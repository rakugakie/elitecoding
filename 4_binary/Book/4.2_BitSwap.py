#4.2
def swap_bits(num: int, x: int, y: int) -> int:
    bit_mask = 1 << x | 1 << y
    return num ^ bit_mask
