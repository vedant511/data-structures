from sorting.sort import Sort
from timeit import default_timer as timer

srt = Sort()
test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
test_list_2 = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]

print('==========BUBBLE SORT==========')
start = timer()
print(srt.bubble_sort(test_list))
print('Time taken = {}'.format(timer()-start))

print('\n==========SELECTION SORT==========')
start = timer()
print(srt.selection_sort(test_list))
print('Time taken = {}'.format(timer()-start))
