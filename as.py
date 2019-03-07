n = int(input())
li = list(map(int, input().split()))
li.sort(reverse = True)
li2 = []
j = len(li) - 1
for i in range(len(li)):
  if i > j:
    break
  if i == j:
  	li2.append(li[i])
  	break
  li2.append(li[i])
  li2.append(li[j])
  j -= 1
for x in li2:
  print(x, end = " ")
