import random


def get_response(message: str) -> str:
    p_message = message.lower()
    
    if p_message == 'hello':
        return 'Hello!'
    if p_message == 'roll':
        dice = random.randint(1,6)
        return str(":game_die: The dice rolled a "+str(dice)+"!")
    if p_message == '!help':
        return "`This is a help message that you can modify.`"
    if p_message == 'flip a coin':
        coin = random.randint(1,2)
        if coin == 1:
            return ":coin: It's Heads!"
        else:
            return ":coin: It's Tails!"

    