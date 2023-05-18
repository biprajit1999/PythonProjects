def find_number_of_superior_elements(arr, n):
    max_so_far = arr[n-1] # Initialize the maximum element encountered so far to the rightmost element
    count = 1 # Initialize the count to 1 for the rightmost element
    for i in range(n-2, -1, -1): # Traverse the array from right to left
        if arr[i] > max_so_far: # If the current element is greater than the maximum encountered so far
            max_so_far = arr[i] # Update the maximum encountered so far
            count += 1 # Increment the count of superior elements
    return count

# Driver code to test the function
n = int(input())
arr = list(map(int, input().split()))
print(find_number_of_superior_elements(arr, n))
