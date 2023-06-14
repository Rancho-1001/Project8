###########################################################

    #  Computer Project #08
    #
    #  Algorithm
    #           This program imports the csv file to be used, it also calls the operator function to import itemgetter. 
    #           
    #           The program reads data from multiple csv files 
    #           The program has 10 functions and 1 main function. 
    #           The docstrings for the various functions have been included in the functions. 
    #           The functions:
    #                          1. open_file(s)
    #                          2. read_file(fp_games)
    #                          3. read_discount(fp_discount)
    #                          4. in_year()
    #                          5. by_genre()
    #                          6. by_dev()
    #                          7. per_discount()
    #                          8. by_dev_year()
    #                          9. by_genre_no_disc() 
    #                         10. by_dev_with_disc()

    #           The main_function():
    #                  1. calls the open_file function twice to ask the user for a name of a file to open. One game file and one discount file. returns 
    #                  2. calls the read_file function to take in the file pointer from the game file and returns a dictionary. 
    #                  3. calls the read_discount function to take in the file pointer from the discount file and returns a dictionary. 
    #                  4. A while loop to keep taking the option from the user until the option is 7.
    #                       a. if option is 1:

    #                                         i. prompts the user to enter a year. If the year is not an integer keep prompting for a year.
    #                                         ii. Call the in_year function and pass the dictionary from the read file function with the year as arguments
    #                                         iii. Display all the games released that year sorted alphabetically
    #                                          
    #                       b.if option is 2:

    #                                       i. prompts the user to a enter a name of a developer 
    #                                       ii. call the by_dev function and pass the dictionary from the read_File function with the developer as arguments.
    #                                       iii. Display all games from the developer sorted from latest to oldest release year
    #                                       

    #                       c. if option is 3:
    #                                          
    #                                      i. prompts the user to enter a genre 
    #                                      ii.  call the by_genre function and pass the dictionary from the read_File function with the developer as arguments. 
    #                                      iii.  Display all games with the genre sorted by the percentage positive reviews in descending order 
    #                                      

    #                       d. if option is 4:

    #                                       i. prompts the user to enter a developer and then a year, if the year is not an integer, keep asking for a year.
    #                                      ii. call the by_dev_year function and pass on both dictionaries from the read file and read discounts together with the developer and year as arguments
    #                                      iii. Display all games that were made by the developer in the year sorted by increasing prices 
    #                                      

    #                       e. if option is 5:

    #                                        i. prompts the user to enter a genre 
    #                                      ii.  call the by_genre_no_disc function and pass the dictionaries from read file and read discount together with the genre as arguments
    #                                      iii.  Display all the games that have the genre and do not offer discount on their prices sorted from cheapest to most expensive.
    #                                      
    #
    #                       f. if option is 6:

    #                                       i. prompts the user to enter a developer 
    #                                      ii. call the by_dev_with_disc function and pass the dictionaries from both the read file and read discount functions and the developer as arguments. 
    #                                      iii. Display all games from the developer that do not offer discount sorted from cheapest to most expensive. 
    #                                     
    #                       g. if option is 7:
    #                                       i. print a goodbye message 
    #                                       ii. Quit the program 
    #
###########################################################################################################################################################################################################

import csv
from operator import itemgetter


MENU = '''\nSelect from the option: 
        1.Games in a certain year 
        2. Games by a Developer 
        3. Games of a Genre 
        4. Games by a developer in a year 
        5. Games of a Genre with no discount 
        6. Games by a developer with discount 
        7. Exit 
        Option: '''
        
def open_file(s):
    """
    Prompts the user for a file name and opens the file in read mode.
    Returns:
        A file object or pointer for the file. 
    Raises:
        FileNotFoundError: If the file cannot be found. 
    """
    while True:
        try:
            game_fname = input('\nEnter {} file: '.format(s))
            game_fp = open(game_fname, 'r', encoding='UTF-8')
            break
        except FileNotFoundError:
            print('\nNo Such file')
    
    return game_fp


