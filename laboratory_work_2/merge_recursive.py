# Лістинг 2.2 – Рекурсивне сортування злиттям (Python)
# Варіант №3

def merge(left, right):
    merged = []
    i = j = 0
    print(f"  Злиття {left} і {right}")
    while i < len(left) and j < len(right):
        print(f"    Порівняння: {left[i]} <= {right[j]} ?", end=" ")
        if left[i] <= right[j]:
            merged.append(left[i])
            print("→ True")
            i += 1
        else:
            merged.append(right[j])
            print("→ False")
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    print(f"  Результат: {merged}")
    return merged


def merge_sort_recursive(arr, depth=0):
    print("  " * depth + f"Рекурсія рівень {depth}: {arr}")
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid], depth + 1)
    right = merge_sort_recursive(arr[mid:], depth + 1)
    result = merge(left, right)
    print("  " * depth + f"Після злиття рівень {depth}: {result}")
    return result

my_list = [68, 97, 12, 15, 31, 40, 22, 50, 53]
sorted_list = merge_sort_recursive(my_list)
print("\nВідсортований масив:", sorted_list)
