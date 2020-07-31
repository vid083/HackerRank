"""Task:
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
Input Format:
Read , the year to test.
Output Format:
The function must return a Boolean value (True/False). Output is handled by the provided code stub.
Sample Input 
1990
Sample Output 
False
Explanation 
1990 is not a multiple of 4 hence it's not a leap year."""

def is_leap(year):
    leap = False
    
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
    
    return leap

year = int(input())
print(is_leap(year))