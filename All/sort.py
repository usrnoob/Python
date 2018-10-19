
# Bubble Sort
def bubbleSort(arr):
    for i in range(len(arr) - 1):    # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(arr) - i - 1):  # ｊ为列表下标
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [6, 3, 8, 2, 9, 1]

print (bubbleSort(arr))


#
arr1=[1,3]
print(range(len(arr1)))

