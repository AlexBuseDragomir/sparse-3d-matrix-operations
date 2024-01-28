from module import *

print(chr(27) + "[2J")
print("                           Welcome to the 3D rare matrix application!")
print()
print("Please choose an option from the list below:")
print("-> 1. Create your matrix")
print("-> 2. Print your matrix")
print("-> 3. Get the size of your matrix")
print("-> 4. Get a value from your matrix")
print("-> 5. Write/Rewrite a value in the matrix")
print("-> 6. Calculate the sum of two matrices")
print("-> 7. Calculate the difference of two matrices")
print("-> 8. Calculate the product of two matrices")
print("-> 9. Create a null matrix with a given dimension")
print("-> 10. Create an identity matrix with a given dimension")
print("-> 11. Calculate the transpose of a matrix")
print()

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# we want to get in the while at least once so we make my_selection = 1
my_selection = 1

matrix1 = Matrix3D()
matrix2 = Matrix3D()

# while we take correct decision inputs
while my_selection in input_list:

    my_selection = int(input("Please insert your selection: "))
    print()

    # if the selection is correct
    if my_selection in input_list:

        if my_selection == 1:
            matrix1.number_of_elements = int(input("Input the number of non null elements you would like to insert: "))
            print()
            matrix1.create_matrix()
            print()

        if my_selection == 2:
            # if we have already created a matrix
            if matrix1.list_of_elements:
                matrix1.print_matrix()
            else:
                print("First you must create a matrix!")
                print()

        if my_selection == 3:
            # if we have already created a matrix
            if matrix1.list_of_elements:
                matrix_size = matrix1.get_matrix_size()
                print("Your matrix has %s rows, %s columns and %s pages" %
                      (matrix_size[0], matrix_size[1], matrix_size[2]))
                print()

            else:
                print("First you must create a matrix!")
                print()

        if my_selection == 4:
            # if we have already created a matrix
            if matrix1.list_of_elements:
                # we ask for the position of the searched value
                my_i = int(input("Please insert from which row: "))
                my_j = int(input("Please insert from which column: "))
                my_k = int(input("Please insert from which page: "))
                print()
                matrix1.get_matrix_value(my_i, my_j, my_k)
                print()
            else:
                print("First you must create a matrix!")
                print()

        if my_selection == 5:
            # if we have already created a matrix
            if matrix1.list_of_elements:
                # we ask for the position in which we will insert a new value (overwrite the last value)
                my_i = int(input("Please insert in which row: "))
                my_j = int(input("Please insert in which column: "))
                my_k = int(input("Please insert in which page: "))
                new_value = float(input("Please insert your new value: "))
                print()

                matrix1.list_of_elements = matrix1.set_matrix_value(my_i, my_j, my_k, new_value)

                print()
                print("This is how your matrix looks like now:")
                matrix1.print_matrix()
            else:
                print("First you must create a matrix!")
                print()

        if my_selection == 6:

            matrix3 = Matrix3D()
            matrix4 = Matrix3D()

            operation = Operations3D(matrix3, matrix4)

            print("You have to insert two matrices and the program will display the sum.")
            print("The two matrices must have the same dimension")
            print()
            matrix3.number_of_elements = int(input("Number of non null elements you would like to insert in MATRIX 1: "))
            print()
            matrix3.create_matrix()
            print()
            matrix4.number_of_elements = int(input("Number of non null elements you would like to insert in MATRIX 2: "))
            print()
            matrix4.create_matrix()

            # we check if the matrices have the same size
            if matrix3.get_matrix_size() != matrix4.get_matrix_size():
                print()
                print("Please insert two matrices with the same dimensions!")
                print()

            # we are good to go
            else:
                print()
                print("Your matrices are shown below. The third matrix is the resulting sum.")
                print()
                print("   FIRST MATRIX")
                matrix3.print_matrix()
                print("   SECOND MATRIX")
                matrix4.print_matrix()

                # we save in this list of tuples the return value of the function
                sum_matrix = operation.matrix_sum()
                # we will use matrix_auxiliary in order to print the resulting matrix
                matrix_auxiliary = Matrix3D()
                matrix_auxiliary.list_of_elements = sum_matrix

                print("   SUM MATRIX")
                matrix_auxiliary.print_matrix()

        if my_selection == 7:

            matrix3 = Matrix3D()
            matrix4 = Matrix3D()

            operation = Operations3D(matrix3, matrix4)

            print("You have to insert two matrices and the program will display the difference.")
            print("The two matrices must have the same dimension")
            print()
            matrix3.number_of_elements = int(input("Number of non null elements you would like to insert in MATRIX 1: "))
            print()
            matrix3.create_matrix()
            print()
            matrix4.number_of_elements = int(input("Number of non null elements you would like to insert in MATRIX 2: "))
            print()
            matrix4.create_matrix()

            # we check if the matrices have the same size
            if matrix3.get_matrix_size() != matrix4.get_matrix_size():
                print()
                print("Please insert two matrices with the same dimensions!")
                print()
            # we are good to go
            else:
                print()
                print("Your matrices are shown below. The third matrix is the resulting difference.")
                print()
                print("   FIRST MATRIX")
                matrix3.print_matrix()
                print("   SECOND MATRIX")
                matrix4.print_matrix()

                # we save in this list of tuples the return value of the function
                difference_matrix = operation.matrix_difference()
                # we will use matrix_auxiliary in order to print the resulting matrix
                matrix_auxiliary = Matrix3D()
                matrix_auxiliary.list_of_elements = difference_matrix

                print("   DIFFERENCE MATRIX")
                matrix_auxiliary.print_matrix()

        if my_selection == 8:

            matrix3 = Matrix3D()
            matrix4 = Matrix3D()

            operation = Operations3D(matrix3, matrix4)

            print("You have to insert two matrices and the program will display the product.")
            print("Matrices must be of form (i, j, k) and (k, m, n)")
            print()
            matrix3.number_of_elements = int(input("Number of non null elements you would like to insert in MATRIX 1: "))
            print()
            matrix3.create_matrix()
            print()
            matrix4.number_of_elements = int(input("Number of non null elements you would like to insert in MATRIX 2: "))
            print()
            matrix4.create_matrix()

            # we check if the number of pages of matrix 1 == number of rows of matrix 2
            my_tuple1 = matrix3.get_matrix_size()
            my_tuple2 = matrix4.get_matrix_size()

            if my_tuple1[2] != my_tuple2[0]:
                print()
                print("Please insert a matrix 1 with k pages and a matrix 2 with k rows!")
                print()

            # we are good to go
            else:
                print()
                print("Your matrices are shown below. The third matrix is the resulting product.")
                print()
                print("   FIRST MATRIX")
                matrix3.print_matrix()
                print("   SECOND MATRIX")
                matrix4.print_matrix()

                # we save in this list of tuples the return value of the function
                product_list = operation.matrix_multiplication()
                print("   PRODUCT MATRIX (under the form of a list of tuples with a value field != 0)")
                print(product_list)
                print()

        if my_selection == 9:
            # we will save in this object of type Matrix3D the null matrix
            my_matrix = Matrix3D()

            print("Let's create a NULL matrix of a given size.")
            my_i = int(input("Please insert the number of rows: "))
            my_j = int(input("Please insert the number of columns: "))
            my_k = int(input("Please insert the number of pages: "))

            # initialising our matrix with the correct list of elements and the number (of elements)
            my_matrix.list_of_elements = my_matrix.null_matrix(my_i, my_k, my_j)
            my_matrix.number_of_elements = len(my_matrix.list_of_elements)
            my_matrix.print_matrix()
            print()

        if my_selection == 10:
            # we will save in this object of type Matrix3D the identity matrix
            my_matrix = Matrix3D()

            print("Let's create an IDENTITY matrix of a given size. The matrix must be cubic")
            my_i = int(input("Please insert the number that will be equal for rows, columns and pages: "))

            # initialising our matrix with the correct list of elements and the number (of elements)
            my_matrix.list_of_elements = my_matrix.identity_matrix(my_i)
            my_matrix.number_of_elements = len(my_matrix.list_of_elements)
            my_matrix.print_matrix()
            print()

        if my_selection == 11:

            operation = Operations3D(matrix1, matrix2)

            # if we have already created a matrix
            if matrix1.list_of_elements:
                print("TRANSPOSED MATRIX:")

                # modifying our matrix object and its members
                matrix1.list_of_elements = operation.matrix_transpose()
                # we can proceed to printing because the number of elements does not change
                # so we do not need to update it
                matrix1.print_matrix()
                print()
            else:
                print("First you must create a matrix!")
                print()

        print()
        print("Please choose an option from the list below:")
        print("-> 1. Create your matrix")
        print("-> 2. Print your matrix")
        print("-> 3. Get the size of your matrix")
        print("-> 4. Get a value from your matrix")
        print("-> 5. Write/Rewrite a value in the matrix")
        print("-> 6. Calculate the sum of two matrices")
        print("-> 7. Calculate the difference of two matrices")
        print("-> 8. Calculate the product of two matrices")
        print("-> 9. Create a null matrix with a given dimension")
        print("-> 10. Create an identity matrix with a given dimension")
        print("-> 11. Calculate the transpose of a matrix")
        print()


