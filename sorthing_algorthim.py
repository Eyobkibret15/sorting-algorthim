import time
import random

array_size = int(input("enter the size of an array:  "))
array_range = int(input("enter the range of random number : "))


def random_array_generator(array_range, array_size):  # generating random generated_array
    array = [random.randint(1, array_range) for i in range(array_size)]
    return array


generated_array = random_array_generator(array_range, array_size)  # store random generated_array

# for random array coping random generated_array and copy for each of them
random_array = generated_array[:]
selection_random_array = random_array[:]
merge_random_array = random_array[:]
radix_random_array = random_array[:]

# for descending order  coping random generated_array
ascending_array = generated_array[:]
ascending_array.sort()  # sort the array in ascending order and copy for each of them
selection_ascending_array = ascending_array[:]
merge_ascending_array = ascending_array[:]
radix_ascending_array = ascending_array[:]

# for descending order coping random generated_array
descending_array = generated_array[:]
descending_array.sort(reverse=True) # sort the array in descending order and copy for each of them
selection_descending_array = descending_array[:]
merge_descending_array = descending_array[:]
radix_descending_array = descending_array[:]

# for A shape array coping random generated_array
a1_array = ascending_array[:len(ascending_array) // 2]
a2_array = ascending_array[len(ascending_array) // 2:]
a2_array.sort(reverse=True)
A_shape_array = a1_array + a2_array  # arrange the array with A shape and copy for each of them
selection_A_shape_array = A_shape_array[:]
merge_A_shape_array = A_shape_array[:]
radix_A_shape_array = A_shape_array[:]

# for V shape array coping random generated_array
v1_array = ascending_array[:len(ascending_array) // 2]
v2_array = ascending_array[len(ascending_array) // 2:]
v1_array.sort(reverse=True)
v2_array.sort()
v_shape_array = v1_array + v2_array   # arrange the array with V shape and copy for each of them
selection_v_shape_array = v_shape_array[:]
merge_v_shape_array = v_shape_array[:]
radix_v_shape_array = v_shape_array[:]


def selection_sort(selection_array):
    for i in range(len(selection_array) - 1):
        minimum_index = i
        for j in range(i + 1, len(selection_array)):
            if selection_array[j] < selection_array[minimum_index]:
                minimum_index = j
        selection_array[i], selection_array[minimum_index] = selection_array[minimum_index], selection_array[i]
    return selection_array


def merge_sort(merge_array):
    if len(merge_array) > 1:
        mid = len(merge_array) // 2
        left = merge_array[:mid]  # Dividing the generated_array elements 
        right = merge_array[mid:]

        merge_sort(left)  # Sorting the left half
        merge_sort(right)  # Sorting the right half

        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merge_array[k] = left[i]
                i += 1
            else:
                merge_array[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            merge_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            merge_array[k] = right[j]
            j += 1
            k += 1
    return merge_array


def counting_sort(radix_array, d):
    length_array = len(radix_array)
    count_array = [0] * 10  # initialize count generated_array
    # crate generated_array with the array_range of generated_array array_range that will have sorted generated_array
    output_array = [0] * length_array

    for i in range(length_array):  # Store occurrences in count generated_array
        ind = (radix_array[i] // d)
        count_array[ind % 10] += 1

    for i in range(1, 10):  # count_array[i] contains the true position in output generated_array
        count_array[i] += count_array[i - 1]

    i = length_array - 1
    while i >= 0:  # construct the output generated_array
        ind = (radix_array[i] // d)
        output_array[count_array[ind % 10] - 1] = radix_array[i]
        count_array[ind % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(radix_array)):
        # Copying the output generated_array to  generated_array  now generated_array is sorted
        radix_array[i] = output_array[i]


def radix_sort(radix_array):
    max1 = max(radix_array)
    d = 1
    while max1 / d > 0:
        counting_sort(radix_array, d)  # Do counting sort for every digit
        d *= 10
    return radix_array


# selection_sort
print("--------selection_sort----------")
start1 = time.time()
selection_sort(selection_random_array)
end1 = time.time()
print(f"random array: {(end1 - start1)*1000}")

start2 = time.time()
selection_sort(selection_ascending_array)
end2 = time.time()
print(f"ascending order array: {(end2 - start2)*1000}")

start3 = time.time()
selection_sort(selection_descending_array)
end3 = time.time()
print(f"descending order array: {(end3 - start3)*1000}")

start4 = time.time()
selection_sort(selection_A_shape_array)
end4 = time.time()
print(f"A shape array: {(end4 - start4)*1000}")

start5 = time.time()
selection_sort(selection_v_shape_array)
end5 = time.time()
print(f"V shape array: {(end5 - start5)*1000}")

# # merge_sort
# print("---------merge_sort---------")
# start6 = time.time()
# merge_sort(merge_random_array)
# end6 = time.time()
# print(f"random array: {end6 - start6}")
#
# start7 = time.time()
# merge_sort(merge_ascending_array)
# end7 = time.time()
# print(f"ascending array: {end7 - start7}")
#
# start8 = time.time()
# merge_sort(merge_descending_array)
# end8 = time.time()
# print(f"descending array: {end8 - start8}")
#
# start9 = time.time()
# merge_sort(merge_A_shape_array)
# end9 = time.time()
# print(f"A shape array: {end9 - start9}")
#
# start10 = time.time()
# merge_sort(merge_v_shape_array)
# end10 = time.time()
# print(f"V shape array: {end10 - start10}")
#
# # # radix_sort
# print("--------radix sort---------")
# start11 = time.time()
# radix_sort(radix_random_array)
# end11 = time.time()
# print(f"random array: {(end11 - start11)*1000}")
#
# start12 = time.time()
# radix_sort(radix_ascending_array)
# end12 = time.time()
# print(f"ascending array: {(end12 - start12)*1000}")
#
# start13 = time.time()
# radix_sort(radix_descending_array)
# end13 = time.time()
# print(f"descending array: {(end13 - start13)*1000}")
#
# start14 = time.time()
# radix_sort(radix_A_shape_array)
# end14 = time.time()
# print(f"A shape array: {(end14 - start14)*1000}")
#
# start15 = time.time()
# radix_sort(radix_v_shape_array)
# end15 = time.time()
# print(f"V shape array: {(end15 - start15)*1000}")

# print("--------end-------")
