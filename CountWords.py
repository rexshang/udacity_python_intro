"""Count words."""
from pkg_resources._vendor.pyparsing import WordStart

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # stores words and ocurrence in words
    words = dict()
    # store the top
    results = dict()

    line = s.split()
    max_occurence = 1
    # TODO: Count the number of occurences of each word in s
    
    for word in line:
        if words.has_key(word):
            # word is found already in our list
            occurence = words[word] + 1
            words[word] = occurence
            if max_occurence < occurence:
                 max_occurence = occurence
                 
            # remove from lower occurence list and move into higher occurence list
            list = results[occurence - 1]
            list.remove(word)
            if results.has_key(occurence):
                list = results[occurence]
            else:
                list = []
            list.append(word)
            results[occurence] = list
             
        else:
            # word is new to our list
            words[word] = 1
            if results.has_key(1):
                list = results[1]
            else:
                list = []
                results[1] = list
            list.append(word)
            results[1] = list
            
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    
    
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    top_n = [];
    occurence= max_occurence
    
    i = n
    while i > 0 and occurence > 0:
        list = results[occurence]
        list.sort()
        for j in range(len(list)):
            tup = (list[j], occurence)
            top_n.append(tup)
            i = i - 1
            if i < 1: break
        occurence = occurence - 1
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()