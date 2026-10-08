def main():
    time = input("What time it is? ").strip()
    normalized_format = check_format(time)

    if 7.0 <= normalized_format <= 8.0:
        print("breakfast time") 
    elif 12.0 <= normalized_format <= 13.0:
        print("lunch time")
    elif 18.0 <= normalized_format <= 19.0:
        print("dinner time")
    
  
def check_format(time):

    if time.endswith("a.m."):
        clear_am = time.replace("a.m.","")
        time = convert(clear_am)
        if 12 <= time < 12.99:
            time = time - 12
        return time
    
    elif time.endswith("p.m."):
        clear_pm = time.replace("p.m.","")
        time = convert(clear_pm)
        if not (12 <= time < 12.99):
            time = time + 12
        return time
    
    else:
        return convert(time) 
    
 
def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + (minutes / 60)


if __name__ == "__main__":
    main()

#I fucking did it Mia, your first problem set in minutes or hours. I'm so proud of you.