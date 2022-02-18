# masking and lookup table

PRECOMPUTED_PARITY = []


def parity_on(x: int) -> int:
    parity = 0
    while x:
        parity ^= x & 1
        x >>= 1
    return parity


def parity_drop_lowest_set_bit(x: int) -> int:
    parity = 0
    while x:
        parity ^= x & 1
        x &= x - 1


def parity_caching(x: int) -> int:
    mask = 0xFFFF
    mask_size = 16
    return (PRECOMPUTED_PARITY[x >> (3 * mask_size)] ^
            PRECOMPUTED_PARITY[x >> (2 * mask_size) & mask] ^
            PRECOMPUTED_PARITY[x >> (1 * mask_size) & mask] ^
            PRECOMPUTED_PARITY[x >> (0 * mask_size) & mask])


# XOR is communicative
# The CPU word level instructions let us process multiple bits at the same time.
def parity_communicative(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1

    return x
