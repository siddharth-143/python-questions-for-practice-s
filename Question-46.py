"""
Question 45 :
    Write a program which can filter even numbers in a
    list by using filter function. The list is :
    [1,2,3,4,5,6,7,8,9,10].

    Hints : Use map() to filter some elements in a list.
    Use lambda to define anonymous functions.
"""

# Solution :

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = map(lambda x: x % 2 == 0, li)
print(list(even_num))

"""
Output : 
    [False, True, False, True, False, True, False, True, False, True]
    
    Process finished with exit code 0
"""