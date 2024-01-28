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
my_matrix = []

# while we take correct decision inputs
while my_selection in input_list:

    my_selection = int(input("Please insert your selection: "))
    print()

    # if the selection is correct
    if my_selection in input_list:

        if my_selection == 1:
            matrix_dimension = int(input("Please insert the number of non null elements you would like to insert: "))
            print()
            my_matrix = create_matrix(matrix_dimension)
            print()

        if my_selection == 2:
            # if we have already created a matrix
            if my_matrix:
                print_matrix(my_matrix)
            else:
                print("First you must create a matrix!")
                print()

        if my_selection == 3:
            # if we have already created a matrix
            if my_matrix:
                matrix_size = get_matrix_size(my_matrix)
                print("Your matrix has %s rows, %s columns and %s pages" % (matrix_size[0], matrix_size[1], matrix_size[2]))
                print()
            else:
                print("First you must create a matrix!")
                print()

        if my_selection == 4:
            # if we have already created a matrix
            if my_matrix:
                # we ask for the position of the searched value
                my_i = int(input("Please insert from which row: "))
                my_j = int(input("Please insert from which column: "))
                my_k = int(input("Please insert from which page: "))
                print()
                get_matrix_value(my_i, my_j, my_k, my_matrix)
                print()
            else:
                print("First you must create a matrix!")
                print()

        if my_selection == 5:
            # if we have already created a matrix
            if my_matrix:
                # we ask for the position in which we will insert a new value (overwrite the last value)
                my_i = int(input("Please insert in which row: "))
                my_j = int(input("Please insert in which column: "))
                my_k = int(input("Please insert in which page: "))
                new_value = float(input("Please insert your new value: "))
                print()
                set_result = set_matrix_value(my_i, my_j, my_k, my_matrix, new_value)
                print()
                print("This is how your matrix looks like now:")
                print_matrix(set_result)
            else:
                print("First you must create a matrix!")
                print()

        if my_selection == 6:
            print("You have to insert two matrices and the program will display the sum.")
            print("The two matrices must have the same dimension")
            print()
            matrix_dimension1 = int(input("Number of non null elements you would like to insert in MATRIX 1: "))
            print()
            my_matrix1 = create_matrix(matrix_dimension1)
            print()
            matrix_dimension2 = int(input("Number of non null elements you would like to insert in MATRIX 2: "))
            print()
            my_matrix2 = create_matrix(matrix_dimension2)

            # we check if the matrices have the same size
            if get_matrix_size(my_matrix1) != get_matrix_size(my_matrix2):
                print()
                print("Please insert two matrices with the same dimensions!")
                print()
            # we are good to go
            else:
                print()
                print("Your matrices are shown below. The third matrix is the resulting sum.")
                print()
                print("   FIRST MATRIX")
                print_matrix(my_matrix1)
                print("   SECOND MATRIX")
                print_matrix(my_matrix2)
                sum_matrix = matrix_sum(my_matrix1, my_matrix2)
                print("   SUM MATRIX")
                print_matrix(sum_matrix)

        if my_selection == 7:
            print("You have to insert two matrices and the program will display the difference.")
            print("The two matrices must have the same dimension")
            print()
            matrix_dimension1 = int(input("Number of non null elements you would like to insert in MATRIX 1: "))
            print()
            my_matrix1 = create_matrix(matrix_dimension1)
            print()
            matrix_dimension2 = int(input("Number of non null elements you would like to insert in MATRIX 2: "))
            print()
            my_matrix2 = create_matrix(matrix_dimension2)

            # we check if the matrices have the same size
            if get_matrix_size(my_matrix1) != get_matrix_size(my_matrix2):
                print()
                print("Please insert two matrices with the same dimensions!")
                print()
            # we are good to go
            else:
                print()
                print("Your matrices are shown below. The third matrix is the resulting difference.")
                print()
                print("   FIRST MATRIX")
                print_matrix(my_matrix1)
                print("   SECOND MATRIX")
                print_matrix(my_matrix2)
                difference_matrix = matrix_difference(my_matrix1, my_matrix2)
                print("   DIFFERENCE MATRIX")
                print_matrix(difference_matrix)

        if my_selection == 8:
            print("You have to insert two matrices and the program will display the product.")
            print("Matrices must be of form (i, j, k) and (k, m, n)")
            print()
            matrix_dimension1 = int(input("Number of non null elements you would like to insert in MATRIX 1: "))
            print()
            my_matrix1 = create_matrix(matrix_dimension1)
            print()
            matrix_dimension2 = int(input("Number of non null elements you would like to insert in MATRIX 2: "))
            print()
            my_matrix2 = create_matrix(matrix_dimension2)

            # we check if the number of pages of matrix 1 == number of rows of matrix 2
            my_tuple1 = get_matrix_size(my_matrix1)
            my_tuple2 = get_matrix_size(my_matrix2)

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
                print_matrix(my_matrix1)
                print("   SECOND MATRIX")
                print_matrix(my_matrix2)
                product_matrix = matrix_multiplication(my_matrix1, my_matrix2)
                print("   PRODUCT MATRIX (under the form of a list of tuples with a value field != 0)")
                print(product_matrix)
                print()

        if my_selection == 9:
            print("Let's create a NULL matrix of a given size.")
            my_i = int(input("Please insert the number of rows: "))
            my_j = int(input("Please insert the number of columns: "))
            my_k = int(input("Please insert the number of pages: "))
            my_null_matrix = null_matrix(my_i, my_j, my_k)
            print_matrix(my_null_matrix)
            print()

        if my_selection == 10:
            print("Let's create an IDENTITY matrix of a given size. The matrix must be cubic")
            my_i = int(input("Please insert the number that will be equal for rows, columns and pages: "))
            my_identity_matrix = identity_matrix(my_i)
            print_matrix(my_identity_matrix)
            print()

        if my_selection == 11:
            # if we have already created a matrix
            if my_matrix:
                print("TRANSPOSED MATRIX:")
                transposed_matrix = matrix_transpose(my_matrix)
                print_matrix(transposed_matrix)
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