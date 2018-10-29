"""
Author:  Roger Hinson
Date Created:  10/26/2018
Purpose:  Class for the creation of Poem objects

Shared: On Github
"""

class Poem():
    """
    Create Poem objects with an author and name or title of a poem
    """

    # Track number of Poems created
    obj_created = 0

    def __init__(self, author, title, text="", haiku="False"):
        """ Initialize a Poem object with author and title """
        self.author = author
        self.title = title
        self.text = text
        self.haiku = haiku
        self.name = self
        Poem.obj_created += 1

    def get_PoemText(self):
        """ Returns the text of the Poem object """
        return self.text if self.text else "No Text Yet"

    def set_PoemText(self, poem_text, haiku=False):
        """ Sets the text of the Poem object """
        self.text = poem_text
        self.haiku = haiku

    def get_haiku(self):
        """ Returns the boolean of haiku for the Poem """
        return self.haiku

    def set_haiku(self, haiku):
        """ Set the boolean of the the haiku"""
        self.haiku = haiku

    @staticmethod
    def poem_count():
        """ Return the number of Poem objects created"""
        return Poem.obj_created

    def __str__(self):
        """ String method to return the object information """
        return "Author: " + self.author +"\nTitle: " + self.title + "\nHaiku: " + str(self.haiku) + \
            "\nText: " + self.text + "\n"


poem_1 = Poem("Roger", "My Poem")
poem_2 = Poem("Jennifer", "Her Poem", "My day is like a winter's night\nCold and dark\nBut short lived\n", False)
poem_3 = Poem("Wolf", "His Poem", "A teacher by night\nA developer by day\nI'm taught by Wolf\n", True)

poem_1.set_PoemText("I like to read\nA lot\nI like to read\n")
poem_1.set_haiku(False)

print(poem_1)
print(poem_2)
print(poem_3)

print(poem_1.get_PoemText())
print(poem_2.get_PoemText())
print(poem_3.get_PoemText())

print("There are %d poems" % Poem.poem_count())

