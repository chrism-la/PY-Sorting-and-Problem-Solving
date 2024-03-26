# Write your solution for algorithm 3 below
def sort_list(list):
  sorted_list = sorted(list, reverse=True)
  return sorted_list


arr = [5,3,4,2,1]

print("Reverse Order List:", sort_list(arr))
print("Original List:", arr)