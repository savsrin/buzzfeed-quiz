
def return_instructor(drink, food, coding): 
    print("entering model")

    instructors = {"Aaron": 0, "Nouran": 0, "Elissa": 0}

    if drink == "boba":
        instructors["Aaron"] += 1
    elif drink == "tea":
        instructors["Elissa"] += 1
    elif drink == "coffee":
        instructors["Nouran"] += 1

    
    if food == "!sashimi":
        instructors["Aaron"] += 1
    elif food == "gymmy bears":
        instructors["Elissa"] += 1
    elif food == "waffles":
        instructors["Nouran"] += 1

    if coding == "yes" and instructors["Aaron"] > 0:
        instructors["Aaron"] += 100
        instructors["Elissa"] -= 100
        instructors["Nouran"] -= 100
    elif coding == "yes" and instructors["Aaron"] == 0:
        return "LIAR, you not coding god!!!!"
    elif coding == "no" and instructors["Aaron"] > 0:
        return "Aaron, you don't need to be humble."
    elif coding == "no" and instructors["Nouran"] > 0:
        return "-1"
    elif coding == "no" and instructors["Elissa"] > 0:
        return "Sorry Elissa, there's only one coding god: Aaron."
         

    max_count = ["", -100]
    keys = instructors.keys()
    for i in keys: 
        if instructors[i] > max_count[1]:
            max_count[0] = i
            max_count[1] = instructors[i]
    print(max_count)
    return max_count[0]
    
    

    

         




   


