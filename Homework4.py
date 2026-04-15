"""
CS 230 Fall 2025
Program 4 Starter File
Sanjana Sathiyavanthan
This is Program 4 which is a program that reads Jeopardy episode data from a file (jeopardata.txt) and lets the user pick different options to see players by date, count the game types, find the multi-day winners, and will show Tournament of Champions qualifiers.
"""

def read_jeopardy_data(FILENAME):
    games = []   #here is the list of game dictionaries

    # this will open the files
    try:
        f = open(FILENAME, "r")
    except:
        print("Error reading file.")
        return []

    for line in f:
        line = line.strip()
        if line == "":
            continue

        parts = line.split("\t")

        # handles the different lines
        if len(parts) == 3:
            info = parts[0]
            players = parts[1]
            comment = parts[2]
        else:
            info = parts[0]
            players = parts[1]
            comment = ""

        # changes the air date from the info field
        info_parts = info.split("aired")
        if len(info_parts) > 1:
            air_date = info_parts[1].strip()
        else:
            air_date = ""

        player_list = players.split(" vs. ")

        # this will build the dictionary for this game
        game = {
            "air_date": air_date,
            "players": player_list,
            "comment": comment
        }

        games.append(game)

    f.close()
    return games


def regular_game(game):

    comment = game["comment"].lower()

    keywords = ["tournament", "competition", "wildcard",
                "invitational", "exhibition"]

    #I am using list comprehension in regular game #[LISTCOMP]
    specials_found = [word for word in keywords if word in comment]

    # if there are no special words then it will just be a regular game
    return len(specials_found) == 0


def get_games_by_type(games_data):  #counts how many games are in each type

    # these names match the assignment categories
    counts = {
        "Regular Season": 0,
        "Tournament of Champions": 0,
        "Second Chance": 0,
        "Champions Wildcard": 0,
        "Invitational": 0,
        "Exhibition Games": 0
    }

    for game in games_data:
        comment = game["comment"].lower()

        if regular_game(game):
            counts["Regular Season"] += 1
        else:
            # Checks for each special type in the comment
            if "second chance" in comment:
                counts["Second Chance"] += 1
            elif "wildcard" in comment:
                counts["Champions Wildcard"] += 1
            elif "tournament of champions" in comment or "champions" in comment:
                counts["Tournament of Champions"] += 1
            elif "invitational" in comment:
                counts["Invitational"] += 1
            elif "exhibition" in comment:
                counts["Exhibition Games"] += 1
            else:
                # if it is special but doesn't match, put it as Tournament of Champions
                counts["Tournament of Champions"] += 1

    print("\nGame Type Counts:")
    for key, value in counts.items(): #[DOTITEMS]
        print(f"{key:25s}: {value}")

    return counts


def get_players_by_date(games_data):

    players_by_date = {} #[RETURNDICT]

    for game in games_data:
        date = game["air_date"]
        players_by_date[date] = game["players"]

    return players_by_date #[RETURNDICT]


def display_players_by_date(players_by_date): #This will not change
    date = input("Enter an air date (YYYY-MM-DD) or press ENTER to stop: ")
    while date != "":
        if date in players_by_date:
            print(f"\nPlayers on {date}:")
            for player in players_by_date[date]:
                print(f"- {player}")
        else:
            print(f"\nNo players found for {date}.")
        date = input("Enter an air date (YYYY-MM-DD) or press ENTER to stop: ")


def multi_day_regular_winners(games_data):

    winners = {} # key is the player name and value is the number of wins

    # here we count wins by using the first player (returning champion) in regular games
    for game in games_data:
        if regular_game(game):   #This is so only regular games count
            name = game["players"][0]
            if name not in winners:
                winners[name] = 0
            winners[name] += 1

    # this now group it into dictionary of lists and the key is the number of wins, and the  value is the list of players with that many wins
    grouped = {}

    # we will also build a list of tuples [TUPLES]
    win_tuples = [] #[TUPLES]

    for name in winners.keys():
        wins = winners[name]
        if wins >= 2:
            win_tuples.append((wins, name))  #[TUPLES]

    # sort tuples from highest wins to lowest
    win_tuples.sort(reverse=True)

    for wins, name in win_tuples:
        if wins not in grouped:
            grouped[wins] = [name]
        else:
            grouped[wins].append(name)

    print("\nMulti-Day Regular Game Winners (Highest to Lowest):")
    for wins in sorted(grouped.keys(), reverse=True):
        print(f"\n{wins} games won:")
        for player in grouped[wins]:
            print(f"- {player}")

    return grouped


def tournament_of_champions_qualifiers(multi_day_winners):

    qualifiers = {}

    for wins, players in multi_day_winners.items(): #[DOTITEMS]
        if wins >= 5:
            for player in players:
                qualifiers[player] = wins

    print("\nTournament of Champions Qualifiers:")
    for name, wins in qualifiers.items():#[DOTITEMS]
        print(f"{name} ({wins} wins)")

    return qualifiers #This function will return the different names and wins.


def main():
    FILENAME = "jeopardata.txt"
    games_data = read_jeopardy_data(FILENAME)

    if games_data == []:
        return

    quit = False
    while not quit:
        print("\n--- This is Jeopardata! ---")
        print("1. Players By Date")
        print("2. Get Games Count By Type")
        print("3. Multi-Day Regular Game Winners (Highest to Lowest)")
        print("4. Tournament of Champions Qualifiers")
        print("X. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            players_by_date = get_players_by_date(games_data)
            display_players_by_date(players_by_date)

        elif choice == "2":
            get_games_by_type(games_data)

        elif choice == "3":
            multi_day_regular_winners(games_data)

        elif choice == "4":
            winners = multi_day_regular_winners(games_data)
            tournament_of_champions_qualifiers(winners)

        elif choice == "X" or choice == "x":
            print("Exiting program. Goodbye!")
            quit = True

        else:
            print("Invalid choice. Please enter 1—4 or X.")


if __name__ == "__main__":
    main()
