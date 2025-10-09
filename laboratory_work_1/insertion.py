# Лістинг 1.4 – Реалізація алгоритму сортування вставками (Python)
# Варіант №3

def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    print("Початковий масив:", arr)  # Початковий стан масиву

    # Цикл ітерується від другого елемента до кінця
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        print(f"\nІтерація {i}: key = {key}")
        assignments += 2

        # Пересуваємо елементи, що більші за key, вправо
        while j >= 0 and arr[j] > key:
            print(f"  A[{j}]={arr[j]} > key={key}? → True → зсув праворуч")
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            comparisons += 1

        # Коли цикл завершився (умова стала False)
        if j >= 0:
            print(f"  A[{j}]={arr[j]} > key={key}? → False (завершення вставки)")
            comparisons += 1

        # Вставляємо key на своє місце
        arr[j + 1] = key
        assignments += 1
        print("  Поточний масив:", arr)

    print("\nВідсортований масив:", arr)
    print(f"Порівнянь: {comparisons}, Присвоєнь: {assignments}")
    return arr, comparisons, assignments


# === Головна частина програми ===
my_list = [68, 97, 12, 15, 31, 40, 22, 50, 53]  # Вхідні дані (варіант №3)
insertion_sort(my_list)
