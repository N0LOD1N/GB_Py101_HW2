# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
print("Problem 10------------------------------")
# Request user input
n = int(input("Enter a number of coins: "))
print()

# Fill the array with random 0s and 1s.
coins = []
import random
for i in range(n):
    coins.append(random.choice([0, 1]))
print("Coins on the table:")
print(' '.join(map(str, coins)))
print()

# Calculate number of occurences for each side
heads = 0
tails = 0
for side in coins:
    if side == 1:
        heads += 1
    else: 
        tails += 1

# Print the least amount of coins
if tails == heads:
    print(f'Turn {heads} coin(s) of either side.')
elif tails < heads:
    print(f"Turn {tails} coin(s) that show tails.")
else:
    print(f"Turn {heads} coin(s) that show heads.")

print()

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
print("Problem 12------------------------------")
S = int(input("Enter the sum of two numbers: ")) #S - sum
P = int(input("Enter the product of two numbers: ")) # P - product
print()

stat = 0
for X in range(1, S):
    Y = S - X
    if X * Y == P and stat == 0:
        print(f"Your numbers are {X} and {Y}")
        stat += 1
    elif X * Y == P and stat == 1:
        print(f"..OR {X} and {Y}")
print()

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
print("Problem 14------------------------------")
N = int(input("Enter a number: "))
sqr = 0
power = 0
while True:
    sqr = 2 ** power
    if sqr > N:
        break
    print(sqr, " ", end="")
    power += 1
print()