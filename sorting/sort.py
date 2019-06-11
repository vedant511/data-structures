class Sort(object):
    def __init__(self):
        pass

    def bubble_sort(self, lst):
        if len(lst) <= 1:
            return lst
        for i in range(len(lst)-1):
            j, k = 0, 1
            swapped = False
            while j < len(lst)-i-1:
                if lst[j] < lst[k]:
                    j += 1
                    k += 1
                else:
                    lst[j], lst[k] = lst[k], lst[j]
                    swapped = True
                    j += 1
                    k += 1
            if not swapped:
                return lst
        return lst

    def selection_sort(self, lst):
        if len(lst) <= 1:
            return lst
        for i in range(len(lst)-1):
            max_idx = 0
            j = 0
            while j < len(lst)-i:
                if lst[j] > lst[max_idx]:
                    max_idx = j
                lst[max_idx], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[max_idx]
                j += 1
        return lst

    def insertion_sort(self, lst):
        if len(lst) <= 1:
            return lst
        for i in range(1, len(lst)):
            current = i
            value = lst[i]
            while current > 0 and lst[current-1] > value:
                lst[current] = lst[current-1]
                current -= 1
            lst[current] = value
        return lst

    def merge_sort(self, lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left_lst = self.merge_sort(lst[:mid])
        right_lst = self.merge_sort(lst[mid:])
        return self.__merge(left_lst, right_lst)

    def __merge(self, lst1, lst2):
        i = 0
        j = 0
        new_lst = []
        while i < len(lst1) and j < len(lst2):
            if lst1[i] < lst2[j]:
                new_lst.append(lst1[i])
                i += 1
            else:
                new_lst.append(lst2[j])
                j += 1
        while i < len(lst1):
            new_lst.append(lst1[i])
            i += 1
        while j < len(lst2):
            new_lst.append(lst2[j])
            j += 1
        return new_lst

    def quick_sort(self, lst):
        return self.__quick_sort_helper(lst, 0, len(lst)-1)

    def __quick_sort_helper(self, lst, left, right):
        if left < right:
            split = self.__partition(lst, left, right)
            self.__quick_sort_helper(lst, left, split-1)
            self.__quick_sort_helper(lst, split+1, right)
        return lst

    def __partition(self, lst, start, end):
        pivot = lst[start]
        left_ptr = start + 1
        right_ptr = end
        done = False
        while not done:
            while left_ptr <= right_ptr and lst[left_ptr] <= pivot:
                left_ptr += 1
            while right_ptr >= left_ptr and lst[right_ptr] >= pivot:
                right_ptr -= 1
            if right_ptr < left_ptr:
                done = True
            else:
                lst[left_ptr], lst[right_ptr] = lst[right_ptr], lst[left_ptr]
        lst[start], lst[right_ptr] = lst[right_ptr], lst[start]
        return right_ptr
