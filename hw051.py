l = input("Give a single uppercase letter: ")
while len(l) != 1 or (("A" or "B" or "C") not in l):
    if len(l) != 1:
        print("Error: it needs to be a single character.")
        continue
    if l not in {"A", "B", "C"}:
        print("Error: You provided the wrong character.")
        continue
    l = input("Give a single uppercase letter: ")

if n.isdigit():
    n_int=int(n)
else:
    print("Error: your input should be only digits.")
while (not n.isdigit()) or n not in range(4):
    n_int=int(n)
    if n_int<1 or n_int>4:
        print("Error: a single digit needs to be in [1,3].")
    n = input("Give an single number character: ")
return n
