import random

mood = 1.0


def mood_refresh():
    global mood
    mood = 0.5


def mood_change(change):
    global mood
    mood += change


def mood_randomise(degree):
    global mood
    mood_change(random.randint(-degree, degree) / 100)

def mood_change_random(change, degree):
    global mood
    mood_change(change)
    mood_randomise(degree)


def irritated():
    global mood
    mood_change(-0.01)


def mood_check():
    global mood
    if mood>1: return 2
    if mood<0: return 1
    else: return 0


def decision(mood_value):
    if mood_value > 1.5: return good_answer(random.randint(0,2))
    if mood_value > 0: return neutral_answer(random.randint(0, 2))
    else: return bad_answer(random.randint(0, 2))


def good_answer(number):
    if number == 0: return "Well done! I think you're ready"
    if number == 1: return "You're the best of the best of the best! I like your work"
    if number == 2: return "I'm gonna make this work for you!"


def neutral_answer(number):
    if number == 0: return "Keep going! Not ready yet"
    if number == 1: return "That's not all. Continue your reserch"
    if number == 2: return "Come next week. You're not ready yet"


def bad_answer(number):
    if number == 0: return "I suppose I shouldn't say that. But you're a moron"
    if number == 1: return "Get out and never come back. I hate you"
    if number == 2: return "You're ^($%!*# %&^ ^( &%# %(*@#! Understood?"