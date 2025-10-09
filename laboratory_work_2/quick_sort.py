# Лістинг 2.3 – Швидке сортування за Хоаром (Python)
# Варіант №3

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low
    j = high
    print(f"\nPartition: low={low}, high={high}, pivot={pivot}")
    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            print(f"  Повертаємо індекс розділення {j}")
            return j
        print(f"  Обмін: arr[{i}]={arr[i]} ↔ arr[{j}]={arr[j]}")
        arr[i], arr[j] = arr[j], arr[i]
        print("  Поточний масив:", arr)
        i += 1
        j -= 1


def quicksort(arr, low, high, depth=0):
    print("  " * depth + f"Рекурсія {depth}: {arr[low:high+1]}")
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p, depth + 1)
        quicksort(arr, p + 1, high, depth + 1)

my_list = [68, 97, 12, 15, 31, 40, 22, 50, 53]
print("Початковий масив:", my_list)
quicksort(my_list, 0, len(my_list) - 1)
print("\nВідсортований масив:", my_list)
