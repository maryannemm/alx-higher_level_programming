#!/usr/bin/env python3

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
    m_a (list of lists): The first matrix.
    m_b (list of lists): The second matrix.

    Returns:
    list of lists: The result of the matrix multiplication.

    Raises:
    TypeError: If m_a or m_b is not a list, not a list of lists, or contains non-integer/float elements.
              If m_a or m_b is not a rectangle (all ‘rows’ should be of the same size).
    ValueError: If m_a and m_b can't be multiplied.

    Example:
    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7, 10], [15, 22]]
    """

    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")

    if m_a == [] or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")

    if m_b == [] or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size" if len(m_a) > 1 else "each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result

# Sample usage
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[1, 2], [3, 4]]
result = matrix_mul(matrix_a, matrix_b)
print(result)

