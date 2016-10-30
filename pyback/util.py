def partition(listc, condition, start, end):
    pivot = listc[end]
    pin = start
    for i in range(start, end):
        if (condition(listc[i], pivot)):
            temp = listc[i]
            listc[i] = listc[pin]
            listc[pin] = temp
            pin += 1
    temp = listc[pin]
    listc[pin] = listc[end]
    listc[end] = temp
    return pin

def quickSort(listc, condition, start, end):
    if (start < end):
        pin = partition(listc, condition, start, end)
        quickSort(listc, condition, start, pin-1)
        quickSort(listc, condition, pin+1, end)
