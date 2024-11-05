def pretty_print(matrix):
    """
    pretty_print prints out 2D lists in an easier to read format than built-in print.
    :param matrix: A 2D list 
    :return: None
    :time complexity: Runs in O(n^2) time, where n is the number of rows or columns in matrix 
                        because esach element in each row of the matrix is printed once
    """
    for row in matrix:
        print(row)
    print()


def transpose_major(matrix, in_place = False):
    """
    transpose_major transposes a 2D lists accross the major diagonal. Can transpose either in-place or not
        depending on user-preference or project requirements
    :param matrix: A 2D list to be transposed
    :param in_place: determines whether matrix is transposed in-place or as a copy
    :return t_matrix: Either a reference to a 2D list (if transposed in-place) or a transposed copy of a 2D list
    :time complexity: O(n^2), as we have to effectively loop over both rows and columns of the matrix in a nested for loop.
                        We only need to loop over a corner of the matrix, however, not the whole thing.

    """
    size = len(matrix)
    t_matrix = []

    if in_place:
        for i in range(size - 1):
            for j in range(i + 1, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        t_matrix = matrix
    else:
        t_matrix = [[matrix[j][i] for j in range(size)] for i in range(size)]

    return t_matrix


def transpose_minor(matrix, in_place=False):
    """
    transpose_minor transposes a 2D lists accross the minor diagonal. Can transpose either in-place or not
        depending on user-preference or project requirements
    :param matrix: A 2D list to be transposed
    :param in_place: determines whether matrix is transposed in-place or as a copy
    :return t_matrix: Either a reference to a 2D list (if transposed in-place) or a transposed copy of a 2D list
    :time complexity: O(n^2), as we have to effectively loop over both rows and columns of the matrix in a nested for loop.

    """
    size = len(matrix)

    if in_place:
        for i in range(size):
            for j in range(size - i - 1):
                matrix[i][j], matrix[size - j - 1][size - i - 1] = matrix[size - j - 1][size - i - 1], matrix[i][j]\
                
        return matrix
    else:
        t_matrix = [[matrix[size - j - 1][size - i - 1] for j in range(size)] for i in range(size)]

        return t_matrix


def reverse_matrix_rows(matrix, in_place=False):
    """
    reverse_matrix_rows reverses the rows of the matrix. Can reverse either in-place or not
        depending on user-preference or project requirements
    :param matrix: A 2D list to be reversed
    :param in_place: determines whether matrix is reversed in-place or as a copy
    :return t_matrix: Either a reference to a 2D list (if reversed in-place) or a reversed copy of a 2D list
    :time complexity: O(n) as we're only iterating over the 2d array once. Either in place or not, we only have
                        to iterate over the outer list itself.

    """                 

    size = len(matrix)

    if in_place:
        for start in range(size // 2):
            end = size - start - 1
            matrix[start], matrix[end] = matrix[end], matrix[start]

        return matrix
    
    else:
        return [matrix[size - 1 - i] for i in range(size)]


def rotate(matrix):
    """
    rotate takes in a matrix and rotates it 90degrees counterclockwise.
    :param matrix: A 2D list to be reversed
    :returns the original array rotated, or a copy of the array depending on the constant size threshold set in the function
    :time complexity: O(n^2) at it's worse. It isn't super significant, but will require us to loop over the array one more time 
                    if we aren't returning the list in place, however this won't change the functions time complexity.

    """  

    # calculate size
    size = len(matrix)
    rotated_matrix = []

    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    if size >= 4: # I should be able to change this 4 to any value > 0
        rotated_matrix = matrix
    else:
        rotated_matrix = [[row for row in matrix] for _ in matrix]

    return rotated_matrix


def check_match(big_matrix, small_matrix, start_row, start_col):
    """
    check_match checks if the subset of a large matrix and a small matrix match.
    :param big_matrix: A 2D list to be checked for a sub matrix
    :param small_matrix: A 2d list to be checked as a sub matrix
    :returns a boolean, depending on whether the subsection and small_matrix match
    :time complexity: O(n^2), where n is the size of the small_matrix. This is because in our
                      list comprehension, we are effectively looping over the small_matrix twice with our slices.

    """  
    # returns True or False, depending on whether a match was found
    small_matrix_len = len(small_matrix)

    big_matrix_subset = [mat[start_row:start_row + small_matrix_len] for mat in big_matrix[start_col:start_col + small_matrix_len]]

    return big_matrix_subset == small_matrix


def count_appearances(big_matrix, small_matrix):
    """
    counts the number of times a sub matrix appears in a larger one
    :param big_matrix: A 2D list to be checked for a sub matrix
    :param small_matrix: A 2d list to be checked as a sub matrix
    :returns a list of matches based on the number of times small_matrix has been rotated
    :time complexity: O(n^2 * N^2), where n is the size of the small_matrix, and N is the size of
                      the large matrix. This is because we are looping over the large matrix within
                      a nested loop, and then calling the check_match, which does the same thing for
                      the smaller matrix

    """  
    counts = [0,0,0,0] # counts for 0, 90, 180, 270 degree rotations
    # YOUR CODE BELOW
    big_matrix_len = len(big_matrix)

    for k in range(4):
        for j in range(big_matrix_len - 1):
            for i in range(big_matrix_len - 1):
                if(check_match(big_matrix, small_matrix, i, j)): counts[k] += 1

        small_matrix = rotate(small_matrix)

    # YOUR CODE ENDS
    return counts


def main(file_path):
    with open(file_path) as f:
        list_index = 0
        contents = f.read().split() # Split simply makes it easier to read the file starting out
        while True:
            # read in big_size, small_size as ints
            # read in big_matrix as 2D list of chars
            # read in small_matrix as 2D list of chars

            big_size, small_size = int(contents[list_index]), int(contents[list_index + 1])
            
            if(big_size == small_size == 0):
                break
            
            big_matrix = [list(string) for string in contents[list_index + 2:list_index + 2 + big_size]]
            small_matrix = [list(string) for string in contents[list_index + 2 + big_size:list_index + 2 + big_size + small_size]]

            list_index += small_size + big_size + 2

            counts = count_appearances(big_matrix, small_matrix)
            print(counts)




# DRIVER CODE (DO NOT MODIFY)
file_path = 'input.txt'
main(file_path)


# EXAMPLE TEST CODE
def initialize_test_matrix():
    return [
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I']
    ]


def test_reverse_matrix_rows():
    original_matrix = initialize_test_matrix()
    test_matrix = initialize_test_matrix()
    
    rev_matrix = reverse_matrix_rows(test_matrix, in_place=False)
    assert rev_matrix == list(reversed(test_matrix)), "reverse_matrix_rows not working as intended when in_place == False"

    rev_matrix = reverse_matrix_rows(original_matrix, in_place=True)
    assert rev_matrix == original_matrix, "reverse_matrix_rows not working as intended when in_place == True"

    
def test_transpose(function, matrix, in_place):
    print(f"\n####### Testing {function.__name__}: in_place = {in_place} #######\n")

    if in_place == False:
        t_matrix = function(matrix, in_place)
        t_matrix[0][1] = 23
        pretty_print(t_matrix)
        assert t_matrix != matrix, "not working if in_place == False"

    else:
        t_matrix = function(matrix, in_place)
        t_matrix[0][1] = 23
        pretty_print(t_matrix)
        assert t_matrix == matrix, "not working if in_place == True"

test_reverse_matrix_rows()

test_matrix = initialize_test_matrix()
test_transpose(transpose_major, test_matrix, in_place=False)

test_matrix = initialize_test_matrix()
test_transpose(transpose_minor, test_matrix, in_place=False)

test_matrix = initialize_test_matrix()
test_transpose(transpose_major, test_matrix, in_place=True)

test_matrix = initialize_test_matrix()
test_transpose(transpose_minor, test_matrix, in_place=True)