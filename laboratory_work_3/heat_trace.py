# Лічильники
comp = 0       # кількість порівнянь
assigns = 0    # кількість присвоювань (swap рахуємо як 3)

def swap(arr, i, j):
    global assigns
    assigns += 3
    print(f"  Обмін: arr[{i}]={arr[i]} ↔ arr[{j}]={arr[j]}")
    arr[i], arr[j] = arr[j], arr[i]

def sink(arr, i, n, tag=""):
    global comp
    k = i
    while True:
        j = 2 * k + 1
        if j >= n:
            break
        comp += 1                       # порівняння існування правого>лівого
        if j + 1 < n:
            comp += 1
            if arr[j + 1] > arr[j]:
                j += 1
        comp += 1                       # порівняння батько vs більший син
        print(f"{tag}Порівняння: arr[{k}]={arr[k]} < arr[{j}]={arr[j]} ?")
        if arr[k] >= arr[j]:
            break
        swap(arr, k, j)
        k = j

def heapsort_trace(arr):
    global comp, assigns
    comp = assigns = 0
    n = len(arr)
    print("Початковий масив:", arr)

    print("\n--- Фаза 1: Побудова максимальної купи ---")
    for i in range(n // 2 - 1, -1, -1):
        print(f"Занурення з індексу {i}: {arr[i]}")
        sink(arr, i, n, tag="    ")
    print("Після побудови купи:", arr)

    print("\n--- Фаза 2: Сортування ---")
    for i in range(n - 1, 0, -1):
        swap(arr, 0, i)
        print(f"↓ Після обміну кореня з A[{i}]:", arr)
        sink(arr, 0, i, tag="    ")
        print(f"→ Поточний стан:", arr)

    print("\nВідсортований масив:", arr)
    print(f"Підсумки: порівнянь={comp}, присвоювань={assigns}")
    return arr, comp, assigns

if __name__ == "__main__":
    A = [68, 97, 12, 15, 31, 40, 22, 50, 53]
    heapsort_trace(A)

