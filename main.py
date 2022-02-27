def lightningbolt(left,right,end,s) :
  x = 0
  for _ in range(s+1):
    if s == 0 :
      print(end)
    else :
      x = len(left + " " * s + right) + x
      print(left + " " * s + right)
      s -= 1
mad = lightningbolt("divine","man","mad",10)
