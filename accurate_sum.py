def accurate_sum(needed: int, nums: list[int])-> tuple[int, list[int]]:
    """Находит комбинацию ближайшей к запрашиваемому числу суммы (>= needed) и возвращает эту сумму и использованные слагаемые.

    Аргументы:
        needed (int): запрашиваемое число, для которого будет находится ближайшее составимое число;
        nums (list[int]): список элементов, из которых составляется сумма.

    Выводит:
        tuple[int, list[int]]: кортеж из ближайшей достижимой суммы и списка, который формирует эту сумму.
    """
    #тут могла быть ваша реклама (проверка типа вводимых данных)
    sorted_nums = nums[:]
    sorted_nums.sort(reverse=True) #по убыванию
    
    total_sum = sum(sorted_nums)
    if needed == 0 or total_sum == 0:
        return 0, []
    if needed >= total_sum:
        return total_sum, sorted_nums
    
    max_num = sorted_nums[0] #самый большой элемент списка
    
    max_sum = needed + max_num #разумный предел искомой суммы
    dp = [False] * (max_sum) #dp[max_sum] не нужен, потому что тогда достижим будет и max_sum - max_num = needed
    dp[0] = True #сумма 0 всегда достижима :)
    
    #заполнение массива достижимых сумм
    for n in sorted_nums:
        for i in range(max_sum-1, n-1, -1):
            if dp[i-n]:
                dp[i] = True
    
    #нахождение ближайшей достижимой суммы (сверху)
    for i in range(needed, max_sum):
        if dp[i]:
            final_sum = i
            break
    
    #восстановление использованных элементов
    current_sum = final_sum
    final_list = []
    for n in sorted_nums:
        if (current_sum - n) >= 0:
            if dp[current_sum-n]:
                final_list.append(n)
                current_sum -= n
        if current_sum == 0:
            break
        
    final_list.sort(reverse=True)
    
    return final_sum, final_list


if __name__ == "__main__":
    l = [100, 98, 86, 65, 43, 37, 22, 19, 14]
    print(accurate_sum(int(input(f"Введите число, которое нужно собрать суммой списка {l}\n")), l))