def split_in_two(ns):
        index = len(ns)//2
        return (ns[:index],ns[index:])

def merge_sorted(left,right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < left[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(left[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(ns):
    if len(ns) <= 1:
        return ns
    else:
        left,right = split_in_two(ns)
        sorted_left = sorted(left)
        sorted_right= sorted(right)
        return  merge_sorted(sorted_left,sorted_right)