#-------------------------------------------------------------------------------
# Name:        Prediction of number in range 1-100
# Author:      Ivan Kleymenov
#-------------------------------------------------------------------------------
import numpy as np

def game_core_v3(number):
    '''Predict number using dividing a range in half'''
    count=1
    count_break=100
    min_val=1
    max_val=100
    remainder=0
    predict=(max_val + min_val) // 2

    while number != predict:
        count+=1
        if number > predict:
            min_val=predict
            # remainder helps to predict max value in range
            # predict value rounds up
            remainder=1 if (max_val + min_val) % 2 >= 0.5 else 0
        elif number < predict:
            max_val=predict
            remainder=0
        predict=(max_val + min_val) // 2 + remainder

        if count==count_break:
            print('Останов по количеству попыток: достигло {} для числа {}'.format(count,number))
            break

    return (count)


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# start scoring
score_game(game_core_v3)

