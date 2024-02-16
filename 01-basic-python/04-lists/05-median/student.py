# Write your code here
def median(ns):
    ns.sort()
    if len(ns)%2 != 0:
        return ns[(len(ns)//2)]
    else:
        een = ns[(len(ns)//2)]
        twee = ns[(len(ns)//2)-1]
        return (een + twee)/2

