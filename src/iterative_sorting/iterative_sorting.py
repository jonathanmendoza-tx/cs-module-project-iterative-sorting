def selection_sort(arr):
	for i in range(0, len(arr) - 1):

		cur_index = i
		smallest_index = cur_index

		while cur_index < len(arr):

			if arr[cur_index] < arr[smallest_index]:

				smallest_index = cur_index

			else:
				cur_index += 1

		if i is not smallest_index:

			prev_small = arr[i]
			new_small = arr[smallest_index]

			arr[i] = new_small

			arr[smallest_index] = prev_small
			
	return arr


def bubble_sort(arr):

	if len(arr) > 0:

		no_swap = False

		large_val = 0

		large_index = len(arr)-1

		while no_swap is False:

			swapped = False

			for i in range(large_index):

				if arr[i] > arr[i + 1]:

					if arr[i] > large_val:

						large_val = arr[i]

					smaller = arr[i+1]
					larger = arr[i]

					arr[i] = smaller
					arr[i+1] = larger

					swapped = True

			if arr[large_index] == large_val:

				large_val = 0
				large_index -= 1

			if swapped == False:

				no_swap = True

	return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):

	if len(arr) > 0:

		maximum = max(arr)

		storage = [0]*(maximum+1)

		for i in range(len(arr)):

			if arr[i] < 0:

				return 'Error, negative numbers not allowed in Count Sort'

			storage[arr[i]] += 1

		arr = []

		for j, k in enumerate(storage):

			if k > 0:
				arr.extend([j]*k)

	return arr