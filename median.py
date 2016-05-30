#program to find a median in a list
def median(lists):
    lists.sort()
    print lists
    mid=len(lists)/2
    print mid
    if len(lists)%2==0:
        med=float(lists[mid]+lists[mid-1])/2
        return med
    else:
        med=lists[mid]
        return med
    
print
print median([5,4,3,2,1])