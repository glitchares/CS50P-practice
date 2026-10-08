def main():
    dwarves = ["Gnomes", "Fairies", "Wizards", "Witches", "Nymphs", "Trolls", "Ogres"]

    name_counter = 0
    for dwarf in dwarves:
        print(dwarf, f"({len(dwarf)})")
        name_counter += 1

    print(f"Total number of names: {name_counter}")

main()