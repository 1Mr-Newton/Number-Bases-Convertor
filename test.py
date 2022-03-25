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
      answer1 += (int(jj) * (16**(int(new_num.index(jj)))))
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

aa= base10toHex(165)
print(aa)