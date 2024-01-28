# function that asks for inputs of form <i,j,k,v>
# i is the row, j the column and k the page of the 3D matrix
# v is the real number stored in Matrix[i][j][k]
# the function stores these tuples in a list (only for v != 0)
# we specify the number of elements of the matrix

def create_matrix(number_of_elements):
    # we will use this in the process of printing a matrix
    values = []

    # we create number_of_elements values
    for iterator in range(0, number_of_elements, 1):

        # we input from keyboard the position and the value of a matrix element
        i = int(input("Please insert the line: "))
        j = int(input("Please insert the column: "))
        k = int(input("Please insert the page: "))
        v = float(input("Please insert the value: "))
        print()

        # we save in a tuple our current matrix element
        my_tuple = (i, j, k, v)

        # we check if we have already inserted an element in that position
        if (i, j, k, v) not in values:
            # we save the current tuple in out list of matrix elements
            values.append(my_tuple)

        # we have already inserted a value in that position
        else:
            print("That value is already inserted there!")
            print()

    print("The following tuples have been saved: ")
    print(values)
    # the function returns the list of tuples
    return values


# function that will get as argument a list of tuples and print the list
# tuples represent the values != 0 from the matrix

def print_matrix(list_of_elements):
    # we will save tuples later in this list
    auxiliary_list = []

    # first of all, we have to determine how big our matrix is
    # in other words, the printed matrix will be of form M[rows][columns][pages]
    # where rows = max(i), columns = max(j) and pages = max(k)
    # in other words, our matrix must encapsulate / contain all the created values

    rows = -1
    columns = -1
    pages = -1

    # we iterate trough our list of matrix values
    # and save the minimum number of rows, columns and the depth
    # necessary in order to encapsulate all elements
    for iterator in range(0, len(list_of_elements), 1):

        if list_of_elements[iterator][0] > rows:
            rows = list_of_elements[iterator][0]

        if list_of_elements[iterator][1] > columns:
            columns = list_of_elements[iterator][1]

        if list_of_elements[iterator][2] > pages:
            pages = list_of_elements[iterator][2]

    # we print the size of the matrix
    # we have a special function that does the exact same thing but I think that it is an useful tool
    # in order to check if our matrix is correctly printed
    print()
    print("Our matrix has %s rows, %s columns and %s pages:" % (rows + 1, columns + 1, pages + 1))
    print()
    # we print the matrix page by page
    # a page is a depth, so depth 0 is the first page, depth 1 is the second page etc
    # every page is a two-dimensional matrix with a fixed number of rows and columns
    # we will consider that the first depth is the page on top and the depth k is the k-th page

    # passing trough the pages (depths)
    for iterator1 in range(0, pages + 1, 1):
        # a normal print of a two-dimensional array
        for iterator2 in range(0, rows + 1, 1):
            # we check if we have a tuple that saves a value for this position
            # if it is one, we print the value
            # else we just print a 0 because we saved only values != 0
            for iterator3 in range(0, columns + 1, 1):
                # we will search if there is a tuple saved for this position
                # we do so by using list comprehension
                # if the list will be non empty, then there is a value != 0 in that position and we print it
                auxiliary_list = [item for item in list_of_elements if
                                  item[0] == iterator2 and item[1] == iterator3 and item[2] == iterator1]

                # list is not empty we print the value stored in the tuple
                if len(auxiliary_list) != 0:
                    print(auxiliary_list[0][3], end="")
                    print("       ", end="")

                # we have no non null value for that position
                else:
                    print('0', end="")
                    print("       ", end="")

            # we go to a new line
            print()

        # we leave a blank space and start printing the next page
        print()
        print()


# after we create a matrix using the function provided above, we can get its size
# by calling print_matrix_size with an argument : a list of tuples reperesenting the inputs
def get_matrix_size(list_of_elements):
    # initialisation of rows, columns and pages
    rows = -1
    columns = -1
    pages = -1

    # we get the minimum number of rows, columns and pages
    # that are necessary in order to encapsulate all elements from input
    for iterator in range(0, len(list_of_elements), 1):

        if list_of_elements[iterator][0] > rows:
            rows = list_of_elements[iterator][0]

        if list_of_elements[iterator][1] > columns:
            columns = list_of_elements[iterator][1]

        if list_of_elements[iterator][2] > pages:
            pages = list_of_elements[iterator][2]

    # we return a tuple containing the number of rows, columns and matrix pages
    return (rows + 1, columns + 1, pages + 1)


