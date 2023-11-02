# Exercise 5

def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])


arr = [113, 175, 12]

total_students = sum(arr)

lab_group = 24

complete_groups, remaining_students = divmod(total_students, lab_group)

print('Total number of complete groups', complete_groups)
print('Remaining students', remaining_students)
