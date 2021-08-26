import random
import copy

def SelectionSort(arr):
    count = 0
    length = len(arr)
    for i in range(length):
        minPos = i
        maxPos = length - i - 1
        #Swap minPos and maxPos if possible
        condition1 = (arr[minPos]>arr[maxPos])
        if condition1:
            temp = arr[minPos]
            arr[minPos] = arr[maxPos]
            arr[maxPos] = temp
        #Break condition
        condition2 = (minPos + 1 == maxPos)
        condition3 = (minPos == maxPos)
        if condition2 | condition3:
            break

        for j in range(i+1, length - 1 - i):
            count += 1
            if arr[j] < arr[minPos]:
                minPos = j
            if arr[j] > arr[maxPos]:
                maxPos = j
        #Swap
        if minPos != i:
            temp = arr[minPos]
            arr[minPos] = arr[i]
            arr[i] = temp
        if maxPos != length - 1 -i:
            temp = arr[maxPos]
            arr[maxPos] = arr[j + 1]
            arr[length - 1 - i] = temp


    # print('Number of iterations: ', count)
    return arr

def DataChecker(SortFunc):
    count = 0
    num_test = 2000
    num_arr = 256
    for k in range(num_test):
        a = []
        for i in range(num_arr):
            a.append(random.randint(1, 2 * num_arr))
        b = copy.deepcopy(a)
        a_sorted = SortFunc(a)
        a_sorted = copy.deepcopy(a_sorted)

        a.sort()
        if a == a_sorted:
            # print('Ture!!')
            count += 1
        else:
            print(b)
            break
    print('Accuracy: ', count / num_test)
    if count / num_test == 1:
        print('Algorithm is correct!')
    else:
        print('Algorithm is false')


if __name__ == "__main__":
    DataChecker(SelectionSort)



