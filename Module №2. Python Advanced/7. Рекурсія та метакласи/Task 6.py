
# Завдання №6. Напишіть рекурсивну функцію, яка підраховує глибину вкладеності списків.


def depth(lists):
    if isinstance(lists, list):
        if len(lists) == 0 or len(lists) == 1:
            return 1
        return len(lists) - 1 + depth(lists.pop())
    else:
        return "Не є списком!"


print(depth([1, [2, [3, [4, [5]]]]]))
