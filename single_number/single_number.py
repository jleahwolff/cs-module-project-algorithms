'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    #create a new array for the list to live in
    numbers = []
    # loop thru array
    for num in arr:
        #put the numbers into the new array
        if num not in numbers:
            numbers.append(num)
            #remove the number if its aready in the array
        elif num in numbers:
            numbers.remove(num)
    #return the first number in the new array
    return numbers[0]




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")