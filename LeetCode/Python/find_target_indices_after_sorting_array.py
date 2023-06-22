class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        # we create a list for situations where there is more than one instance of the target
        result = []

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]

            if guess == target:
                result.append(mid)

                # search the left side of the array for the target
                # we do i = mid - 1 because we already found the target at mid, so we decrement to search the left of the array
                # example: [1, 2, 2, 3, 5]
                # the left side would be [1, 2, 2]
                i = mid - 1
                # while i is greater than or equal to low and the value at nums[i] is equal to the target
                while i >= low and nums[i] == target:
                    # append the index to the result list
                    result.append(i)
                    i -= 1

                # search the right side of the array for the target
                # example: [1, 2, 2, 3, 5]
                # the right side would be [2, 3, 5]
                i = mid + 1
                while i <= high and nums[i] == target:
                    result.append(i)
                    i += 1

                return sorted(result)
            
            # guess was too high
            # example: [1, 2, 2, 3, 5]
            # high originally was 4, but now it is 2 (high = len(nums) - 1, which is 4, but now, mid - 1 would be 2)
            if guess > target:
                high = mid - 1
            # guess was too low
            # low originally was 0, but now it is 2 (low = mid + 1, which is 0, but now, mid + 1 would be 2)
            else:
                low = mid + 1
            # after high and low get updated, we go back to the top of the while loop and check again

        return result # which would be [] if the target was not found