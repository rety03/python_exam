def words_url(filename):
    """
    Find urls
    :return: filename: Name of the file
    """
    #open the file
    with open(filename,"r") as file:
        for line in file:
            words = line.split(" ")
            for word in words:
                if word.startswith("https://") and word.startswith(".com"):
                    print(word)
    return

words_url("url.txt")