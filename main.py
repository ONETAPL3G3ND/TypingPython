from typing import List
def my_function(numbers: List[int]) -> int:
	total = 0
	for number in numbers:
		total += number
	return total

if __name__ == "__main__":
	print(my_function([0,1,2,6,8,9]))