# the program will ask for the searched position (my_i, my_j, my_k) and the list of matrix values
def get_matrix_value(my_i, my_j, my_k, list_of_elements):
    # we check if the input is correct
    # we may want to check for an element that is not even inside our matrix_size
    # (my_i > number of rows, my_j > number of columns etc.)
    matrix_size = get_matrix_size(list_of_elements)

    if my_i >= matrix_size[0] or my_j >= matrix_size[1] or my_k >= matrix_size[2]:
        print("There is no element with these coordinates!")

    # we are searching for an element that is inside the matrix
    else:

        # we will save in auxiliary_list the tuples from list_of_elements that are of form (my_i, my_j, my_k, value)
        # where my_i, my_j and my_k are the coordinates of the searched element

        # we will save here the searched value
        searched_value = 0

        # searching for the element in the list of tuples
        auxiliary_list = [item for item in list_of_elements if
                          item[0] == my_i and item[1] == my_j and item[2] == my_k]

        # we verify if our list has an element (if we have a non null value)
        # if the list has no element, then we have a null value in that position
        # we cannot have two values on the same position, so auxiliary_list will have either 0 or 1 elements
        if len(auxiliary_list) == 1:
            searched_value = auxiliary_list[0][3]
            print("The element with the coordinates (%s, %s, %s) is %s" % (my_i, my_j, my_k, searched_value))
        else:
            # searched_value will have the initial value, so 0
            print("The element with the coordinates (%s, %s, %s) is %s" % (my_i, my_j, my_k, searched_value))


# my_i, my_j, my_k are the coordinates in which we will insert set_value
# list_of_values contains our tuples of form (i, j, k, value)

def set_matrix_value(my_i, my_j, my_k, list_of_elements, set_value):
    # we check if the input is correct
    # we may want to check for an element that is not even inside our matrix_size
    # (my_i >= number of rows, my_j >= number of columns etc.)
    # we use >= because values are saved from 0 and my_i, my_j, my_k represent indices
    matrix_size = get_matrix_size(list_of_elements)

    if my_i >= matrix_size[0] or my_j >= matrix_size[1] or my_k >= matrix_size[2]:
        print("There is no element with these coordinates")

    # we are searching for an element that is inside the matrix
    else:
        # we will save in auxiliary_list the tuples from list_of_elements that are of form (my_i, my_j, my_k, value)
        # where my_i, my_j and my_k are the coordinates of the searched element

        # searching for the element in the list of tuples
        auxiliary_list = [item for item in list_of_elements if
                          item[0] == my_i and item[1] == my_j and item[2] == my_k]

        # we verify if our list is empty or not
        # we ask the user if he would like to overwrite the data

        # list is not empty
        if auxiliary_list:
            print("The element with the coordinates (%s, %s, %s) is %s" % (my_i, my_j, my_k, auxiliary_list[0][3]))
            answer = input("Do you want to overwrite this value? (y/n) ")

            # if the answer is yes, we find the value in the original list of tuples and replace it
            if answer == 'y':
                for it in range(0, len(list_of_elements), 1):
                    if list_of_elements[it][0] == my_i and list_of_elements[it][1] == my_j \
                            and list_of_elements[it][2] == my_k:
                        print("The value %s was replaced by the value %s" % (list_of_elements[it][3], set_value))
                        # we replace the whole tuple because tuples are immutable objects
                        list_of_elements[it] = (my_i, my_j, my_k, set_value)

            elif answer == 'n':
                print("The matrix was not modified.")

            else:
                print("No action was performed because your answer was incorrect")

        # list is empty
        else:
            print("The element with the coordinates (%s, %s, %s) is %s" % (my_i, my_j, my_k, '0'))
            answer = input("Do you want to overwrite this value? (y/n) ")

            # if the answer is yes, we find the value in the original list of tuples and replace it
            if answer == 'y':
                print("The value %s was replaced by the value %s" % ('0', set_value))
                # because previously the tuple with these coordinates was not save (value was 0)
                # now we just append it to the list of elements
                list_of_elements.append((my_i, my_j, my_k, set_value))

            elif answer == 'n':
                print("The matrix was not modified")

            else:
                print("No action was performed because the answer was incorrect")

    # we return the modified list
    return list_of_elements


