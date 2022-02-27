def lightningbolt(left,right,end,s) :
  for _ in range(s+1):
    if s == 0 :
      print(end)
    else :
      print(left + " " * s + right)
      s -= 1
mad = lightningbolt("divine","man","mad",10)
