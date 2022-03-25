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
      answer1 += int(jj) * (2**(int(new_num.index(jj))))
    return answer1

aa = fromHex2B10('A5')
print(aa)


# a ='1D7F'
