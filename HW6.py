def main():
    movies = read_movie_file()  # call a function to read content of movie_data.txt into the list movies
    display_rankings(movies)  # call a function to print the content of the movie list to the screen
    choice = get_choice()  # call a function to ask user if they want to make any changes to the rankings
    while choice.lower() == 'y':
        current_rank, new_rank = get_ranking_change(movies) # call a function to collect users inputs to change the ranking of a movie
        change_ranking(movies,current_rank,new_rank)  # call a function to make the change to the movie list with users inputs
        display_rankings(movies)  # call a function to print the content of the movie list to the screen
        choice = get_choice()  # call a function to ask user if they want to make any changes to the rankings
    write_movie_file(movies)  # call a function to write the new movie rankings list to persistent memory file movie_data.txt
    print(f"\nThe file 'movie_data.txt' has been updated")  # notify the user that the file has been updated
    print(f"Thanks for using the Movie Ranking Program!")  # parting thank you message

# Your implementation of the required functions goes below here



if __name__ == '__main__':
    main()

