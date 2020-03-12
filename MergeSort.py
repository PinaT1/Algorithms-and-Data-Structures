def Merge(A, p, q, r) :

    n1 = q-p+1
    n2 = r-q

    L = []
    R = []

    for i in range (0, n1) :
        L.insert(i, A[p+i])

    for j in range (0, n2) :
        R.insert(j, A[q+j+1])

    i=0
    j=0
    k=p

    while (i < n1 and j < n2) :

        if (L[i] <= R[j]):
            A[k] = L[i]
            i=i+1

        else :
            A[k] = R[j]
            j=j+1

        k=k+1

    while (i< n1):
        A[k] = L[i]
        i=i+1
        k=k+1

    while (j < n2):
        A[k] = R[j]
        j=j+1
        k=k+1



def MergeSort(A, p, r) :
    if p < r :
        q = int((p+r)/2)
        MergeSort(A, p, q)
        MergeSort(A, q+1, r)
        Merge(A, p, q, r)

