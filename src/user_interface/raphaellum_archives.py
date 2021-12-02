import pickle
from time import sleep
from src.models.band import Band, BandGenreEnum, BandMember
from src.actions.add_new_band import add_new_band
from src.actions.add_band_member import add_band_member
from src.actions.delete_band import delete_band
from src.actions.list_all_bands import list_all_bands
from src.actions.search_band_by_name import fetch_band_by_name

with open("bandslist.pickle", "rb") as bandslist:
    bands_list: list[Band] = pickle.load(bandslist)


def main():
    welcome_message = "Welcome to Raphaellum Archives!\nWhat do you want to do?\n"
    user_options = "(1) - Add new band\n" \
                   "(2) - Delete existing band\n" \
                   "(3) - List all bands\n" \
                   "(4) - Search band by name\n" \
                   "(5) - Quit\n"

    print(welcome_message)
    print(user_options)
    user_input = input("-> ")

    if user_input == "1":
        new_band_name = input("Band Name: ")
        new_band_genre = input("Band Genre (Rock, Pagode or Arrocha): ")
        if new_band_genre == "Rock":
            new_band_genre = BandGenreEnum.ROCK
        elif new_band_genre == "Pagode":
            new_band_genre = BandGenreEnum.PAGODE
        elif new_band_genre == "Arrocha":
            new_band_genre = BandGenreEnum.ARROCHA
        else:
            print("Invalid input.\n Try again.\n"
                  "Loading main menu...")
            sleep(1)
            main()
        new_band_members: list[BandMember] = []
        add_members = True
        while add_members:
            band_member_name: str = input("Band member's Name: ")
            band_member_instrument: str = input("Band member's instrument: ")
            add_band_member(band_member_name, band_member_instrument, new_band_members)
            add_another_member = input("Add another member to the band?(y) (n)\n-> ")
            if add_another_member == "n":
                add_members = False
        add_new_band(new_band_name, new_band_genre, new_band_members, bands_list)
        print(f"{new_band_name} successfully added to Raphaellum Archives!\n")

        main()

    elif user_input == "2":

        band_to_delete = input("Name the band you want to delete: ")
        i = 0
        for band in bands_list:
            if band.name == band_to_delete:
                i += 1

        if i == 0:
            print(f"{band_to_delete} was not found in Raphaellum Archives.\n")
            main()

        print(f"Are you sure you want to delete {band_to_delete}?\n"
              f"This action is irreversible.\n")

        user_confirmation = input("(y) (n)\n> ")

        if user_confirmation == "y":
            print(f"Deleting {band_to_delete}...")
            delete_band(band_to_delete, bands_list)
        main()

    elif user_input == "3":
        print("Bands in Raphaellum Archives:\n")
        list_all_bands(bands_list)
        sleep(1)
        main()

    elif user_input == "4":
        searched_band = input("What band are you searching for?\n> ")
        resulting_list = fetch_band_by_name(searched_band, bands_list)
        for band in resulting_list:
            print(band)
        main()

    elif user_input == "5":
        with open("bandslist.pickle", "wb") as newbandslist:
            pickle.dump(bands_list, newbandslist)
        exit(666)

    else:
        print("Invalid command.\n"
              "Returning to main menu...")
        sleep(1)
        main()


main()
