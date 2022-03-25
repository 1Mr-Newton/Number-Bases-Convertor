print("Welcome to the Newton's Number bases convertor")
print()
# import readch
def fromHex2B10(hex_number):
  new_num= []
  hex_alpha = 'ABCDEFG'
  hex_nums = ['10','11','12','13','14','15', '16']
  for num in str(hex_number):
    if num in hex_alpha:
      num = hex_nums[int(hex_alpha.index(str(num)))]
  if int(num) >= 16:
    return (f"This is not a base {16} number!")
  else:
    answer1 = 0
    for l in hex_number:
      if l in hex_alpha:
        k = int(hex_nums[int(hex_alpha.index(str(l)))])
        new_num.append(k)
      else:
        new_num.append(l)

    new_num.reverse() #
    for jj in new_num:
      answer1 += int(jj) * (16**(int(new_num.index(jj))))
    return answer1

def base10toHex(number):
  answer = ''
  hex_alpha = 'ABCDEFG'
  hex_nums = [10,11,12,13,14,15]

  while number > 0:
    k = number % 16
    number = number // 16
    if k in hex_nums:
      k =hex_alpha[hex_nums.index(k)]
      answer += str(k)
    else:
      answer += str(k)
  return answer[::-1]

def base10toANY(base, number):
  answer = ""
  while number > 0:
    k = number % base
    number = number // base
    answer += str(k)
  return answer[::-1]
  # print(answer[::-1])

# base10toANY(2, 15)


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

  return answer1
  # print(answer1)

# toBase10(2, 1111)

calculating = True
while calculating:
  # print(fromHex2B10('A5'))
  user_choice = input("Please choose one of the following services:\n1. From any base to any base(eg. from base 8 to base 2)\n2. From any base to base 10(eg. from base 8 to base 10)\nEnter your choice here: ")
  print()

  if user_choice == '1':
    from_base = int(input('Please enter the "from" base(eg. from base 2)\n'))
    number = int(input('Please enter the number you want to convert\n'))
    conv2base10 = toBase10(from_base, number)
    to_base = int(input('Please enter the "to" base(eg. to base 8)\n'))
    final_ans = base10toANY(to_base, conv2base10)
    print(final_ans)


  elif user_choice == '2':
    from_base = int(input('Please enter the "from" base(eg. from base 2)\n'))
    
    number = input('Please enter the number you want to convert\n')

    if from_base == 16:
      print(fromHex2B10(number))

    else:
      final_an = toBase10(from_base, number)
      print(final_an)

  print()

  calculate_again = input("Do you have more to calculate?\nPress 'y' to continue or anykey to quit:")
  if calculate_again == 'y':
    continue
  else:
    break