#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices
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
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a and m_b are lists of lists
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    # Check if all elements in m_a and m_b are integers or floats
    for row in m_a:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Check if all rows in m_a and m_b are the same size
    row_len = len(m_a[0])
    for row in m_a:
        if len(row) != row_len:
            raise TypeError("each row of m_a must be of the same size")
    row_len = len(m_b[0])
    for row in m_b:
        if len(row) != row_len:
            raise TypeError("each row of m_b must be of the same size")

    # Check if the matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        result.append([])
        for j in range(len(m_b[0])):
            product = 0
            for k in range(len(m_b)):
                product += m_a[i][k] * m_b[k][j]
            result[i].append(product)

    return result
