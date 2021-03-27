from random import randint
import re

def check(dice):
    dice_type_allowed = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    result = False
    for kosc in dice_type_allowed:                                  # dice type exist
        if kosc in dice:
            dice_type = re.split('[D+-]', dice)
            if len(dice_type[1]) > 0 and len(dice_type[1]) <= 3:
                if dice_type[0] != "":                              # multipler is int
                    multipl = dice.find("D")
                    multipl = dice[:multipl]
                    try:
                        int(multipl)
                    except:
                        result = False
                        return result
                if "+" in dice:
                    d = dice.find("D")
                    modi = dice[d+1:]
                    modi = modi.replace("+", "0")
                    try:
                        int(modi)
                        result = True
                        return result
                    except:
                        result = False
                        return result
                if "-" in dice:
                    d = dice.find("D")
                    modi = dice[d+1:]
                    modi = modi.replace("-", "0")
                    try:
                        int(modi)
                        result = True
                        return result
                    except:
                        result = False
                        return result
            result = True
            return result
    return result


def roll(input_roll):
    result = 0
    if check(input_roll) == True:
        dice_roll = re.split('[D+-]', input_roll)
        if dice_roll[0] == "":
            dice_roll[0] = "1"
        roll_multiplier = int(dice_roll[0])
        for i in range(roll_multiplier):
            result += randint(1, int(dice_roll[1]))
        if "-" in input_roll:
            result -= int(dice_roll[2])
        if "+" in input_roll:
            result += int(dice_roll[2])
        return result
    else:
        return "Wrong dice"
