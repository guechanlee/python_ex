from our_dice import Dice

def sortNumbers(*numbers):
    list = sorted(numbers)
    list.sort(reverse=True)
    return list

gamer1Dice = Dice()
gamer2Dice = Dice()
gamer3Dice = Dice()

for i in range(5):
    gamer1Dice.playDice()
    gamer2Dice.playDice()
    gamer3Dice.playDice()

print(f'gamer1: {gamer1Dice.getNumbers()}')
print(f'gamer2: {gamer2Dice.getNumbers()}')
print(f'gamer3: {gamer3Dice.getNumbers()}')

print(f'sum of gamer1: {gamer1Dice.getSum()}')
print(f'sum of gamer2: {gamer2Dice.getSum()}')
print(f'sum of gamer3: {gamer3Dice.getSum()}')

sortedNumbers = sortNumbers(gamer1Dice.getSum(),
                            gamer2Dice.getSum(),
                            gamer3Dice.getSum())

for idx, item in enumerate(sortedNumbers):
    if idx == 0:
        print(f'{idx + 1}등: {item} WINNER!!')
    else:
        print(f'{idx + 1}등: {item}')


print(f'1등: {sortedNumbers[0]} WINNER!!')
print(f'1등: {sortedNumbers[1]}')
print(f'1등: {sortedNumbers[2]}')
