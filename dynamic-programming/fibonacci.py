memo = {}

def fibonacci(num):
  answer = None
  # Write your code here
  if num in memo:
    answer = memo[num]
  elif num == 0 or num == 1:
    answer = num
  else:
    answer = fibonacci(num - 1) + fibonacci(num - 2)
    memo[num] = answer
  return answer

# Test your code with calls here:
print(fibonacci(20))
print(fibonacci(200))
