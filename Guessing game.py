import random

def play_game():
    print("Wlecome to 'Press The Rigth key Game!'")
    print("Press the correct key. You get only one try! ")

    #choose a random correct key
    correct_key = random.choice(['a','b','c','d','e'])

    #Show options to player 
    print(f"Guess which key is correct: a, b, c, d, or e?")

    #Get the players input(o(1) time)
    