#!/usr/bin/env python3


def matrix_in_spiral_order(square_matrix: list[list[int]]) -> list[int]:
    def matrix_layer_in_clockwise(offset):
        if offset == len(square_matrix) - offset - 1:
            # square_matrix has odd dimension, and we are at the center of the
            # matrix square_matrix.
            spiral_ordering.append(square_matrix[offset][offset])
            return

        spiral_ordering.extend(square_matrix[offset][offset : -1 - offset])
        spiral_ordering.extend(
            list(zip(*square_matrix))[-1 - offset][offset : -1 - offset]
        )
        spiral_ordering.extend(square_matrix[-1 - offset][-1 - offset : offset : -1])
        spiral_ordering.extend(
            list(zip(*square_matrix))[offset][-1 - offset : offset : -1]
        )

    spiral_ordering: list[int] = []
    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise(offset)
    return spiral_ordering
