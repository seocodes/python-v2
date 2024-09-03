from functools import reduce
nums = [1,5,9,10,2]

notas = reduce(lambda x,y: x+y, nums)
media = notas/len(nums)
print(media)