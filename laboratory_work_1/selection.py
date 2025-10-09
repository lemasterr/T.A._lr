# Лістинг 1.2 – Реалізація алгоритму сортування вибором (Python)
# Варіант №3

def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    print("Початковий масив:", arr)  # Початковий стан масиву

    # Зовнішній цикл проходить по всіх елементах списку (крім останнього)
    for i in range(n - 1):
        # Припускаємо, що поточний елемент є мінімальним
        min_index = i
        print(f"\nІтерація {i}: початковий min_index = {min_index}, поточний елемент = {arr[i]}")
        assignments += 1

        # Внутрішній цикл шукає найменший елемент у решті списку
        for j in range(i + 1, n):
            comparisons += 1
            print(f"  Порівняння: A[{j}]={arr[j]} < A[{min_index}]={arr[min_index]} ?", end=" ")
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1
                print("→ True → оновлено min_index =", min_index)
            else:
                print("→ False")

        # Перевіряємо, чи знайшовся менший елемент
        comparisons += 1
        if min_index != i:
            print(f"  Обмін A[{i}]={arr[i]} ↔ A[{min_index}]={arr[min_index]}")
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3

        # Поточний стан масиву після ітерації
        print("  Поточний масив:", arr)

    print("\nВідсортований масив:", arr)
    print(f"Порівнянь: {comparisons}, Присвоєнь: {assignments}")
    return arr, comparisons, assignments

my_list = [68, 97, 12, 15, 31, 40, 22, 50, 53]  # Вхідні дані (варіант №3)
selection_sort(my_list)
