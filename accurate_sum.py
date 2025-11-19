def accurate_sum(needed: int, nums: list[int])-> list[int]:
    """Находит подмножество nums, сумма которого равна needed. Если не существует - поднимает ValueError. Только натуральные числа.

    Аргументы:
        needed (int): число, которое будет суммой подмножества;
        nums (list[int]): множество, из которого будет искаться подмножество

    Выводит:
        list[int]: искомое подмножество, сумма которого равна needed.
    """
    #проверка введенных данных
    for i in nums:
        if not (i > 0 and isinstance(i, int)):
            raise ValueError(f'Ненатуральное число в списке: {i}')
    if not (needed > 0 and isinstance(needed, int)):
        raise ValueError(f'Запрашиваемая сумма ненатуральна: {needed}')
    
    #сортировка
    sorted_nums = nums[:]
    sorted_nums.sort(reverse=True) #по убыванию
    
    total_sum = sum(sorted_nums)
    if needed == total_sum:
        return sorted_nums
    elif needed > total_sum:
        raise ValueError('Запрашиваемая сумма несоставима этими элементами')
   
    max_sum = needed
    dp = [False] * (max_sum + 1)
    dp[0] = True #сумма 0 всегда достижима :)
    prev = [-1] * (max_sum + 1) #самый большой элемент, с которым достижима сумма (меньше не нужны)
    prev[0] = 0
    
    #заполнение массива достижимых сумм
    for n in sorted_nums:
        for i in range(max_sum, n-1, -1):
            if dp[i-n] and not dp[i]:
                dp[i] = True
                prev[i] = n            
    
    #проверка достижимости
    if not dp[needed]:
        raise ValueError('Данное число несоставимо этими элементами')
    
    #восстановление использованных элементов
    current_sum = needed
    final_list = []
    while current_sum:
        final_list.append(prev[current_sum])
        current_sum -= prev[current_sum]

    final_list.sort(reverse=True)
    
    return final_list


if __name__ == "__main__":
    l = [100, 98, 86, 65, 43, 37, 22, 19, 14]
    print(accurate_sum(int(input(f"Введите число, которое нужно собрать суммой списка {l}\n")), l))