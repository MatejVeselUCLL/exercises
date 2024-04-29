
def linear_search(students, target_id):
    for student in students:
        if student.id == target_id:
            return student

def binary_search(students, target_id):
    if len(students) == 0:
        return
    
    left = 0
    right = len(students) - 1
    for i in range(10000):
        middle = (left + right) // 2
        if target_id == students[middle].id:
            return students[middle]
        elif left == right:
            return
        elif target_id < students[middle].id:
            right = middle - 1
        else:
            left = middle + 1

        