def countInversions(arr):
    numInv = mergeSort(arr, 0, len(arr)-1) #for (array, leftIndex, rightIndex)
    return numInv

def merge(arr, left, mid, right):
    #No need of merging if subarray form a sorted array after joining
    if(arr[mid] <= arr[mid+1]):
        return 0
    
    count = 0
    L = arr[left:mid+1] #starting array will start into the index 0 to middle
    R = arr[mid+1:right+1] #starting index starts at the middle to the end or rightmost index
    
    # Merge the temp arrays back into arr[l..r]
    
    i = 0     # Initial index of first and second subarray
    j = 0
    k = left     # Initial index of merged subarray
    
    # getting leght of each subarrays
    len_left  = mid+1-left
    len_right = right-mid

    while i < len_left and j < len_right: #this will compare the given array to sorted array
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            count += len_left - i
        k += 1
 
    arr[k: k + len_left - i] = L[i:]

    return count

def mergeSort(arr,left, right):
    numInv = 0
    if left < right:

        mid = (left+right)//2
        
        # Sort first and second halves
        numInv = mergeSort(arr, left, mid) #the left hand part or the first subarray
        numInv += mergeSort(arr, mid+1, right) #the right hand part or the second subarray
        numInv += merge(arr, left, mid, right) #use for merging
    #print(arr, numInv)
    return numInv



arr = [1, 3, 5, 2, 4, 6] 

result = countInversions(arr)

print(result)