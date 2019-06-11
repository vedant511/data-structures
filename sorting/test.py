from sorting.sort import Sort
from timeit import default_timer as timer

srt = Sort()
bubble_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 99, 11, 5, 0, -45, 11, 2, 18, 28, 100, 5]
selection_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 99, 11, 5, 0, -45, 11, 2, 18, 28, 100, 5]
insertion_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 99, 11, 5, 0, -45, 11, 2, 18, 28, 100, 5]
merge_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 99, 11, 5, 0, -45, 11, 2, 18, 28, 100, 5]
quick_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 99, 11, 5, 0, -45, 11, 2, 18, 28, 100, 5]
test_list_2 = [20]
test_list_3 = []
test_list_4 = [5, 2]
test_list_5 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print('==========BUBBLE SORT==========')
start = timer()
print(srt.bubble_sort(bubble_list))
print('Time taken = {}'.format(timer()-start))

print('\n==========SELECTION SORT==========')
start = timer()
print(srt.selection_sort(selection_list))
print('Time taken = {}'.format(timer()-start))

print('\n==========INSERTION SORT==========')
start = timer()
print(srt.insertion_sort(insertion_list))
print('Time taken = {}'.format(timer()-start))

print('\n==========MERGE SORT==========')
start = timer()
print(srt.merge_sort(merge_list))
print('Time taken = {}'.format(timer()-start))

print('\n==========QUICK SORT==========')
start = timer()
print(srt.quick_sort(quick_list))
print('Time taken = {}'.format(timer()-start))
