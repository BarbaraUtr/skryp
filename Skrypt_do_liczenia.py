from pathlib import Path
from os import path
from io import FileIO


def path_to_new(path1, string1):
    new_name = str(path1) + string1
    new_file = Path(new_name)
    return new_file


p = Path(".")
main_directory = Path('C:/Users/utrac/problemset')  # change to where the file is
# main_directory = Path('C:/Users/utrac/Desktop/SAT_check/Zadania')

for x in main_directory.iterdir():
    if x.is_dir():
        group = x.name
        print(x.name)

        for y in x.iterdir():
            if y.is_dir():
                skill = y.name

                licznik = 0

                for z in y.iterdir():
                    licznik += 1
                    folder = z.stem
                    problem = z.name

                print(licznik, end=": ")
                print(' ', y.name)
