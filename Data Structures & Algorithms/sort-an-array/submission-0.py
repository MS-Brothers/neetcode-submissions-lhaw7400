class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left, right):

            result = []

            i = 0
            j = 0

            # Compare both arrays
            while i < len(left) and j < len(right):

                if left[i] < right[j]:

                    result.append(left[i])
                    i += 1

                else:

                    result.append(right[j])
                    j += 1

            # Remaining elements
            result.extend(left[i:])
            result.extend(right[j:])

            return result


        def mergeSort(arr):

            # Base case
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            # Divide
            left = mergeSort(arr[:mid])

            right = mergeSort(arr[mid:])

            # Merge
            return merge(left, right)


        return mergeSort(nums)