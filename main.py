# big_matrix = [
#     ["T", "H", "I", "S"],
#     ["C", "O", "D", "E"],
#     ["W", "O", "R", "K"],
#     ["G", "O", "O", "D"]
# ]

# small_matrix = [
#     ["D", "O", "O", "G"],
#     ["K", "R", "O", "W"],
#     ["E", "D", "O", "C"],
#     ["S", "I", "H", "T"]
# ]

# def check_sub_matrix():
#     small_matrix_len = len(small_matrix)

#     count = 0

#     for j in range(len(big_matrix) - 1):
#         for i in range(len(big_matrix) - 1):
#             big_matrix_subset = [mat[i:i + small_matrix_len] for mat in big_matrix[j:j + small_matrix_len]]
            
#             if(big_matrix_subset == small_matrix): count += 1

#     return count


# def reverse(list):
#     list_len = len(list)

#     for start in range(list_len // 2):
#         end = list_len - start - 1

#         list[start], list[end] = list[end], list[start]

#     return list

# print(reverse([1, 2, 3, 4]))


# def rotate90(mat):
#     n = len(mat)
    
#     for row in mat:
#         row.reverse()

#     for i in range(n):
#         for j in range(i + 1, n):
#             mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

#     return mat

# # Driver code
# mat = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]

# rotate90(rotate90(rotate90(rotate90(mat))))

# # Print the rotated matrix
# # for row in mat:
# #     print(" ".join(map(str, row)))


# # print(check_sub_matrix())

# with open("input.txt") as f:
#     list_index = 0
#     contents = f.read().split()
#     while True:
#         # read in big_size, small_size as ints
#         # read in big_matrix as 2D list of chars
#         # read in small_matrix as 2D list of chars

#         big_size, small_size = int(contents[list_index]), int(contents[list_index + 1])
        
#         if(big_size == small_size == 0):
#             break
        
#         big_matrix = [list(string) for string in contents[list_index + 2:list_index + 2 + big_size]]
#         small_matrix = [list(string) for string in contents[list_index + 2 + big_size:list_index + 2 + big_size + small_size]]

#         print(small_matrix)

#         list_index += small_size + big_size + 2

#         # counts = check_sub_matrix(big_matrix, small_matrix)
#         # print(counts)

# print(list(reversed([
#         ['A', 'B', 'C'],
#         ['D', 'E', 'F'],
#         ['G', 'H', 'I']
#     ])))

def reverse_matrix_rows(matrix, in_place = False):
    rev_matrix = []
    size = len(matrix)

    for start in range(size // 2):
        end = size - start - 1

        matrix[start], matrix[end] = matrix[end], matrix[start]

    if(in_place):
        rev_matrix = matrix
    else:
        rev_matrix = [row[:] for row in matrix]

    return rev_matrix

# print(   
#     reverse_matrix_rows([
#         ['A', 'B', 'C'],
#         ['D', 'E', 'F'],
#         ['G', 'H', 'I']
#     ])

#     ==

#     list(reversed([
#         ['A', 'B', 'C'],
#         ['D', 'E', 'F'],
#         ['G', 'H', 'I']
#     ]))
# )

test_matrix = [
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I']
    ]

rev_matrix = reverse_matrix_rows(test_matrix, in_place=False)
print(rev_matrix, list(reversed(test_matrix)))
# assert rev_matrix == list(reversed(test_matrix)), "reverse_matrix_rows not working as intended when in_place == False"
