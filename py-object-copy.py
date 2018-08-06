import copy

old_items = [[1,4,6],[4,6,8],['g',8,3]]
new_items = old_items
new_items[2][0] = 3
print('Old items', old_items)
print('Id of old ', id(old_items))

print('New items', new_items)
print('Id of New ', id(new_items))
print()
print('##############\n')
print('Shalow Copy method')
old_list = [[1,4,6],[4,6,8],['g',8,3]]

new_list = copy.copy(old_list)
old_list[0][2] = 'bb'

old_list.append([5,9,2])
new_list.remove([4,6,8])
new_list.append([7,11,34])
new_list.append([3,56,34])
print('Old List', old_list)
print('Id of old List ', id(old_list))
print('New List', new_list)
print('Id of New List ', id(new_list))
print()


print('##############\n')
print('Deep Copy method')
print()
old_matrix = [[4,4,1],[2,2,8],['r',1,4]]

new_matrix = copy.deepcopy(old_matrix)

# Check Line 17 it still changes in new_list 
# but in case of deepcopy it not refelects in new matrix
old_matrix[0][1] = 'UC'
print('Old Matrix', old_matrix)
print('New Matrix', new_matrix)

