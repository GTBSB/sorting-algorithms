def bubble_sort(arr):
    n = len(arr)
    
    # Проходим по всем элементам массива
    for i in range(n):
        # Флаг для оптимизации: если в ходе прохода не было перестановок, сортировка завершена
        swapped = False
        
        # Последние i элементов уже отсортированы, так что можно их игнорировать
        for j in range(0, n-i-1):
            # Сравниваем соседние элементы
            if arr[j] > arr[j+1]:
                # Меняем их местами
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # Если за проход не было перестановок, выходим из цикла
        if not swapped:
            break

    return arr

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
print("Исходный массив:", arr)
sorted_arr = bubble_sort(arr)
print("Отсортированный массив:", sorted_arr)
