class Sort(object):
    def __init__(self):
        pass

    def bubble_sort(self, lst):
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
        for i in range(len(lst)-1):
            max_idx = 0
            j = 0
            while j < len(lst)-i:
                if lst[j] > lst[max_idx]:
                    max_idx = j
                lst[max_idx], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[max_idx]
                j += 1
        return lst

    def insertion_sort(self):
        pass

    def shell_sort(self):
        pass

    def quick_sort(self):
        pass

    def merge_sort(self):
        pass

    def merge(self):
        pass
