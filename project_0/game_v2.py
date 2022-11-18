#P.S. Так как мой компьютер не справляется с 1000 подходов угадывания, изменил число попыток на 100.


"""Игра угадай число.
Компьютер сам загадывает и сам угадывает число.
"""

import numpy as np
import math as math

def random_predict(number:int=np.random.randint(1, 101)) -> int:
    """Рандомно угадываем число.

    Args:
        number (int, optional): Загаданное число. По умолчанию рандомно загадывается компьютером в диапазоне 1-100.

    Returns:
        int: Число попыток.
    """

    count = 0
    lst_num = list(range(101))

    while True: # В цикле будем брать за искомое среднее число из возможных, и с каждой иттерацией уменьшать диапазон чисел вдвое, пока не найдем нужное.
        count += 1
        predict_number = np.mean(lst_num)
        
        if number == predict_number:
            break 
        if predict_number < number: 
            predict_number = int(math.floor(predict_number)) # Округляем предполагаемое число в сторону меньшего целого, чтобы передать его как нижнюю границу диапазона чисел. 
            lst_num = list(range(predict_number,lst_num[-1]+1)) 
        if predict_number > number:
            predict_number = int(math.ceil(predict_number)) # Округляем предполагаемое число в сторону большего целого, чтобы передать его как верхнюю границу диапазона чисел. 
            lst_num = list(range(lst_num[0],predict_number+1)) 
            
    return count

if __name__ == '__main__':
    # RUN
    random_predict()

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 100 подходов угадывает наш алгоритм.

    Args:
        random_predict ([type]): функция угадывания.

    Returns:
        int: среднее количество попыток.
    """
    count_ls = []
    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, 100)  # Загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    