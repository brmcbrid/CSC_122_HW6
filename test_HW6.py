# Tests for Lab6
# Movie Ranking Program

import os.path
import sys
from HW6 import main
from tud_tests import *

def test_HW6():

    try:
        exists = os.path.exists("HW6.py")
        assert exists == True
    except:
        sys.exit()

    # Test 1
    set_keyboard_input(['y','4','1','n'])
    main()
    output = get_display_output()

    assert output == [
        "\n The Movie Ranking Program\n---------------------------",
        " 1 - The Incredibles",
        " 2 - Monsters Inc.",
        " 3 - Toy Story",
        " 4 - Cars",
        " 5 - Finding Nemo",
        "\nDo you want to change any rankings (y/n): ",
        "Enter the current ranking of a movie: ",
        "Enter the new ranking of that movie: ",
        "\n The Movie Ranking Program\n---------------------------",
        " 1 - Cars",
        " 2 - The Incredibles",
        " 3 - Monsters Inc.",
        " 4 - Toy Story",
        " 5 - Finding Nemo",
        "\nDo you want to change any rankings (y/n): ",
        "\nThe file 'movie_data.txt' has been updated",
        "Thanks for using the Movie Ranking Program!"
        ]
