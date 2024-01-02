#!/usr/bin/env python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
    m_a (list of lists): The first matrix.
    m_b (list of lists): The second matrix.

    Returns:
    numpy.ndarray: The result of the matrix multiplication.

    Raises:
    ValueError: If m_a and m_b can't be multiplied.

    Example:
    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    array([[ 7, 10],
           [15, 22]])
    """

    result = np.dot(m_a, m_b)

    return result

# Sample usage
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[1, 2], [3, 4]]
result = lazy_matrix_mul(matrix_a, matrix_b)
print(result)

