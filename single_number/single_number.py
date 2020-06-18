'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    #loop thru array
    for num in range(len(arr)):
        first_num = num
        second_num = num + 1
    #pick up one num
    #if current number == next number, 
        if first_num != second_num:
            return num
        else:
            single_number(arr)

    return single_number(arr)

    #restart the for loop

    #else, return the number
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")