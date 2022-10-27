from pathlib import Path
from os import path


def path_to_new(path1, string1):
    new_name = str(path1) + string1
    new_file = Path(new_name)
    return new_file


p = Path(".")
main_directory = Path('C:/Users/utrac/Desktop/SAT_check')

for x in p.iterdir():
    if x.is_dir():
        group = x.name
        print(x.name)

        for y in x.iterdir():
            if y.is_dir():
                skill = y.name
                print(' ', y.name)

                licznik = 0

                for z in y.iterdir():
                    licznik += 1

                    folder = z.stem
                    problem = z.name

                    with open(z) as file:
                        lines = file.readlines()

                    new_directory = main_directory / y / folder

                    if not new_directory.exists():
                        new_directory.mkdir(parents=True)

                    f_question = open(new_directory / path_to_new(folder, '.question.md'), "w")
                    f_answer1 = open(new_directory / path_to_new(folder, '.answer1.md'), "w")
                    f_answer2 = open(new_directory / path_to_new(folder, '.answer2.md'), "w")
                    f_answer3 = open(new_directory / path_to_new(folder, '.answer3.md'), "w")
                    f_answer4 = open(new_directory / path_to_new(folder, '.answer4.md'), "w")
                    f_correct = open(new_directory / path_to_new(folder, '.correct.txt'), "w")
                    f_isCalc = open(new_directory / path_to_new(folder, '.calculator.txt'), "w")

                    tak = False
                    i = 0

                    for line in lines:
                        if '@' in line:
                            tak = True
                            break
                        f_question.write(line)
                        i += 1

                    if tak:
                        f_answer1.write(lines[i + 1])
                        f_answer2.write(lines[i + 2])
                        f_answer3.write(lines[i + 3])
                        f_answer4.write(lines[i + 4])
                        f_correct.write(lines[i + 5])
                        f_isCalc.write(lines[i + 6])

                    f_answer1.close()
                    f_answer2.close()
                    f_answer3.close()
                    f_answer4.close()
                    f_correct.close()
                    f_isCalc.close()
                print(" ", licznik)
