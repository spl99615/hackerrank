import sys
import os

def sort_quick(nums):
	if len(nums) == 1:
		return nums
	if nums == sorted(nums):
		return nums
	pivot = nums[len(nums)-1]
	leftpart,rightpart = partition(nums,pivot)
	return sort_quick(leftpart) + [pivot] + sort_quick(rightpart)

def partition(arr,pivot):
	left_part = []
	right_part = []

	for i in arr[:-1]:
		if i <= pivot:
			left_part.append(i)
		else:
			right_part.append(i)
	return (left_part,right_part)

if __name__ == '__main__':
	print(sort_quick([23,100,3,3,67,1,0,34,99,3]))