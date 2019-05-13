class Search(object):
    def __init__(self, lst):
        self.lst = lst

    def binary(self, item):
        left = 0
        right = len(self.lst) - 1
        return self.__helper(item, left, right)

    def __helper(self, item, left, right):
        if left > right:
            return False
        mid = (left + right) // 2
        if self.lst[mid] == item:
            return True, mid
        elif item < self.lst[mid]:
            return self.__helper(item, left, mid-1)
        else:
            return self.__helper(item, mid+1, right)

    def linear1(self, item):
        for i in range(len(self.lst)):
            if self.lst[i] == item:
                return True, i
        return False

    def linear2(self, item):
        left = 0
        right = len(self.lst) - 1
        while left < right:
            if self.lst[left] == item:
                return True, left
            elif self.lst[right] == item:
                return True, right
            else:
                left += 1
                right -= 1
        return False
