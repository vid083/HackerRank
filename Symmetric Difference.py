"""
Task:
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

Input Format:
The first line of input contains an integer, . 
The second line contains  space-separated integers. 
The third line contains an integer, . 
The fourth line contains  space-separated integers.

Output Format:
Output the symmetric difference integers in ascending order, one per line.

Sample Input:
4
2 4 5 9
4
2 4 11 12

Sample Output:
5
9
11
12
"""

a,b=(int(input()),input().split())
c,d=(int(input()),input().split())
x=set(b)
y=set(d)
p=y.difference(x)
q=x.difference(y)
r=p.union(q)
print ('\n'.join(sorted(r, key=int)))