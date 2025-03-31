def heapify(arr, n, i):
    largest = i  # Инициализация самого большого элемента как корня
    left = 2 * i + 1     # Левый дочерний элемент
    right = 2 * i + 2    # Правый дочерний элемент

    # Если левый дочерний элемент больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый дочерний элемент больше самого большого элемента
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если самый большой элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Обмен

        # Рекурсивно вызываем heapify для поддерева, которое изменилось
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение максимальной кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Перемещаем текущий корень в конец
        heapify(arr, i, 0)  # Восстанавливаем кучу

# Пример использования
arr = [12, 11, 13, 5, 6, 7]
print("Исходный массив:", arr)

heap_sort(arr)

print("Отсортированный массив:", arr)
