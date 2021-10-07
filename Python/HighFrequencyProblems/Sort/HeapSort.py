def heapAdjust(nums, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and nums[i] < nums[left]:
        largest = left
    if right < n and nums[largest] < nums[right]:
        largest = right
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapAdjust(nums, n, largest)

def heapSort(nums):
    n = len(nums)
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapAdjust(nums, n, i)
    # Swap from end to start
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapAdjust(nums, i, 0)

nums = [12, 11, 13, 5, 6, 7]
heapSort(nums)
print(nums)