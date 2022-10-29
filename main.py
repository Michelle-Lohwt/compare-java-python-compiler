import timeit

def partition(array, low, high):
  global x
  # Choose the rightmost element as pivot
  pivot = array[high]

  # Position where partioned is done
  i = low - 1

  x = x + 4

  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      # Swapping element at i with element at j
      array[i], array[j] = array[j], array[i]
      x = x + 7
    x = x + 2

  # Swap pivot element with a greater element at position i
  array[i + 1], array[high] = array[high], array[i + 1]
  x = x + 7

  # Return the partitioned position
  return i + 1
  
# Quicksort
def quick_sort(array, low, high):
  global x
  if low < high:
    # Find a pivot element
    pi = partition(array, low, high)

    # Sort elements on the left of pivot
    quick_sort(array, low, pi - 1)

    # Sort elements on the right of pivot
    quick_sort(array, pi + 1, high)
    x = x + 7
  x = x + 1


# Load words
wordlist = []
with open('sgb-words.txt','r') as file:
  for line in file.readlines():
    word = line.replace('\n', '')
    wordlist.append(word)

# Variable for time complexity analysis
x = 0

# Sort words
a = timeit.default_timer()
quick_sort(wordlist, 0, len(wordlist) - 1)
x = x + 3
print(a)
# print(f'Sorted array: {wordlist}')
# print(f'Time complexity: {x}')
# print(f'Space complexity: {len(wordlist)}')