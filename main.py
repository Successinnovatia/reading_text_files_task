# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from cgitb import text


def read_file_content(filename):
    # [assignment] Add your code here
    #opening the file in read mode
    with open("story.txt", "r") as f:
        #to read the contents of the file
        contents = f.read() 
        #closing the open file
        f.close()
    
    return contents

print(read_file_content("story.txt"))


def count_words(text):
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    import string
    #created an empty dictionary
    counts = {}
    #remove whitespaces and newlines
    words = text.strip()
    #convert characters to lowercase
    words = text.lower()
    #remove punctuatiion marks fromtext
    words = text.translate(text.maketrans("","", string.punctuation))
    #split text into words
    words = text.split(" ")
    #iterate over each word in text
    for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word]= 1
    return counts
print(count_words(text))   