# we will get two lists of elements, namely the tuples of matrix1 and those of matrix2
# we will calculate the sum of the two matrices
def matrix_sum(matrix1, matrix2):
    sum_of_matrices = []

    # we consider that the two matrices have the same dimension so we iterate trough their tuples and add values

    # if a non null element is neither in matrix1, nor in matrix2, we do not save it in a tuple
    # if a non null element is just in one matrix, we save it as it is
    # if a non null element is in both matrices, we save the value of the sum

    # here we check elements from both matrices and elements that are just in first matrix
    for iterator1 in range(0, len(matrix1), 1):

        tuple1 = matrix1[iterator1]
        flag = 0

        # we search for non null elements in matrix2 that are in matrix1 too
        for iterator2 in range(0, len(matrix2), 1):
            if tuple1[0] == matrix2[iterator2][0] and tuple1[1] == matrix2[iterator2][1] \
                    and tuple1[2] == matrix2[iterator2][2]:
                # tells us if we found a non null element in matrix2 or it is just in matrix1
                flag = 1
                tuple2 = matrix2[iterator2]
                sum_tuple = (tuple1[0], tuple1[1], tuple1[2], tuple1[3] + tuple2[3])

                # adding the tuple in the sum list
                sum_of_matrices.append(sum_tuple)
                break

        # we do not have a non null value in the second matrix
        # so we just add this one in the sum list
        if flag == 0:
            sum_of_matrices.append(tuple1)

    # finally, we search for tuples from the second matrix that are not in the first one and add them
    for iterator in range(0, len(matrix2), 1):

        tuple2 = matrix2[iterator]

        # there is a null value in this position (in matrix 2)
        if (tuple2[0], tuple2[1], tuple2[2],) not in matrix1:
            sum_of_matrices.append(tuple2)

    # we return the list containing the sum matrix tuples
    return sum_of_matrices


# we will get two lists of elements, namely the tuples of matrix1 and those of matrix2
# we will calculate the difference of the two matrices
def matrix_difference(matrix1, matrix2):
    difference_of_matrices = []

    # we consider that the two matrices have the same dimension so we iterate trough their tuples and add values

    # if a non null element is neither in matrix1, nor in matrix2, we do not save it in a tuple
    # if a non null element is in matrix1 but not in matrix2 -> we save his value
    # if a non null element is in matrix2 but not in matrix1 -> we save his value * (-1)
    # if a non null element is in both matrices, we save the value of the difference

    # we check elements from both matrices and elements that are just in first matrix
    for iterator1 in range(0, len(matrix1), 1):

        tuple1 = matrix1[iterator1]
        flag = 0

        # we search for non null elements in matrix2 that are in matrix1 too
        for iterator2 in range(0, len(matrix2), 1):
            if tuple1[0] == matrix2[iterator2][0] and tuple1[1] == matrix2[iterator2][1] \
                    and tuple1[2] == matrix2[iterator2][2]:
                flag = 1
                tuple2 = matrix2[iterator2]
                difference_tuple = (tuple1[0], tuple1[1], tuple1[2], tuple1[3] - tuple2[3])

                # adding the tuple in the difference list
                difference_of_matrices.append(difference_tuple)
                break

        # we do not have a non null value in the second matrix
        # so we just add this one in the difference list
        if flag == 0:
            difference_of_matrices.append(tuple1)

    # finally, we search for tuples from the second matrix that are not in the first one and add them
    # since they are in the second matrix, the values will be multiplied with -1 before saving them
    for iterator in range(0, len(matrix2), 1):

        tuple2 = matrix2[iterator]

        # there is a null value in this position (in matrix 2)
        if (tuple2[0], tuple2[1], tuple2[2],) not in matrix1:
            negative_tuple = (tuple2[0], tuple2[1], tuple2[2], tuple2[3] * (-1))
            difference_of_matrices.append(negative_tuple)

    # we return the list containing the difference matrix tuples
    return difference_of_matrices


