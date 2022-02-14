#Given an array, find the maximum sum of any contiguous sub array
# Input: [34, -50, 42, 14, -5, 86]
# Output: 137

def sub_array(arr):
  max_end = max_seen = 0

  for i in arr:
    max_end = max(i, max_end + i)
    max_seen = max(max_seen, max_end)

  return max_seen


arr = [34, -50, 42, 14, -5, 86]
res = sub_array(arr)
print(res)