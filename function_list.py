#The global list variable
list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

#Grimes Golden functions list (GODS WHAT A MESS)

#This function double_index() will double the index of a given list
def double_index(lst, index):
  if index < len(lst):
    x = lst[index] * 2
    lst[index] = x
    print(lst)
  else:
    print(lst)

#This function remove_middle() will remove the start and ending index of a given list. 
def remove_middle(lst, start, end):
	if start < len(lst) and end < len(lst):
		del lst[start:(end + 1)]
		return lst
	else:
		return("You did not enter a valid index number")
		
#This function returns True if the 'item' repeats in the list more than 'n' times. 
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False
#Uncomment the line below when your function is done
#print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#This function returns item1 or item2 depending on which occurs more frequently. 
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2
#Uncomment the line below when your function is done
#print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#This little bastard almost killed me. This will return the middle number of an odd list. Or given an even length list, will return the average of the two middle numbers.
def middle_element(lst):
  odd = len(lst) // 2 
  even = odd - 1
  if len(lst) % 2 == 0:
    return (lst[odd] + lst[even]) / 2
  else:
    return lst[odd]
#Uncomment the line below when your function is done
#print(middle_element([5, 2, -10, -4, 4, 5]))

#The append_sum() function will add the last two items of the list together and append them to the end of the list. It will do this three times and then print the list. 
def append_sum(lst):
  if len(lst) >= 2:
	  for x in range(3):
		  add_last_two = lst[-1] + lst[-2]
		  lst.append(add_last_two)
	  return lst
  else:
	  return "List must have at least two items"
#print(append_sum([1, 1, 2]))

#Prints the Fibonnaci sequence up to whatever level is typed.
def fibonacci_seq(n):
	fib = [1,1]
	y = (n - 2)
	for x in range(y):
		sum = fib[-1] + fib[-2]
		fib.append(sum)
	return fib
#print(fibonacci_seq(10))  

#Runs the fibonacci sequence on an indefinite loop
def fibonacci_seq():
	fib = [1,1]
	while True == True:
		sum = fib[-1] + fib[-2]
		fib.append(sum)
		print(fib) 

#Combines two lists and sorts the results. 
def combine_sort(lst1, lst2):
  combine = lst1 + lst2
  sort = sorted(combine)
  return sort

#Function attempts to return a list from the starting number up to 100, stepping 3 each time. Current issue is getting it to inclusively end at 100. Input 99 outputs up to 102.
def every_three_nums(start):
    lst = list(range(start,101, 3))
    return lst

#The function delete_starting_evens() will delete the first items that are even from every list. For example 8, 10, 11 would just return 11. 
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst
 
#This function raised every base number to each exponent in powers.
 def exponents(bases, powers):
	return [b ** p for b in bases for p in powers]

#print(exponents([2, 3, 4], [1, 2, 3]))
#This function does the exact same thing, it just doesnt use list comprehension
def exponents_ver_2(bases, powers):
  empty_list = []
  for i in bases:
    for num in powers:
      number = i ** num
      empty_list.append(number)
  return empty_list
#print(exponents_ver_2([2, 3, 4], [1, 2, 3]))
