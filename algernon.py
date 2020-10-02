def substrings(string: str) -> list:
  return [string[i:j] for i in range(len(string)) for j in range(len(string)+1) if i < j]


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
