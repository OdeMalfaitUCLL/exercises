def lineair_search(students,target_id):
    result =[s for s in students if s.id == target_id]
    if result == []:
        result = None
    return result

def binary_search(students, target_id):
    left = 0
    right = len(students)-1
    while left < right:
        middle = left + right //2
        middle_id = students[middle].id
        if target_id > middle_id:
            left = middle + 1
        elif target_id < middle_id:
            right = middle
        else: return students[middle]
    return None