def read_file(fp_games):
    """
    Reads a csv file and returns a dictionary of game data.
    Parameters:
    fp_games (file object): The csv file object to read.
    Returns:
    dict: A dictionary of game data, where each key is a game name and each value is a list of properties:
          - release_date (str): The release date of the game.
          - developers (list of str): The list of developers of the game.
          - genres (list of str): The list of genres of the game.
          - mode (int): The player mode of the game, where 0 is multiplayer and 1 is singleplayer.
          - price (float): The price of the game in dollars.
          - overall_reviews (str): The overall review rating of the game.
          - reviews (int): The number of reviews for the game.
          - percent_positive (int): The percentage of positive reviews for the game.
          - supports (list of str): The list of platforms the game supports, where each element is either 'win_support',
            'mac_support', or 'lin_support'.
    """

    # Convert the csv file object to a csv reader object
    fp_games = csv.reader(fp_games) 
    
    # Create an empty dictionary to store game data
    games_dict = {}
    
    # Skip the header row
    next(fp_games)
    
    # Iterate over each row in the csv file
    for row in fp_games:
        # Extract the values from the row
        name, release_date, developers, genres, player_modes, price, overall_reviews, reviews, percent_positive, win_support, mac_support, lin_support = row
        
        # Convert the developers and genres to lists
        developers = developers.split(';')
        genres = genres.split(';')
        
        # Extract the first player mode and convert to 0 if it's multiplayer, 1 otherwise
        mode = 0 if 'multi-player' in player_modes.lower().split(';')[0] else 1
        
        # Convert price to float and convert to dollars
        try:
            price = float(price.replace(',', '')) * 0.012
        except ValueError:
            price = 0.0
        
        # Convert reviews and percent_positive to integers
        reviews = int(reviews)
        percent_positive = int(percent_positive.strip('%'))
        
        # Create the list of supports
        supports = []
        if int(win_support) == 1:
            supports.append('win_support')
        if int(mac_support) == 1:
            supports.append('mac_support')
        if int(lin_support) == 1:
            supports.append('lin_support')
        
        # Add the values to the dictionary
        games_dict[name] = [release_date, developers, genres, mode, price, overall_reviews, reviews, percent_positive, supports]
    
    return games_dict

def read_discount(fp_discount):
    """
    Reads the discount data file using the provided file pointer and returns a dictionary
    with the name of the game as the key and the discount as the value rounded to 2 decimal places.
    Args:
    fp_discount: A file pointer to the discount data file.
    Returns:
    A dictionary with the name of the game as the key and the discount as the value rounded to 2 decimal places.
    """
    fp_discount = csv.reader(fp_discount)
    next(fp_discount)  # Skip header line

    # Create an empty dictionary
    discount_dict = {}

    # Iterate over each row in the csv file
    for row in fp_discount:
        game_name = row[0]
        discount = round(float(row[1]), 2)      #round the discount to two decimals 
        discount_dict[game_name] = discount

    return discount_dict


def in_year(master_D, year):
    """
    Returns a sorted list of game names that were released in a given year.
    Parameters:
        master_D (dict): A dictionary with game names as keys and a list of game details as values.
        year (int): The year to filter game releases by.
    Returns:
        A sorted list of game names released in the given year.
    """
    # Create an empty list
    game_list = []

    # Iterate through the key-value pair of the master_D using game-details as pair
    for game, details in master_D.items():
        release_date = details[0]
        if int(release_date[-4:]) == year:  # Look for all release dates with year same as the year parameter
            game_list.append(game)

    # Sort the list in place
    game_list.sort()

    return game_list


def by_genre(master_D, genre):
    """
    Filters out games of a specific genre from the main dictionary master_D and returns a sorted
    list of game names by percentage positive reviews in descending order. If there is a tie in the
    percentage positive reviews, keep the same order as in the dictionary.

    Args:
    - master_D (dictionary): a dictionary containing game names as keys and game attributes as values
    - genre (str): the genre to filter games by

    Returns:
    - sorted_games (list): a sorted list of game names that meet the filtering criteria
    """

    filtered_games = []  # create an empty list to store the list of filtered games from the dictionary

    # Loop through each game in the master dictionary
    for game_name, game_details in master_D.items():
        # Extract the percentage of positive reviews from the game's attributes
        percent_pos_reviews = game_details[7] 

        # Extract the list of genres from the game's attributes
        genres = game_details[2]
        # Check if the specified genre is in the list of genres for this game
        if genre in genres:
            # If so, add the game name and percentage of positive reviews to a list of filtered games
            filtered_games.append((game_name, percent_pos_reviews))
    
    # Sort the list of filtered games by percentage of positive reviews in descending order, then by the original order in the master dictionary
    sorted_games = sorted(filtered_games, key=itemgetter(1), reverse=True)

    # Extract just the game names from the sorted list and return them
    return [game[0] for game in sorted_games]


