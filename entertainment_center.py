'''
Created on Oct 21, 2016

@author: erexsha
'''
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toy come to life",
                        "",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
print (toy_story.storyline)
toy_story.show_trailer()