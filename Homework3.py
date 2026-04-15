"""
CS 230 Fall 2025
Program 3 Starter File
Sanjana Sathiyavanthan
This is Homework 3 which is a program reads member data from a file (members.txt) and then prints mailing labels based on what the user picks
"""

# Constants
MEMBER_DATA = "members.txt"
SEPARATOR = 30 * "="


# This will get all the user choices for how the labels should look.
def get_options():
    # ask user how they want the labels formatted
    case = input("[T]itle or [U]pper Case (ENTER for [T]): ").strip().upper()
    if case == "":
        case = "T"

    name_format = input("[F]irst name or [I]nitial (ENTER for [F]): ").strip().upper()
    if name_format == "":
        name_format = "F"

    address_format = input("[A]bbreviated or [E]xpanded Address (ENTER for [A]): ").strip().upper()
    if address_format == "":
        address_format = "A"

    label_type = input("Which labels? [B]ronze, [S]ilver, [G]old or (ENTER for [A]ll): ").strip().upper()
    if label_type == "":
        label_type = "A"

    # return the user choices as a list
    return [case, name_format, address_format, label_type]


def expand(address): # expands the street abbreviations using a match-case function
    words = address.split()
    last_word = words[-1]

    match last_word:
        case "St":
            words[-1] = "Street"
        case "Ave":
            words[-1] = "Avenue"
        case "Ln":
            words[-1] = "Lane"
        case "Rd":
            words[-1] = "Road"
        case "Way":
            words[-1] = "Way"
        case "Dr":
            words[-1] = "Drive"
        case "Ct":
            words[-1] = "Court"
        case _:
            pass  # this will do nothing if no match

    # puts the words back together into one string
    address = " ".join(words)
    return address


def parse(line): # split the line into different parts
    parts = line.split(",")

    name = parts[0]
    address = parts[1]
    city = parts[2]
    state = parts[3]
    zip_code = parts[4]
    email = parts[5]
    mtype = parts[6]

    # checks if the address includes apt in the address
    apt = ""
    if "Apt" in address:
        address_parts = address.split("Apt")
        address = address_parts[0].strip()
        apt = "Apt" + address_parts[1].strip()

    return name, address, apt, city, state, zip_code, mtype


# Prints one mailing label using the user's choices
def print_label(label, styles):
    # takes data from the lists and breaks it down
    name, addr, apt, city, state, zip_code, mtype = label
    case, name_format, address_format, label_type = styles

    # converts the differents cases
    if case == "U":
        name = name.upper()
        addr = addr.upper()
        apt = apt.upper()
        city = city.upper()
        state = state.upper()
    else:
        name = name.title()
        addr = addr.title()
        apt = apt.title()
        city = city.title()

    # expands the address if the user wants too
    if address_format == "E":
        addr = expand(addr)

    # change to initials if the user wants
    if name_format == "I":
        name_parts = name.split()
        last_name = name_parts[-1]
        initials = ""
        for part in name_parts[:-1]:
            initials += part[0].upper() + ". "
        name = initials + last_name.title()

    # this will print the label
    print()
    print(name)
    print(addr)
    if apt != "":
        print(apt)
        print(city + ", " + state + " " + zip_code)
    else:
        print(city + ", " + state + " " + zip_code)
        print(SEPARATOR)


#  This section print all the members for this grou (gold/silver/bronze).
def print_members(title, members_list):
    # print the category and names in that group
    print("\n" + title + " Members:")
    for member in members_list:
        print("\t" + member)


#This is the actual program
def main():
    print("Welcome to the Label Maker")

    # get the options from the user
    options = get_options()

    # open the file and skip the header
    f = open(MEMBER_DATA, "r")
    f.readline()
    lines = f.read().split("\n")
    f.close()

    # lists for the different members
    labels = []

    gold = []
    silver = []
    bronze = []


    for line in lines:
        if line.strip() == "":
            continue

        name, addr, apt, city, state, zip_code, mtype = parse(line)

        # sorts the different members into different groups
        match mtype:
            case "Gold":
                gold.append(name)
            case "Silver":
                silver.append(name)
            case "Bronze":
                bronze.append(name)

        # shows which of the different labels to print
        if options[3] == "A" or options[3][0] == mtype[0].upper():
            labels.append([name, addr, apt, city, state, zip_code, mtype])
            print_label([name, addr, apt, city, state, zip_code, mtype], options)

    #print the labels
    print(f"\n{len(labels)} labels printed.")

    #prints the grouped member lists
    print_members("Gold", gold)
    print_members("Silver", silver)
    print_members("Bronze", bronze)


if __name__ == "__main__":
    main()
