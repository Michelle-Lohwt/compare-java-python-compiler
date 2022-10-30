import timeit

def partition(array, low, high):
  # Choose the rightmost element as pivot
  pivot = array[high]

  # Position where partioned is done
  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      # Swapping element at i with element at j
      array[i], array[j] = array[j], array[i]

  # Swap pivot element with a greater element at position i
  array[i + 1], array[high] = array[high], array[i + 1]

  # Return the partitioned position
  return i + 1
  
# Quicksort
def quick_sort(array, low, high):
  if low < high:
    # Find a pivot element
    pi = partition(array, low, high)

    # Sort elements on the left of pivot
    quick_sort(array, low, pi - 1)

    # Sort elements on the right of pivot
    quick_sort(array, pi + 1, high)

# Load words
wordlist = []
with open('sgb-words.txt','r') as file:
  for line in file.readlines():
    word = line.replace('\n', '')
    wordlist.append(word)

# Sort words
a = timeit.default_timer()
quick_sort(wordlist, 0, len(wordlist) - 1)

# print(f'Sorted array: {wordlist}')
# print(f'Time complexity: {a}')
# print(f'Space complexity: {len(wordlist)}')