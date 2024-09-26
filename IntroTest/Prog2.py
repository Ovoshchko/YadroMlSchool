def create_dict_from_lists(list1, list2, N):
    result_dict = {}
    
    for i in range(min(len(list1), N)):
        result_dict[list1[i]] = list2[i] if i < len(list2) else i
    
    for i in range(len(list1), N):
        result_dict[f'key_{i}'] = list2[i] if i < len(list2) else i
    
    for i in range(len(list2), N):
        result_dict[f'key_{i}'] = i
    
    return result_dict

# Пример использования функции
list1 = ['q', 'x', 'z', 's', 't', 'j', 'c', 'k', 'f', 'h', 'd', 'g', 'v', 'a', 'y', 'z', 'r', 'e', 'l', 'w']
list2 = [16, -2, -10, 0, -3, 8, -6, -6, 5, 6, 6, -3, 8, -5, 2, 10, 12]
N = 18

result = create_dict_from_lists(list1, list2, N)
print(result)