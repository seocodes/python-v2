import random
nums = (random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),
        random.randint(0,50))

print(f'Números gerados:\n')
for i in range (len(nums)):
    print(nums[i])
print(f'Maior número: {max(nums)}')
print(f'Menor número: {min(nums)}')