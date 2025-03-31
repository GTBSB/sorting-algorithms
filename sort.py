def quick_sort(arr):
    # Базовый случай: если массив состоит из одного или ноль элементов, он уже отсортирован
    if len(arr) <= 1:
        return arr
    
    # Выбираем опорный элемент (обычно берем последний)
    pivot = arr[-1]
    
    # Сортируем элементы, меньшие опорного
    left = [x for x in arr[:-1] if x <= pivot]
    
    # Сортируем элементы, большие опорного
    right = [x for x in arr[:-1] if x > pivot]
    
    # Рекурсивно сортируем обе части и соединяем их с опорным элементом
    return quick_sort(left) + [pivot] + quick_sort(right)

# Пример использования
arr = [10, 7, 8, 9, 1, 5]
print("Исходный массив:", arr)

sorted_arr = quick_sort(arr)

print("Отсортированный массив:", sorted_arr)