def substrings(string: str) -> list:
  return [string[i:j] for i in range(len(string)) for j in range(len(string)+1) if i < j]

def substrings2(st):
    s = 0
    e = 1
    strings = []
    while s < len(st):
        if e == len(st)+1:
            s += 1
            e = s + 1
        strings.append(st[s:e])
        e += 1
    return strings

def transpose(mx: list) -> list:
  size = len(mx[0])
  return [[row[i] for row in mx] for i in range(size)]

def merge_lists(a_list, b_list):
    a_idx = 0
    b_idx = 0
    result = []
    while True:
        if a_idx == len(a_list):
            result += b_list[b_idx:]
            break
        if b_idx == len(b_list):
            result += a_list[a_idx:]
            break
        a_elem = a_list[a_idx]
        b_elem = b_list[b_idx]
        if a_elem < b_elem:
            result.append(a_elem)
            a_idx += 1
        else:
            result.append(b_elem)
            b_idx += 1
    return result
  
def maxSubArray(nums):
      ms = [0] * (len(nums))
      ms[0] = nums[0]
      for i in range(1,len(nums)):
          ms[i] = max(ms[i-1] + nums[i], nums[i])
      return max(ms)
def maxSubArray2(nums):
      mx = nums[0]
      prev = nums[0]
      for i in range(1,len(nums)):
          current = max(prev + nums[i], nums[i])
          mx = max(current, mx)
          prev = current
      return mx  

def binary(arr, v):
    start = 0
    end = len(arr) - 1
    idx = 0
  
    while start <= end: 
        idx = (end + start) // 2
        if arr[idx] < v: 
            start = idx + 1
        elif arr[idx] > v: 
            end = idx - 1
        else: 
            return idx
