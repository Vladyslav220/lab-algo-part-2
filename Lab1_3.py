import unittest

def peek_seq(arr):
    max_length = 0
    for i in range(len(arr)):
        if i == 0 or i == len(arr) - 1:
            continue
        if arr[i - 1] < arr[i] > arr[i + 1]:
            left = i
            right = i
            while left > 0:
                if arr[left - 1] < arr[left]:
                    left -= 1
                else:
                    break
            while right < len(arr) - 1:
                if arr[right + 1] < arr[right]:
                    right += 1
                else:
                    break
            if right - left + 1 > max_length:
                max_length = right - left + 1
    return max_length