def by_dev(master_D, developer):
    """
    Filters out games made by a specific developer from the main dictionary master_D and returns a sorted
    list of game names from latest to oldest released games. If there is a tie in the release year, keep the same 
    order as in the dictionary.
    
    Args:
    - master_D (dictionary): a dictionary containing game names as keys and game attributes as values
    - developer (str): the name of the developer to filter games by
    
    Returns:
    - sorted_games (list): a sorted list of game names that meet the filtering criteria
    """
    
    filtered_games = []    #create an empty list to store the list of filtered games from the dictionary 
    
    # Loop through each game in the master dictionary
    for game_name, game_details in master_D.items():
        # Extract the release year from the game's attributes
        release_year = int(game_details[0].split('/')[-1])
        # Extract the list of developers from the game's attributes
        developers = game_details[1]
        # Check if the specified developer is in the list of developers for this game
        if developer in developers:
            # If so, add the game name and release year to a list of filtered games
            filtered_games.append((game_name, release_year))

    # Sort the list of filtered games first by release year, then by the original order in the master dictionary
    sorted_games = sorted(filtered_games, key=itemgetter(1), reverse=True)

    # Extract just the game names from the sorted list and return them
    return [game[0] for game in sorted_games]


def per_discount(master_D, games, discount_D):
    """
    Calculate the discounted prices for a given list of games using the master dictionary and the discount dictionary.
    Parameters:
        master_D (dict): A dictionary with the name of the game as the key and a list containing its details as the value.
        games (list): A list of game names.
        discount_D (dict): A dictionary with the name of the game as the key and the discount as the value.
    Returns:
        result (list): A list of discounted prices for the given list of games, rounded to 6 decimal places.
    """
    result = []                                     # create an empty list to store discounted prices
    for game in games:                              # iterate over the list of game names
        if game in master_D:                        # check if the game exists in the master dictionary
            price = master_D[game][4]               # retrieve the original price of the game
            if game in discount_D:                  # check if the game has a discount
                discount = discount_D[game]         # retrieve the discount percentage
                price *= (100 - discount) / 100     # apply the discount to the price
            result.append(round(price, 6))          # add the discounted price to the result list, rounded to 6 decimal places
    
    return result                                   # return the list of discounted prices


def by_dev_year(master_D, discount_D, developer, year):
    """
    Returns a list of game names filtered by the given developer and release year, sorted by discounted price and game name.
    Args:
    - master_D (dict): A dictionary of game details with game names as keys
    - discount_D (dict): A dictionary of game discounts with game names as keys
    - developer (str): The name of the developer to filter by
    - year (int): The release year to filter by
    Returns:
    - A list of game names sorted by discounted price and game name
    """
    # filter games by developer and release year 
    filtered_games = [game for game in master_D.items() if developer in game[1][1] and int(game[1][0][-4:]) == year]

    # calculate the discounted price of each game and create a list of tuples containing game name and discounted price
    games_with_discount = [(game[0], game[1][4] * (1 - discount_D.get(game[0], 0) / 100)) for game in filtered_games]

    # sort the list of tuples by discounted price, then by game name 
    sorted_games = sorted(games_with_discount, key=itemgetter(1, 0))

    # return a list of game names sorted by discounted price and game name 
    return [game[0] for game in sorted_games]


def by_genre_no_disc(master_D, discount_D, genre):
    """
    Filters out games by a specific genre that do not offer a discount on their price. It returns
    a list of game names sorted from cheapest to most expensive. If there is a tie, it should be sorted by the
    percentage positive reviews in descending order.

    Args:
    - master_D (dictionary): a dictionary containing game names as keys and game attributes as values
    - discount_D (dictionary): a dictionary containing game names as keys and their discounted prices as values
    - genre (str): the genre to filter games by

    Returns:
    - sorted_games (list): a sorted list of game names that meet the filtering criteria
    """
    # Filter out games of the specified genre using the by_genre function
    games_by_genre = by_genre(master_D, genre)

    # Filter out the games that have a discount
    games_no_disc = []
    for game_name in games_by_genre:
        price = master_D[game_name][4]
        percent_pos_review = master_D[game_name][7]
        if game_name not in discount_D:
            games_no_disc.append((game_name, float(price), percent_pos_review))

    # Sort the list of games by the percentage of positive reviews in descending order, and then by price in ascending order 
    sorted_games = sorted(games_no_disc, key=itemgetter(2), reverse=True)
    sorted_games1 = sorted(sorted_games, key=itemgetter(1)) 

    # Extract just the game names from the sorted list and return them
    return [game[0] for game in sorted_games1]


