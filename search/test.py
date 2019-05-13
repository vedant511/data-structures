from search.Search import Search
import time
import timeit
from timeit import default_timer as timer

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
sch = Search(test_list)

print('=====Binary Search=====')
start = timer()
# print(sch.binary(13))
# print(sch.binary(0))
print(sch.binary(42))
# print(sch.binary(5))
print('Binary Search took {} sec'.format(timer()-start))

print('=====Linear Search 1=====')
start = timer()
# print(sch.linear1(13))
# print(sch.linear1(0))
print(sch.linear1(42))
# print(sch.binary(5))
print('Linear Search 1 took {} sec'.format(timer()-start))

print('=====Linear Search 2=====')
start = timer()
# print(sch.linear1(13))
# print(sch.linear1(0))
print(sch.linear1(42))
# print(sch.binary(5))
print('Linear Search 2 took {} sec'.format(timer()-start))
