#Meal time
# ask time -> breakfast/lunch/dinner / anything

def main():
    time = input("What time it is? ")
    twenty_four = convert(time)
    check_meal_time(twenty_four)


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + (minutes / 60)

def check_meal_time(twenty_four):
    if  7.0 <= twenty_four <= 8.0:
        print("breakfast time") 
    elif 12.0 <= twenty_four <= 13.0:
        print("lunch time")
    elif 18.0 <= twenty_four <= 19.0:
        print("dinner time")

if __name__ == "__main__":

    main()