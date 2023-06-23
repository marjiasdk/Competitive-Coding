class Solution(object):
    def sortColors(self, nums):
        def findSmallest(arr):
            smallest = arr[0]
            smallest_index = 0
            for i in range(1, len(arr)):
                 if arr[i] < smallest:
                    smallest = arr[i]
                    smallest_index = i
            return smallest_index
        
        # we don't have a new list here because we are modifying the original list
        def selectionSort(arr):
            for i in range(len(arr)):
                # we use arr[i:] because we want to find the smallest element in the unsorted part of the list
                # we add i to the result because we want to get the index of the smallest element in the original list
                # example = [2, 0, 2, 1, 1, 0]
                # i = 0, arr[i:] = [2, 0, 2, 1, 1, 0], smallest = 0, smallest_index = 1
                # i = 1, arr[i:] = [0, 2, 1, 1, 0], smallest = 0, smallest_index = 0
                # i = 2, arr[i:] = [2, 1, 1, 0], smallest = 0, smallest_index = 3
                # i = 3, arr[i:] = [1, 1, 0], smallest = 0, smallest_index = 2
                # i = 4, arr[i:] = [1, 0], smallest = 0, smallest_index = 1
                # i = 5, arr[i:] = [0], smallest = 0, smallest_index = 0
                # arr = [0, 0, 1, 1, 2, 2]
                smallest = findSmallest(arr[i:]) + i
                # we swap the smallest element with the current element
                # example = [2, 0, 2, 1, 1, 0]
                # i = 0, smallest = 1, arr = [0, 2, 2, 1, 1, 0]
                # i = 1, smallest = 0, arr = [0, 2, 2, 1, 1, 0]
                # i = 2, smallest = 3, arr = [0, 0, 2, 1, 1, 2]
                # i = 3, smallest = 2, arr = [0, 0, 1, 2, 1, 2]
                # i = 4, smallest = 1, arr = [0, 0, 1, 1, 2, 2]
                # i = 5, smallest = 0, arr = [0, 0, 1, 1, 2, 2]
                # arr = [0, 0, 1, 1, 2, 2]
                arr[i], arr[smallest] = arr[smallest], arr[i]

        selectionSort(nums)
        return nums