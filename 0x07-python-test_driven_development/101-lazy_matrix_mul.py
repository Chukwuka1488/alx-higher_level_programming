#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module
    Args:
        m_a: list of lists of integers or floats
        m_b: list of lists of integers or floats
    Returns:
        A new matrix containing the product of m_a and m_b
    Raises:
        TypeError: if m_a or m_b is not a list, if m_a or m_b is not a list of lists,
                   if one element of those list of lists is not an integer or a float,
                   or if m_a or m_b is not a rectangle (all ‘rows’ should be of the same size)
        ValueError: if m_a or m_b is empty, or if m_a and m_b can’t be multiplied
    """
    # Convert input matrices to NumPy arrays
    try:
        a = np.array(m_a)
        b = np.array(m_b)
    except:
        raise TypeError("m_a and m_b must be lists of lists")

    # Check if all elements in a and b are integers or floats
    if not (a.dtype == int or a.dtype == float):
        raise TypeError("m_a should contain only integers or floats")
    if not (b.dtype == int or b.dtype == float):
        raise TypeError("m_b should contain only integers or floats")

    # Check if a and b are not empty
    if a.size == 0:
        raise ValueError("m_a can't be empty")
    if b.size == 0:
        raise ValueError("m_b can't be empty")

    # Check if the matrices can be multiplied
    if a.shape[1] != b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication using NumPy's dot function
    return np.dot(a, b)
