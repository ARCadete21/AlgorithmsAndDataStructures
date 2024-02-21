import random


# Makes intervals from inputs
def make_interval():
    initial_number = int(input("Interval's initial value (-999 to 999):\t"))
    while not (-1000 < initial_number < 1000):
        initial_number = int(input("That wasn't a valid answer. Insert a valid interval's initial value (-999 to 999):\t"))

    final_number = int(input(f"Interval's final value ({initial_number} to 999):\t"))
    while not (initial_number <= final_number < 1000):
        final_number = int(input(f"That wasn't a valid answer. Insert a valid interval's final value ({initial_number} to 999):\t"))

    user_interval = [number for number in range(initial_number, final_number + 1)]
    return user_interval


# check
def check():
    checking = input("Do you want to insert another interval? (Yes/No)\t")
    while not (checking.lower() == 'yes' or checking.lower() == 'no'):
        checking = input("That wasn't a valid answer. Do you want to insert another interval? (Yes/No)\t")

    return checking.lower()


# Sorting function
def merge(left_list, right_list):
    result = []
    i = j = 0

    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            j += 1

    result.extend(left_list[i:])
    result.extend(right_list[j:])
    return result


def merge_sort(list_to_sort):
    if len(list_to_sort) == 1:
        return list_to_sort

    middle = len(list_to_sort) // 2
    left = merge_sort(list_to_sort[:middle])
    right = merge_sort(list_to_sort[middle:])
    return merge(left, right)


# shuffle
def shuffle(list_to_shuffle):
    shuffled_list = []
    for i in range(len(list_to_shuffle)):
        chosen = random.choice(list_to_shuffle)
        shuffled_list.append(chosen)
        list_to_shuffle.remove(chosen)

    return shuffled_list


# elimination of repeated numbers
def repeated_numbers_elimination(new_interval, current_interval):
    new_list = new_interval + current_interval
    no_duplicates_list = []

    for element in new_list:
        if element not in new_interval or element not in current_interval:
            no_duplicates_list.append(element)

    return no_duplicates_list


# create a list from a matrix
def make_list_from_matrix(matrix):
    a = []
    for lst in matrix:
        list = a + lst
        a = list

    return list


# create a matrix from a list
def make_matrix_from_list(list):
    matrix = []
    a = []

    for index in range(len(list)-1):
        if list[index] == (list[index+1]-1):
            a.append(list[index])

            if index == (len(list)-2):
                a.append(list[index+1])
                matrix.append(a)

        elif index == (len(list)-2) and list[index] != (list[index+1]-1):
            a.append(list[index])
            matrix.append(a)
            matrix.append([list[index+1]])

        else:
            a.append(list[index])
            matrix.append(a)
            a = []

    return matrix


print('INSTRUCTIONS:'
      '\n\n1. This program will generate a list, which will consist in the\nunion of all the intervals eventually imputed by a user.'
      '\n\n2. If the user, at some point, inputs an interval containing values which \nalready belong to the list, these repeted values will be deleted.'
      '\n\n3. The minimum limit of the list will be -999 and the maximum limit 999.'
      '\n\n4. After the insertion of any interval, the user will be asked if they want to insert a new one.'
      '\n\nLETS BEGIN:')

main_interval = make_interval()
print(main_interval)
check_yes = check()

while check_yes == 'yes':
    small_interval = make_interval()
    main_interval = repeated_numbers_elimination(main_interval, small_interval)
    check_elements = False
    for element in main_interval:
        if element:
            check_elements = True
            break
    if check_elements:
        main_interval = merge_sort(main_interval)
        main_matrix = make_matrix_from_list(main_interval)
        for index in range(len(main_matrix)):
            if index % 2 != 0:
                main_matrix[index] = shuffle(main_matrix[index])
                main_interval = make_list_from_matrix(main_matrix)
    print(main_interval)
    check_yes = check()

print(f"\nYour final interval is:\n{main_interval}")