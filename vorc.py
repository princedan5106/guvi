ch = input()
v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
c = [ chr(x) for x in range(65, 91)]
for x in c:
  c.append(x.lower())
for x in c:
  if x in v:
    c.remove(x)
if c in v:
  print("Vowel")
elif ch in :
  print("Consonant")
else:
  print("invalid")
