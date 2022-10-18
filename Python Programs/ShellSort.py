# Python3 program for implementation of Shell Sort
  
def shellSort(arr, n):
    gap=n//2
      
    while gap>0:
        j=gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j<n:
            i=j-gap 
              
            while i>=0:
                # If value on right side is already greater than left side value
                # We do not swap else we swap
                if arr[i+gap]>arr[i]:
                    break
                else:
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]
  
                i=i-gap 
                # To check left side also
                # If the element present is greater than current element 
            j+=1
        gap=gap//2
  
  
  
# driver to check the code
arr2 = [2, 4, 78, 65, 1]
print("Given array:",arr2)
  
shellSort(arr2,len(arr2))
print("Sorted array",arr2) 