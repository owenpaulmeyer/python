def substrings(string: str) -> list:
  return [string[i:j] for i in range(len(string)) for j in range(len(string)+1) if i < j]


def transpose(mx: list) -> list:
  size = len(mx[0])
  return [[row[i] for row in mx] for i in range(size)]
