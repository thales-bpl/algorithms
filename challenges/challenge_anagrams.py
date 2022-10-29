# def is_anagram(st_word, nd_word):
#     if (st_word == '' or nd_word == ''):
#         return False
#     for index, letter in enumerate(st_word):
#         if (nd_word[0] == letter):
#             print('letter', letter)
#             print('index', index)
#             print('1º palavra ANTES DO EDIT: ', st_word)
#             print('2º palavra ANTES DO EDIT: ', nd_word)
#             st_word = st_word.replace(st_word[index], '')
#             nd_word = nd_word.replace(nd_word[0], '')
#             print('1º palavra DEPOIS DO EDIT: ', st_word)
#             print('2º palavra DEPOIS DO EDIT: ', nd_word)
#             is_anagram(st_word, nd_word)
#     if (st_word == '' or nd_word == ''):
#         return True

def is_anagram(first_word, second_word): # complex: n
    first_word = first_word.lower()
    second_word = second_word.lower()

    if (first_word == '' or second_word == ''):  # complex: 1
        return False

    repeated_letter_index = second_word.find(first_word[0]) # complex: n
    if (repeated_letter_index == -1):
        return False

    first_word = first_word[1:] # complex: 1
    second_word = second_word[:repeated_letter_index] + second_word[repeated_letter_index + 1:] # complex: 1

    if (first_word == '' and second_word == ''): # complex: 1
        return True

    return is_anagram(first_word, second_word)