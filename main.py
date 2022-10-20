import math
import random
import collections

memo = {}
bonus_arr = [100, 500, 1000, 2500, 5000, 10000]


def targetSum(round):
    return math.floor(7 * round / 3)


def numbers(sum):
    num = []
    for i in range(5):
        num.append(random.randint(1, sum))
    return num


def bestSum(sum, num, memo, shortComb_list):
    if sum in memo: return memo[sum]
    if sum == 0: return []
    if sum < 0: return None
    shortComb = None
    for n in num:
        remain = sum - n
        result = bestSum(remain, num, memo, shortComb_list)
        if result != None:
            comb = [*result, n]
            if shortComb == None or len(shortComb) > len(comb): shortComb = comb
            if len(comb) == len(shortComb):
                sum_of_comb = sum
                if sum_of_comb == totSum:
                    if len(shortComb_list) == 0: shortComb_list.append(comb)
                    if len(comb) <= len(shortComb_list[0]):
                        if len(comb) < len(shortComb_list[0]): shortComb_list.clear()
                        shortComb_list.append(comb)
    if shortComb not in shortComb_list: memo[sum] = shortComb
    if len(shortComb_list) > 1:
        for comb1 in shortComb_list:
            for comb2 in shortComb_list:
                if collections.Counter(comb1) == collections.Counter(comb2): shortComb_list.remove(comb2)
    return shortComb


def bonus(score):
    if score == None: score = 0
    if score >= bonus_arr[0] and score < bonus_arr[1]:
        print("Congrats! You made it past " + str(bonus_arr[0]) + " points. You get a " + str(score * 1.25) + " bonus.")
        score += score * 1.25
        del bonus_arr[0]
        return math.floor(score)
    return score


def gamePlay():
    global sum
    global score
    print('What is the shortest combination?')
    player_input = input("Sum: " + str(sum) + ' Choose numbers or \'0\' for None, and separate with \'+\': ' + str(num) + '   ')
    if player_input[-1] == '+': player_input = player_input[:-1]
    player_input = list(player_input.split('+'))
    player_input = [eval(i) for i in player_input]
    if shortComb_list == [] and player_input == [0]:
        score += 10
        print('Correct!!!')
        print('Score: ' + str(score))
        print('')
        return score
    for comb in shortComb_list:
        if collections.Counter(player_input) == collections.Counter(comb):
            score += sum
            print('Correct!!!')
            print('Score: ' + str(score))
            print('')
            return score
    if shortComb_list == []: return print('Wrong!!! The correct answer is: NONE')
    score -= sum
    print('Wrong!!! The correct answer is: ' + str(shortComb_list))
    print('Score: ' + str(score))
    print('')
    return score


if __name__ == "__main__":
    round = 1
    score = 99
    while round < 100:
        shortComb = []
        shortComb_list = []
        sum = targetSum(round)
        totSum = sum
        num = numbers(sum)
        memo.clear()
        if shortComb not in shortComb_list: bestSum(sum, num, memo, shortComb_list)
        score = bonus(score)
        score = gamePlay()

        round += 1