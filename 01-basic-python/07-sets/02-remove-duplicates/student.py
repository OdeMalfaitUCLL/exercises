# Write your code here:
def remove_duplicates(xs):
    found = set()
    result = []
    for x in xs:
            if x not in found:
                found.add(x)
                result.append(x)
            else: continue
    return result
