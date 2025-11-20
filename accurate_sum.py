def accurate_sum(needed: int, nums: list[int])-> tuple[int, list[int]]:
    """Находит комбинацию ближайшей к запрашиваемому числу суммы (>= needed) и возвращает эту сумму и использованные слагаемые.

    Аргументы:
        needed (int): запрашиваемое число, для которого будет находится ближайшее составимое число;
        nums (list[int]): список элементов, из которых составляется сумма.

    Выводит:
        tuple[int, list[int]]: кортеж из ближайшей достижимой суммы и списка, который формирует эту сумму.
    """
    #проверка введенных данных
    for i in nums:
        if not (i > 0 and isinstance(i, int)):
            raise ValueError(f'Ненатуральное число в списке: {i}')
    if not (needed > 0 and isinstance(needed, int)):
        raise ValueError(f'Запрашиваемая сумма ненатуральна: {i}')
    
    sorted_nums = nums[:]
    sorted_nums.sort(reverse=True) #по убыванию
    
    total_sum = sum(sorted_nums)
    if needed >= total_sum:
        return total_sum, sorted_nums
    
    max_num = sorted_nums[0] #самый большой элемент списка
    
    max_sum = needed + max_num #разумный предел искомой суммы
    dp = [-1] * (max_sum) #dp[max_sum] не нужен, потому что тогда достижим будет и max_sum - max_num = needed
    dp[0] = 0 #сумма 0 всегда достижима :)
    exit_flag = False
    #заполнение массива достижимых сумм
    for n in sorted_nums:
        for i in range(max_sum-1, n-1, -1):
            if dp[i-n] != -1 and dp[i] == -1:
                dp[i] = n
                if i == needed:
                    exit_flag = True
                    break
        if exit_flag:
            break
    
    #нахождение ближайшей достижимой суммы (сверху)
    if exit_flag:
        final_sum = needed
    else:
        for i in range(needed + 1, max_sum):
            if dp[i] != -1:
                final_sum = i
                break
    
    #восстановление использованных элементов
    current_sum = final_sum
    final_list = []
    while current_sum > 0:
        n = dp[current_sum]
        final_list.append(n)
        current_sum -= n
        
    return final_sum, final_list[::-1]


if __name__ == "__main__":
    l = [100, 98, 86, 65, 43, 37, 22, 19, 14]
    print(accurate_sum(int(input(f"Введите число, которое нужно собрать суммой списка {l}\n")), l))