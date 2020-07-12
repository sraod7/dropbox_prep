from random import random, randint
from threading import Thread, current_thread


def merge_sort(arr):
    print(f'{current_thread().name} \n')
    if len(arr) > 1:
        mid = len(arr) // 2
        low = arr[mid:]
        high = arr[:mid]
        t1 = Thread(target=merge_sort, name=f'{randint(1,100000)}', args=(low,))
        t2 = Thread(target=merge_sort, name=f'{randint(100000, 2000000)}', args=(high,))

        t1.start()
        t2.start()
        t1.join()
        t2.join()

        i = 0
        j = 0
        k = 0

        while i < len(low) and j < len(high):
            if low[i] < high[j]:
                arr[k] = low[i]
                i += 1
            else:
                arr[k] = high[j]
                j += 1
            k += 1

        while i < len(low):
            arr[k] = low[i]
            i += 1
            k += 1

        while j < len(high):
            arr[k] = high[j]
            j += 1
            k += 1

myList = [54,26,93,17,77,31,44,55,20]
merge_sort(myList)
print(myList)