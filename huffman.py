def inArray(arr, key):
  for i in range(len(arr)):
    if arr[i][0] in key:
      arr[i][1] += 1
  return arr

def createArr(arr):
  lisTemp = arr.copy()
  lis = list()
  for i in range(len(lisTemp)):
    lis.append([lisTemp[i][0], 0])
  return lis

def findMins(arr):
  lisTemp = arr.copy()
  a = lisTemp[0]
  for i in range(len(lisTemp)):
    if a[1] > lisTemp[i][1]:
      a = lisTemp[i]
  lisTemp.remove(a)
  b = lisTemp[0]
  for i in range(len(lisTemp)):
    if b[1] > lisTemp[i][1]:
      b = lisTemp[i]
  return [a,b]

# paso 1 leer input
txt = input()
txt2 = list(set(txt))
lis = list()
for i in range(len(txt2)):
  lis.append([txt2[i], txt.count(txt2[i])])
lisCount = createArr(lis.copy())
lis2 = lis.copy()

#paso 2: combinar parejas y determinar la profundidad
while(len(lis) > 1):
  mins = findMins(lis)
  node = [mins[0][0]+mins[1][0], mins[0][1]+mins[1][1]]
  lis.remove(mins[0])
  lis.remove(mins[1])
  lis.append(node)
  lisCount = inArray(lisCount, node[0])

# paso 3: Multiplicar y sumar
res = 0
for i in range(len(lisCount)):
  res += (lisCount[i][1]*lis2[i][1])
print((len(txt)*8)/res)