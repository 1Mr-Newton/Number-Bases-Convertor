def calculator(base, number):
  answer = ""
  # number = 20
  while number > 0:
    k = number % base
    number = number // base
    answer += str(k)
  print(answer[::-1])

calculator(8, 67)


def toBase10(from_base, number):
  for f in str(number):
    pass
  if int(f) >= from_base:
    print(f"This is not a base {from_base} number!")
    print()
    return
  ind =- 1
  answer1 = 0
  for n in str(number)[::-1]:
    ind += 1
    answer1 += int(n) * (from_base**int(ind))
  print(answer1)
  # return answer1

toBase10(8, 3137)