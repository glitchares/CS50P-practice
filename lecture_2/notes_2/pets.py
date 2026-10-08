def main():
    pets = [
        {"name": "Olivia", "animal": "dog",  "age": 16},
        {"name": "Jacinta", "animal": "cat", "age": 12},
        {"name": "Marulina", "animal": "hen", "age": 7},
        {"name": "Tortu", "animal": "turtle", "age": 101}

    ]

    dog_counter = 0
    for pet in pets:
        print(pet["name"], pet["animal"], pet["age"] , sep=", ")

        if pet["animal"] == "dog":
            dog_counter += 1

    if dog_counter == 1:
        print(f"There is {dog_counter} dog in the list. ")
    else: 
        print(f"There are {dog_counter} dogs in the list. ")

main()