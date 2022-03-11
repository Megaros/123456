# Ввод от пользователя с проверкой
while True:
    try:
        array = list(map(int, input('Введите массив целых чисел через пробел: ').split()))

        # Если полученный ввод не число, будет вызвано исключение
    except ValueError:
        # Цикл будет повторяться до правильного ввода
        print("\033[33m\033[40m{}\033[0m".format('Error!'), 'Есть не целое число, попробуйте снова.')
    else:
        break
while True:
    try:
        any_number = int(input('Введите любое целое число:'))
    except ValueError:
        print("\033[33m\033[40m{}\033[0m".format('Введено не целое число'))
    else:
        array.append(any_number)
        break


# Созаем функцию по алгоритму быстрой сортировки
def qsort(array, left=0, right=len(array) - 1):
    middle = (left + right) // 2
    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
    return array


# Функция поиска индекса введенного числа
def binary_search(array, any_number, left=0, right=len(array) - 1):
    middle = (right + left) // 2  # находимо середину
    if array[middle] == any_number:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif any_number < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, any_number, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, any_number, middle + 1, right)


print(qsort(array))
index_any_number = binary_search(array, any_number, right=len(array) - 1)
index_left = 0
if 0 != index_any_number != len(array) - 1:
    index_left = index_any_number - 1
    print('Индекс числа слева = ', index_left)
elif index_any_number == 0:
    print('Введенное число является минимальным среди чисел последовательности')
elif index_any_number == len(array) - 1:
    print('Введенное число является максимальным среди чисел последовательности')
