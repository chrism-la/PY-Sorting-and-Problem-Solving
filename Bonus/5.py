# Write your solution for algorithm 5 below
arr = [5,10,4,7,6,2]


def two_sum(arr, target):
  arr.sort()
  left = 0
  right = len(arr) - 1

  while left < right:
    sum = arr[left] + arr[right]
    if sum == target:
      return [arr[left], arr[right]]
    elif sum < target:
      left +=1
    else:
      right -=1
  return "no sum"

print(two_sum(arr, 9))


