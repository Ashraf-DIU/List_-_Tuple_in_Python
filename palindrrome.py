list1 = [7 , 4, 12, 4, 7]
list2 = [7 , 4, 12, 8]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")