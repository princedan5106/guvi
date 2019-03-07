alp = [chr(x) for x in range(65, 91)]
for x in range(97, 123):
	alp.append(chr(x))
ch = input()
if ch in alp:
  print("Alphabet")
else:
  print("No")
