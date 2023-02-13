import pandas as pd

if __name__ == "__main__":
    Tweets = open("Tweets.txt");#Creating a file object with the tweet file
    Tweets = Tweets.strip('\n'); #Seperating tweets into a by using the next-line('\n') character as the differentiator


    """Converting files to a list makes a data intensive task much easier, more efficient and less error prone """

    slurs_FILE = open("Racial_slurs.txt");#I will assume a file with racial slurs in a csv format.
    lines = slurs_FILE.readlines();#Creating a list with the racial words for easier processing further.
    racial_Slurs = [line for line in lines];#Adding a single slur in every position in the index.

    #Calculating the number of words in a tweet
    for Tweet in Tweets:

        number_Of_words = 0#Variable for storing the number of words in a tweet which is used to calculate the profanity percentage
        number_Of_slurs = 0;
        for slur in racial_Slurs:#Iterating through the sentence where 'slur' is an individual slur word.
            number_Of_slurs += Tweet.lower().count(slur.lower());#Calculate how many times a slur is repeated in a sentence
            # by first convert both the words into lowercase and then using count() function to find how many times it is repeated
            number_Of_words += 1;#Increment for every Iteration

            """I will be calculating the profanity percentage by dividing the number of slurs with the total words in a sentence and then multiply ot with 100"""

            print("Profanity Percentage {0}".format(((number_Of_slurs/number_Of_words)*100)));
            #Prints the user name along side the percentage of racial profanity


