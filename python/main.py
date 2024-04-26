import timeit
import signal
import sys
import random
import re

def main():
    ##########################################################
    ###                      ЗАДАЧА №1
    ##########################################################
    
    print("\nЗАДАЧА №1 \n")

    # программа может сама сгененрировать несколько чисел для проверки
    autotest = get_input_int('введите количество тестовых номеров (0 - ручной ввод): ')
    

    if autotest:  # если выбран автотест
        # случайные числа от 0 до 100000 
        for i in range(autotest):
            number = random.randint(0, 100000)
            print(f'результат для числа {number}:')
            print_quantity(number)
    else :  # если выбран ручной ввод
        number = get_input_int('Введите число компьютеров: ')
        print_quantity(number)

    ##########################################################
    ###                      ЗАДАЧА №2
    ##########################################################
    
    print("\nЗАДАЧА №2 \n")
    
    # получение списка чисел для поиска общих делителей
    numbers = input('введите список чисел, разделённых запятой или пробелом: ')
    numbers = re.findall(r'\d+', numbers)
    numbers = [int(i) for i in numbers]
    # формирование списка множеств делителей для каждого числа
    list_common_dividers = [dividers(i) for i in numbers]

    # выполнение пересечения множеств
    intersection = set.intersection(*list_common_dividers)
    if len(intersection):
        print("Общие делители: ", *intersection)
    else:
        print("Общие делители отсутсвуют")
 
    ##########################################################
    ###                      ЗАДАЧА №3
    ##########################################################
    
    print("\nЗАДАЧА №3 \n")
    
    # получение min max диапазона для поиска ростых чисел
    min_max = input('введите два числа (min, max), разделённых запятой или пробелом: ')
    min_max = re.findall(r'\d+', min_max)[:2]
    min_max = [int(i) for i in min_max]
    # получение простых чисел из диапазона
    result = prime_numbers(*min_max)
    print(f"Простые числа в диапазоне [{min_max[0]}:{min_max[1]}]: ", *result)   

    ########################################################
    #                      ЗАДАЧА №4
    ########################################################
    
    print("\nЗАДАЧА №4 \n")
    
    # получение числа для таблицы умножения
    max = get_input_int('введите максимальное число таблицы умножения: ')
    # формирование линнии чисел [' ' 1  2  3  4  5]
    line = [' '] + list(range(1, max + 1))
    # вывод первой строки
    print(*line, end='', sep='  ')
    # вывод остальных строк (форматирование работает до 9, для бОльших чисел я не стал усложнять код)
    [
        print(f'\n{row}' if row == number else '',  ''.join([' ']*int(2/len(f'{number}'))), f'{number}', end='', sep='') 
        for row in line[1:] 
        for number in [row*i for i in line] 
    ]
    print('\r')

    
def print_quantity(number: int) -> None:
    """
    функция склонения наименования компьютеров в зависимости от количества
    """
    # count_time = True
    # start = timeit.default_timer()

    remainders = number % 100, number % 10, number
    match remainders:
        # если два последних разряда от 11 до 19
        case _ as a, _, c if (10 < a and a < 20) or (10 < c and c < 20) :
           print(f'{number} компьютеров')  
        # если последний разряд == 0  или от 5 до 9
        case _ as a, b, _ if (b == 0 or (b >= 5 and b <= 9)) :
           print(f'{number} компьютеров') 
        # если последний разряд == 1
        case _ as a, b, _ if (b == 1) :
           print(f'{number} компьютер') 
         # если последний разряд от 2 до 4
        case _ as a, b, _ if (2 <= b and b <= 4) :
           print(f'{number} компьютера') 
    
    # stop = timeit.default_timer()
    # if count_time:
    #     print('Time: ', stop - start)      
    

def dividers(number: int) -> set[int]: 
    """
    функция поиска делителей числа с помощью простых чисел
    """
    dividers = set()
    end = False
    # получение простых чисел в диапазоне от 2 до заданного числа
    prime_nums = prime_numbers(2, number) 
    # инициализация результата деления заданным числом
    remainder = number
    # поиск простых чисел, на которы заданное число делится без остатка
    while not end:
        # 
        for prime_number in prime_nums:
            # если результат деления равен простому числу завершаем цикл
            if remainder/prime_number==1:
                dividers.add(prime_number)
                end=True 
                break
             # если заданное число делится без остатка, сохраняем это простое число
            if not (new_remainder := remainder % prime_number):
                dividers.add(prime_number)
                # меняем переменную с заданным числом на остатки от деления
                remainder = remainder / prime_number
                break
  
    # перемножение полученных простых чисел для поиска составных делителей             
    list_dividers = list(dividers)   
    for i in range(len(list_dividers)-1):
        for k in range(i+1, len(list_dividers)):
            list_dividers.append(list_dividers[i]*list_dividers[k]) 
    return set(list_dividers)
    

def prime_numbers(min: int, max: int) -> list[int]:
    """
    возвращает список простых чисел в диапазоне от min до max
    """
    prime_numbers = []
    for num in range (min if min > 1 else 2, max + 1):
        for i in range(2, num):
            if not num % i:
                break
        else:
            prime_numbers.append(num)
    return prime_numbers
    
    
def get_input_int(text: str) -> int:
    """
    получение пользовательского ввода в виде int
    """
    
    input_int = 0
    
    while True:
        try:
            input_int = int(input(text))
        except Exception as err:
            print(f'Введены неправильные данные, попробуйте ещё раз')
            continue
        else:
            break   
    return input_int
         
    
def signal_handler(sig, frame):
    """
    прекращение работы по Ctrl+C
    """ 
    print('Exit by Ctrl+C')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    main()