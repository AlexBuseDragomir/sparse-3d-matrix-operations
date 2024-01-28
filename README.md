A simple implementation for a module for 3D sparse matrices of real numbers.

A matrix is considered sparse if the number of its non zero elements is smaller than half of the total
number of stored values.
We represent the matrix by saving only the non null values, specified as tuple of form <i, j, k, v>, where
i = the x axis coordinate, j = the y axis coordinate, k = the z axis coordinate and v = the value stored
in that position.

The module offers the following list of operations:

-> matrix creation
-> matrix print
-> get matrix dimensions
-> read value from matrix
-> write value in matrix
-> matrix sum, difference
-> matrix multiplication
-> create unity matrix
-> create null matrix
-> get the transposed matrix
