import numpy  as np
list1 = [1,2,3,4,5]
list2 = [2,3,4,5,6] 
list3 = [5,6,7,8,9]

nested_list = [list1, list2, list3]
arr = np.array(nested_list);
print(arr[1:2,1:4])