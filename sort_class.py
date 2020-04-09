

#avg O(n^2)

def bubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range (0,len(arr)-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


def selectionSort(arr):
    for i in range(len(arr)-1):
        minidex=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minidex]:
                minidex=j
        if i !=minidex:
            arr[i],arr[minidex]=arr[minidex],arr[i]
    return arr


def insertionSort(arr):
    for i in range(len(arr)):
        preindex=i-1
        current=arr[i]
        while preindex>=0 and arr[preindex]>current:
            arr[preindex+1]=arr[preindex]
            preindex-=1
        arr[preindex+1]=current
    return arr



#O（nlogn）

def shellSort(arr):
    import math
    gap=1
    while(gap<len(arr)/3):
        gap=gap*3+1
    while gap>0:
        for i in range(gap,len(arr)):
            temp=arr[i]
            j=i-gap
            while j>=0 and arr[i]>temp:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap]=temp
        gap=math.floor(gap/3)
    return arr




def mergeSort(arr):
    import math
    if(len(arr)<2):
        return arr
    middle=math.floor(len(arr)/2)
    left,right=arr[0:middle],arr[middle:]
    return merge(mergeSort(left),mergeSort(right))

def merge(left,right):
    result=[]
    while left and right:
        if left[0]<=right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result




def quickSort(arr,left=None,right=None):
    left=0 if not isinstance(left,(int,float)) else left
    right=len(arr)-1 if not isinstance(right,(int,float)) else right
    if left<right:
        pindex=p(arr,left,right)
        quickSort(arr,left,pindex-1)
        quickSort(arr,pindex+1,right)
    return arr
def p(arr,left,right):
    pivot=left
    index=pivot+1
    i=index
    while i<=right:
        if arr[i]<arr[pivot]:
            swap(arr,i,index)
            index+=1
        i+=1
        swap(arr,pivot,index-1)
        return index-1
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]


def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr,i)
def heapify(arr,i):
    left=2*i+1
    right=2*i+2
    largest=i
    if left<arrLen and arr[left]>arr[largest]:
        largest=left
    if right<arrLen and arr[right]>arr[largest]:
        largest=right
    if largest !=i:
        swap(arr,i,largest)
        heapify(arr,largest)
def heapSort(arr):
    global arrLen
    arrLen=len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen-=1
        heapify(arr,0)
    return arr



#O(n+k)

def countingSort(arr,maxValue):
    bucketLen=maxValue+1
    bucket=[0]*bucketLen
    sortedIndex=0
    arrLen=len(arr)
    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]]=0
        bucket[arr[i]]+=1
    for j in range(bucketLen):
        while bucket[j]>0:
            arr[sortIndex]=j
            sortIndex+=1
            bucket[j]-=1
    return arr

        
arr=[4,5,3,2,7,9,1,33,56,21,14,59,87]
print(insertionSort(arr))
