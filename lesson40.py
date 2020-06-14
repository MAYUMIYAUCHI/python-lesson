"""
count = 0
while count < 5:
  print(count)
  count += 1
else:
  print('done')
"""
count = 0
while count < 5:
  if count == 1:
    break
  print(count)
  count += 1
else:
  print('done')