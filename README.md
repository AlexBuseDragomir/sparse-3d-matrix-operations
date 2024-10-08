# Sparse 3D Matrix Module

A simple implementation for a module that handles 3D sparse matrices of real numbers.   
This has been a college assignment for the Object Oriented Programming module.  
  
A matrix is considered sparse if the number of its non-zero elements is smaller than half of the total number of stored values.   
The matrix is represented by saving only the non-null values, specified as tuples in the form `<i, j, k, v>`, where:

- `i`: the x-axis coordinate  
- `j`: the y-axis coordinate  
- `k`: the z-axis coordinate  
- `v`: the value stored in that position

## Supported Operations

- **Matrix creation**
- **Matrix print**
- **Get matrix dimensions**
- **Read value from matrix**
- **Write value in matrix**
- **Matrix sum**
- **Matrix difference**
- **Matrix multiplication**
- **Create unity matrix**
- **Create null matrix**
- **Get the transposed matrix**
