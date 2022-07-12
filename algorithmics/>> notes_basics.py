#BASIC ALGORITHMS

#RECURSION------------------------------------------------------------------------|
#A programming method characterized by functions that, during their operation
#call additional copies of themselves. Recursion involves breaking down a problem
#into smaller instances recursively until each of them can be independently
#solved. Solutions to these smaller instances combine to form the solution for
#the original problem.

#recursion_example
def factorial(n):
     if n == 1:
          return 1
     else:
          return n * factorial(n-1)

#recursion_example
def fibonacci(n):
     if n == 1 or n == 2:
          return 1
     else:
          return fibonacci(n - 1) + fibonacci(n - 2)

#Head recursion occurs when the recursive call is near the beginning of the function,
#before other reasoning or code. Tail recursion occurs when the recursive call is
#closer to the end of the function, after some reasoning or code.
     
#tail_recursion_example
def count_down_1(start):
     if start <= 0:
         print(start)
     else:
         print(start)
         count_down_1(start - 1)

count_down_1(5)

#head_recursion_example
def count_down_2(start):
     if start <= 0:
         print(start)
     else:
         count_down_2(start - 1)
         print(start)
         
count_down_2(5)


#SORTING-ALGORITHMS---------------------------------------------------------------|
#Algorithms that take as input a list and produce as output a sorted version of
#that list. Examples include: bubble sort, insertion sort, merge sort, shell sort,
#quick sort and heap sort.

#bubble_sort_algorithm, O(n^2)
def sort_with_bubbles(lst):
    swap_occurred = True

    while swap_occurred:

        swap_occurred = False        

        for i in range(len(lst) - 1):

            if lst[i] > lst[i + 1]:                
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp

                swap_occurred = True

    return lst     

print(sort_with_bubbles([4, 3, 5, 2, 1]))
