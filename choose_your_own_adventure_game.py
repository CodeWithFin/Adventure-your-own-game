name = input("Type your name: ")
print("Welcome", name, "to this adventure!")


answer = input("You wake up in a walled city surrounded by massive walls, a place where humanity seeks refuge from the Titans. What do you do(Investigate your surroundings|Head to the training grounds|Visit the market place for supplies|quit)? ").lower()
if answer == "investigate your surroundings":
    print("You decide to investigate your surroundings")
    answer = input(
        "While investigating, you stumble upon a hidden passage. Do you enter(Yes| No)? ").lower()
    if answer == "yes":
        answer = input(
            "Your investigation leads you to discover a suspicious character. What do you do(approach and question|keep distance)? ").lower()
        if answer == "approach and question":
            print("The person takes out a knife and stubs you to death")
            quit()
        else:
            print("The person runs and you later discover that he is titan")
            quit()
    else:
        print("You eventually become a resident and later on the wall is breached and you are killed")
        quit()
elif answer == "head to the training grounds":
    answer = input(
        "At the training grounds, you meet Armin, Mikasa, and Eren. They invite you to join their squad. Do you accept(yes|no) ?").lower()
    if answer == "yes":
        answer = input(
            "During training, you become close friends with Eren. What role do you take on during your training days(train as a soldier| specialize in 3d MG)?").lower()
        if answer == "Train as a Soldier":
            answer = input(
                "What skills are you focused on  mastering(Combat skills| Survival and invasion skills)? ").lower()

elif answer == "visit the market place for supplies":
    pass
else:
    print("You lose !sorry")
