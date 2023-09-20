# List or Arrays

#1.you have been givenpython python list [10,501,22,37,100,999,87,351] your task is to create a two list one which all have even numbers and another list which all have odd numbers in it

#solution:

given_list = [10,501,22,37,100,999,87,351]
odd_list = []
even_list = []
for tot_list in given_list:
    if tot_list % 2 == 0:
        even_list.append(tot_list)
    else:
        odd_list.append(tot_list)
print(f'Even numbers in a given_list are: {even_list}')
print(f'Odd numbers in a given_list are: {odd_list}')

#2.given python list [10,501,22,37,100,999,87,351] your task is to count all the prime numbers and create new python list which will contain all prime numbers in it
#solution:
given_list = [10,501,22,37,100,999,87,351]
prime_numbers_list = []
for num_list in given_list:
    if num_list in given_list:
        value = 0
        for new_list in range(1,num_list):
            if (num_list % new_list == 0):
                value = value + 1
        if (value == 1):
            prime_numbers_list.append(num_list)
print(f'2.prime numbers are present in given_list are: {prime_numbers_list}')

#3.given a python list [10,501,22,37,100,999,87,351] find out how many numbers are there in the given python list which are happy numbers
#solution:

#happy numbers means if results 1 when replaced by sum of squares of its digits recursively

#creating function with  parameter
def happy_numbers(given_list):
    for list_1 in range(len(given_list)):
        count = given_list[list_1]
        while count != 1 and count != 4:
            reminder = 0
            for list_2 in str(count):
                reminder += int(list_2) ** 2
            count = reminder
        if count == 1:
            total_list.append(given_list[list_1])
    return f'3.happy numbers are present in given_list are: {total_list}'
#input
given_list =  [10,501,22,37,100,999,87,351]
total_list = []

#calling function with print method and passing  given_list to argument
print(happy_numbers(given_list))

#4.write python program to find sum of first and last digit of an integer

#input
given_number = 123456
#conditional statements
if given_number < 9:
    print(f"sumof first and last digit is: {given_number * 2}" )
else:
    last_digit = given_number % 10
    first_digit = given_number
    #here we using while loop  repeatedly eecute till statement becomes true
    while first_digit > 9:
        first_digit = first_digit // 10

    result = last_digit + first_digit
    print(f'4.sum of first and last digit {given_number}: {result}')


#6.you have been given three list. your task is to find the duplicates in the three list .write a python program for the same.you can use your own python list

#solution:

#we using list comprehension method to find duplicates present in a list
list_1 = [1,3,5,7,7,23,45,23,67,89,45,76,67,1,5,3]
method = [element for element in list_1 if list_1.count(element) > 1]
duplicate_element_list1 = list(set(method))
print(f'6.given list are: {list_1}')
print(f'  duplicate elements are present in list_1: {duplicate_element_list1}')

# below we using for loop to find duplicate element in a list
List_2 = [1,2,5,7,3,2,1,7,5]
unique_list = []
duplicate_list = []
for count_list in List_2:
    if count_list not in unique_list:
        unique_list.append(count_list)
    elif count_list not in duplicate_list:
        duplicate_list.append(count_list)
print(f'  the given list are: {List_2}')
print(f'6.duplicate elements are present in list_2: {duplicate_list}')


#7.write a python program to find first non-repeating elements in given list of integers

#soution:

#given list
list_4 = [1,3,-2,4,-2,3,5,1,6]
empty_dict = {}

#using for loop to iteration
# transeverse hashlist
for nr_element in list_4:
    if nr_element not in empty_dict:
        empty_dict[nr_element] = 1
    else:
        empty_dict[nr_element] += 1
for count in list_4:
    if empty_dict[nr_element] == 1:
        print(f'7.first non repeating integer in list: {nr_element}')
        break

#8.write python program to find minimum element in a rotated and sorted list

def find_min_element(lists, len_list):
    minimum_ele = lists[0]
    #traversing over list
    for nums in range(len_list):
        if lists[nums] < minimum_ele:
            minimum_ele = lists[nums]
    print(f'8.minimum integer present in list is: {minimum_ele}')

given_lists = [501,22,37,2,100,999,351]
find_min_element(given_lists, len(given_lists))


#9.you have been given python list[10,20,30,9] and value of 59.write python program to find triplet in the list whose sum is equal to the given value
#solution:

def find_triplet(name,arr,sum):
    for num1 in range(0, arr -2):
        for num2 in range(num1 + 1, arr - 1):
            for num3 in range(num2 + 1, arr):
                if (name[num1] + name[num2] + name[num3]) == sum:
                    print(f'9. triplet in a list are: {name[num1],name[num2],name[num3]}')

givenn_list = [10,20,30,9]
sum = 59

#calling function
find_triplet(givenn_list, len(givenn_list), sum)

#10.given list [4,2,-3,1,6] write python program to find if there is a sub-list with sum equal to zero

def sub_list(give_list, len_list):
    for out_loop in range(len_list - 1):
        arr_list = give_list[out_loop]
        for inner_loop in range(out_loop + 1, len_list):
            arr_list += give_list[inner_loop]
            if arr_list == 0:
                print("10.True, there is an sub_list with sum equal zero in given list")

    return False
giv_list = [4,2,-3,1,6]
sub_list(giv_list, len(giv_list))
