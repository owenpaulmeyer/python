def substrings(string: str) -> list:
  return [string[i:j] for i in range(len(string)) for j in range(len(string)+1) if i < j]
