#!/usr/bin/env python3


from .parity2 import parity


PRECOMPUTED_PARITY = {x: parity(x) for x in range(2**16)}


def parity3(x: int) -> int: 
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE)
                                & BIT_MASK] ^ PRECOMPUTED_PARITY[x & BIT_MASK])
