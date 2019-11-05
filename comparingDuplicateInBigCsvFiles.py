def getDuplicateRowsFromCsv(file1,file2,fileToSave):
    """
    This function takes two CSV file names, reads them and looks for duplicate
    data between them. So, it opens a new file to save the duplicate data.
    """
    print("Getting duplicate data from files.")
    #opening files for reading
    file_1 = open(file1,"r")
    file_2 = open(file2,"r")

    #opening file for writting
    file_duplicate = open(fileToSave,"w")

    #loading files into memory as lines sets
    file_1_line_set = set(file_1.readlines())
    file_2_line_set = set(file_2.readlines())

    #calculating intersections (duplicate entries)
    intersection = file_1_line_set.intersection(file_2_line_set)

    #writting into the file of duplicates
    for line in intersection: file_duplicate.write(line)

    #closing files
    file_1.close()
    file_2.close()
    file_duplicate.close()
    print(f"Duplicate data saved into {fileToSave}.")
    print("Done.")













if __name__ == "__main__": #MAIN PROGRAM
    #file names
    file_name_1 = "nanika1.csv"
    file_name_2 = "nanika2.csv"
    file_name_to_save = "duplicate.csv"

    from csvTestGenerator import *

    #generating files
    generateFile(file_name_1,10000000)
    generateFile(file_name_2,10000000)


    #opening file for reading
    f1 = open(file_name_1,"r")

    #opening file for appending
    f2 = open(file_name_2,"a")

    #copying some rows from one file into the other
    for i in range(37):
        f2.write(f1.readline())

    #closing files
    f1.close()
    f2.close()
    #now these files have some rows duplicated


    #calling the main function
    getDuplicateRowsFromCsv(file_name_1,file_name_2,file_name_to_save)
    print("THE END.")
