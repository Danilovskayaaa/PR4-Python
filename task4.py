filenames = input("Введите имена файлов через пробел: ").split()
ofilename = "data_join.txt"

with open(ofilename, 'w') as ofile:
    for file in filenames:
        with open(file, 'r') as ifile:
            ofile.writelines(ifile.readlines())