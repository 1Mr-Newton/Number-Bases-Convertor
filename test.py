#  This is Newton
# In this video I'm going to show you how to you how to write an advanced python number bases convertor using no third party libraries.
# # Let's start...

# print("Welcome to Newton's Number Bases convertor")

# # Let's write some functions to take the number and convert is to base 10

# def convert2base10(number, current_num_base):
#   '''
#   This function takes any number from any base and convert it to base 10
#   # '''

#   # ind = -1
#   # for n in str(number):



def calculator(base, number):
  answer = ""
  # number = 20
  while number > 0:
    k = number % base
    number = number // base
    answer += str(k)
  print(answer[::-1])


hex_alpha = 'ABCDEF'
hex_nums = ['10','11','12','13','14','15']
# answer = ""
# number  = 10861007
# while number > 0:
#   k = number % 16
#   number = number // 16
#   if str(k) in hex_nums:
#     k = hex_alpha[int(hex_nums.index(str(k)))]
#   answer += str(k)
# print(answer[::-1])

s = 'F5'
for l in s:
  if l in hex_alpha:
    k = int(hex_nums[int(hex_alpha.index(str(l)))])

print(k)

def fromHex2B10(number):
  hex_alpha = 'ABCDEF'
  hex_nums = ['10','11','12','13','14','15']
  for f in str(number):
    pass
  if int(f) >= 16:
    print(f"This is not a base {16} number!")
    print()
    return
  else:
    ind =- 1
    answer1 = 0
    
    for l in s:
      if l in hex_alpha:
        k = int(hex_nums[int(hex_alpha.index(str(l)))])
        number = (k*16)

    for n in str(number)[::-1]:
      ind += 1
      answer1 += int(n) * (16**int(ind))

    return answer1

aa = fromHex2B10('A5')
print(aa)