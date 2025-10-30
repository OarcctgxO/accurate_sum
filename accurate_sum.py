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
        raise ValueError(f'Запрашиваемая сумма ненатуральна: {i}')
    
    #сортировка
    sorted_nums = nums[:]
    sorted_nums.sort(reverse=True) #по убыванию
    
    total_sum = sum(sorted_nums)
    if needed == total_sum:
        return sorted_nums
    elif needed > total_sum:
        raise ValueError('Запрашиваемая сумма несоставима этими элементами')
    
    max_num = sorted_nums[0] #самый большой элемент списка
    
    max_sum = needed
    dp = [False] * (max_sum + 1)
    dp[0] = True #сумма 0 всегда достижима :)
    
    #заполнение массива достижимых сумм
    for n in sorted_nums:
        for i in range(max_sum, n-1, -1):
            if dp[i-n]:
                dp[i] = True
    
    #проверка достижимости
    if not dp[needed]:
        raise ValueError('Данное число несоставимо этими элементами')
    
    #восстановление использованных элементов
    current_sum = needed
    final_list = []
    for n in sorted_nums:
        if (current_sum - n) >= 0:
            if dp[current_sum-n]:
                final_list.append(n)
                current_sum -= n
        if current_sum == 0:
            break
    
    return final_list


if __name__ == "__main__":
    l = [100, 98, 86, 65, 43, 37, 22, 19, 14]
    print(accurate_sum(int(input(f"Введите число, которое нужно собрать суммой списка {l}\n")), l))