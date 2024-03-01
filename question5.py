def words_c(filename):
    """
    Find words beginning with the letter C and ending in jeb
    :return: filename: Name of the file
    """
    #open the file
    with open(filename,"r") as file:
        for line in file:
            words = line.split(" ")
            for word in words:
                if word.startswith("c") and word.endswith("jeb"):
                    print(word)
    return

words_c("cjeb.txt")