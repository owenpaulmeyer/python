def substrings(s: str) -> list:
  idxs = [[x,y] for x in range(6) for y in range(len(s) + 1) if x < y]
  subs = []
  for i in idxs:
    subs.append(string[i[0]:i[1]])
  return subs
