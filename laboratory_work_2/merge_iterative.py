# Лістинг 2.1 – Ітеративне сортування злиттям (Python)
# Варіант №3

def merge(left, right):
    merged = []
    i = j = 0
    print(f"Злиття {left} і {right}")
    while i < len(left) and j < len(right):
        print(f"  Порівняння: {left[i]} <= {right[j]} ?", end=" ")
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
    print(f"  Результат злиття: {merged}\n")
    return merged


def merge_sort_iterative(arr):
    print("Початковий масив:", arr)
    step = 1
    while step < len(arr):
        for i in range(0, len(arr), 2 * step):
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]
            if right:
                merged = merge(left, right)
                arr[i:i + 2 * step] = merged
                print(f"Після злиття підмасивів (крок {step}): {arr}")
        step *= 2
    print("\nВідсортований масив:", arr)
    return arr

my_list = [68, 97, 12, 15, 31, 40, 22, 50, 53]
merge_sort_iterative(my_list)