def by_dev_with_disc(master_D, discount_D, developer):
    """
    Filters out games by a specific developer and offers discounts. The function should return a list 
    of game names sorted from cheapest to most expensive. The original price (not the discounted price) 
    should be considered when sorting. If there is a tie, sort from latest to oldest released games. 
    If there is a tie in the release year, keep the same order as in the dictionary.
    
    Args:
    - master_D (dictionary): a dictionary containing game names as keys and game attributes as values
    - discount_D (dictionary): a dictionary containing game names as keys and discount percentages as values
    - developer (str): the name of the developer to filter games by
    
    Returns:
    - sorted_games (list): a sorted list of game names that meet the filtering and discount criteria
    """
    
    filtered_games = []    #create an empty list to store the list of filtered games from the dictionary 
    
    # Loop through each game in the master dictionary
    for game_name, game_details in master_D.items():
        # Extract the release year from the game's attributes
        release_year = int(game_details[0].split('/')[-1])

        # Extract the list of developers from the game's attributes
        developers = game_details[1]

        # Extract the prices from the game's attributes 
        prices = game_details[4]

        # Check if the specified developer is in the list of developers for this game and if the game is discounted
        if developer in developers and game_name in discount_D:
            # If so, add the game name, release year, and original price to a list of filtered games
            filtered_games.append((game_name, release_year, prices))  
            
    # Sort the list of filtered games first by original price,
    # then by release year, and then by the original order in the master dictionary
    sorted_games = sorted(filtered_games, key=itemgetter(2, 1, 0), reverse=False)
    
    # Extract just the game names from the sorted list and return them
    return [game[0] for game in sorted_games]

             
def main():

    fp_games= open_file("games")
    fp_discount = open_file("discount")
    master_D = read_file(fp_games)
    discount_D = read_discount(fp_discount) 
      
    while True:

        # Get user input and handle invalid input
        try:
            options = int(input(MENU))
            if options not in range(1, 8):
                raise ValueError
                break
        except ValueError:
            print("\nInvalid option")
            continue
        
        #if option is 7 print goodbye message and quit 
        if options == 7:
            print("\nThank you." )
            break 

        #elif option is 1, prompt the user for a year until a correct year is received.
        elif options == 1:
            while True:
                year = input('\nWhich year: ')
                try:
                    year = int(year)
                    game_display = in_year(master_D, year)  #call the in_year function to receive a list of values
                    if game_display:
                        printed_games = ", ".join(game_display)
                        print("\nGames released in {}:".format(year))
                        print(printed_games)                #print out the values, comma-separated 

                    else:
                        print("\nNothing to print")         #if there is no value to print 

                    break  # break out of the loop if a valid year is entered

                except ValueError:
                    print("\nPlease enter a valid year")
                    continue 
    
        #if option is 2, ask the user for a developer's name             
        elif options == 2:
            developer = input('\nWhich developer: ')
            game_display = by_dev(master_D, developer)  #call the by dev function to get the list of values 
            if game_display:
                printed_games = ", ".join(game_display)
                print("\nGames made by {}:".format(developer))
                print(printed_games)                    #print out the values, comma-separated 

            else:
                print("\nNothing to print")             #if there is no value to print 

        #if option is 3, ask the user for genre 
        elif options == 3:
            genre = input('\nWhich genre: ')
            game_display = by_genre(master_D,genre)  #call the by_genre function to get the list of values 
            if game_display:
                printed_games = ", ".join(game_display)
                print("\nGames with {} genre:".format(genre))
                print(printed_games)                  #print out the values, comma-separated 

            else:
                print("\nNothing to print")             #if there is no value to print 

        #if option is 4, ask the user for a name of a developer and a year
        #if the year is not a valid year, repeatedly ask the user for a valid year 
        elif options == 4:
            developer = input('\nWhich developer: ')  
            year = input('\nWhich year: ')
            while True:
                try:
                    year = int(year)
                    game_display = by_dev_year(master_D, discount_D, developer, year) #call the by_dev_year function to get the list of values
                    if game_display:
                        printed_games = ", ".join(game_display)
                        print("\nGames made by {} and released in {}:".format(developer,year)) 
                        print(printed_games)                                           #print out the values, comma-separated 
                    else:
                        print("\nNothing to print")                                    #if there is no value to print 
                    break                  
                except ValueError:
                    print("\nPlease enter a valid year")
                    continue 

        #if option is 5, ask the user for a genre 
        elif options == 5:
            genre = input('\nWhich genre: ')
            game_display = by_genre_no_disc(master_D, discount_D, genre)  #call the by_gen_no_disc function to receive a list of values
            if game_display:
                printed_games = ", ".join(game_display)
                print("\nGames with {} genre and without a discount:".format(genre))
                print(printed_games)                                        #print out the values, comma-separated 

            else:
                print("\nNothing to print")                                 #if there is no value to print

        #if option is 6, ask the user for a developer's name 
        elif options == 6:
            developer = input('\nWhich developer: ')
            game_display = by_dev_with_disc(master_D, discount_D, developer) #call the by_dev_with_disc function to receive a list of values 
            if game_display:
                printed_games = ", ".join(game_display)
                print("\nGames made by {} which offer discount:".format(developer))
                print(printed_games)                                          #print out the values, comma-separated 

            else:
                print("\nNothing to print")                                   #if there is no value to print


if __name__ == "__main__":
    main()

