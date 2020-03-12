def left(i):

    return 2*i;

def right(i) :
    return ((2*i) + 1)

def swap( A, x, y ) :
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


def MaxHeapify(A, i, heapsize) :

    l = left(i)
    r = right(i)
    largest = i;

    if(l <= heapsize and A[l] > A[i]) :
        largest = l;

    if(r <= heapsize and A[r] > A[largest]) :
        largest = r;

    if(largest != i ) :
        swap(A, i, largest)
        MaxHeapify(A, largest, heapsize)


def BuildMaxHeap(A) :
    heapsize=len(A)-1
    leastParent = int(len(A)/2)
    for i in range (leastParent , -1, -1 ):
        MaxHeapify(A, i,heapsize)


def HeapSort(A) :

    BuildMaxHeap(A)
    heapsize=len(A)-1
    for i in range (heapsize, 0, -1) :
        swap(A,0,i)
        heapsize = heapsize - 1
        MaxHeapify(A, 0, heapsize)