# we will create a null matrix
# we have 3 arguments: the number of rows, the number of culomns and the number of pages
def null_matrix(rows, columns, pages):
    # our way of thinking assumes that only non null valued elements will be saved into tuples
    # so here we must force the creation of a matrix with a given dimension by inserting tuples with 0 value
    # if we would return an empty list, the print_matrix function would print nothing
    # the whole print process is linked with the idea of tuples in this program

    # so we create fictive tuples that actually contain a value of 0
    # the key idea is to force the print_matrix function to print the whole matrix, even though it contains only 0
    # we do so by providing a tuple of form (rows - 1, columns - 1, pages - 1, 0)

    null_matrix_list = [(rows - 1, columns - 1, pages - 1, 0)]
    return null_matrix_list


# for the identity matrix we have a cube form because rows = columns = pages = size
# an identity matrix will have values of 1 on the main diagonal and 0 elsewhere
def identity_matrix(size):
    # we will save here our tuples
    identity_matrix = []

    for iterator in range(0, size, 1):
        # we put 1 in positions like : (0,0,0, ), (1,1,1, ) .... (k,k,k, )
        my_tuple = (iterator, iterator, iterator, 1)
        identity_matrix.append(my_tuple)

    return identity_matrix


# we will transpose a 3D matrix with tuples of form (i, j, k, v)
# in order to make this simple, we will go from (i, j, k , ) to (j, k, i, )
def matrix_transpose(list_of_elements):
    # we iterate trough the tuples and in a new list we save the elements of the transposed matrix
    transposed_matrix = []

    for iterator in range(0, len(list_of_elements), 1):
        my_tuple = (list_of_elements[iterator][1], list_of_elements[iterator][2], list_of_elements[iterator][0],
                    list_of_elements[iterator][3])

        transposed_matrix.append(my_tuple)

    return transposed_matrix


# we get two arguments, a list of tuples matrix1 and a list of tuples matrix2
# we calculate their product
# we must have matrices of form M1(i,j,k), M2(k, m, n)
# the result will be of form R(i, j, m, n)
# so we will get result_list[i][j][m][n] = value
# we do not use tuples here because the algorithm is similar with that for 2D matrix so we will have intermediary sums
# tuples are immutable, we cannot change a value in them, so we choose lists
def matrix_multiplication(matrix1, matrix2):
    # we save the size of the two matrices (i, j, k) and (k, m, n)
    matrix1_size = get_matrix_size(matrix1)
    i = matrix1_size[0]
    j = matrix1_size[1]
    k = matrix1_size[2]

    matrix2_size = get_matrix_size(matrix2)
    m = matrix2_size[1]
    n = matrix2_size[2]

    # here we will have the resulting matrix result[a][b][c][d] = value
    # where a in range(i), b in range(j), c in range(m), d in range(n)
    result = [[[[0 for d in range(n)] for c in range(m)] for b in range(j)] for a in range(i)]

    value1 = 0
    value2 = 0

    # we apply the formula
    for a in range(i):
        for b in range(j):
            for c in range(m):
                for d in range(n):
                    for e in range(k):

                        # we search for a tuple in matrix1 of form (a, b, c, )
                        for iterator1 in range(0, len(matrix1), 1):
                            # there is a non null value there
                            if matrix1[iterator1][0] == a and matrix1[iterator1][1] == b and matrix1[iterator1][2] == e:
                                value1 = matrix1[iterator1][3]
                                break
                            else:
                                value1 = 0

                        # we search for a tuple in matrix2 of form (e, c, d, )
                        for iterator2 in range(0, len(matrix2), 1):
                            # there is a non null value there
                            if matrix2[iterator2][0] == e and matrix2[iterator2][1] == c and matrix2[iterator2][2] == d:
                                value2 = matrix2[iterator2][3]
                                break
                            else:
                                value2 = 0

                        # result[a][b][c][d] = result[a][b][c][d] + matrix1(a, b, c, ) * matrix2(e, c, d, )
                        result[a][b][c][d] = result[a][b][c][d] + value1 * value2

    # now we convert data from result into a list of tuples in order to show a final result
    new_result = []

    for a in range(i):
        for b in range(j):
            for c in range(m):
                for d in range(n):
                    # we save only tuples for positions in which we have a non null element
                    if result[a][b][c][d] != 0:
                        auxiliary_tuple = (a, b, c, d, result[a][b][c][d])
                        # adding the tuple to the list
                        new_result.append(auxiliary_tuple)

    return new_result