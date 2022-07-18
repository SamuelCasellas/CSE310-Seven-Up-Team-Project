from datetime import datetime
import os
class Database:

    def __init__(self):
        self.data = dict()
        self.data_list = []
        self.file_name = "data.txt"
        self.top_scores = []


    def load_data(self):
        """Loads the data from data.txt and stores it in a dictionary for later use.
        The dictionary is stored datetime : [initials, score] and can be called as such.
        """
        #load any data from the data.txt and place it into a dictionary.
        with open(self.file_name, "r") as f:
            for line in f:
                currentline = line.split(",")
                self.data_list.append([currentline[0], currentline[2]])
        
    def save_data(self, initials, score):
        """Save a new line of data to the data.txt, if the txt doesn't exist it will create it.
        The data is stored as a comma seperated line. The \n is necessary to create a new line of saved data.
        """
        now = datetime.now()
        saved_datetime = now.strftime("%d/%m/%Y %H:%M:%S")
        #put data into the dictionary
        saved_list = [initials, score]
        self.data[saved_datetime] = saved_list
        #use data and save it to the data.txt
        with open(self.file_name, "a") as f:
            f.write(f"{initials}, {saved_datetime}, {score}, \n")
    
    def clear_data(self):
        os.remove(self.file_name)

    def get_data(self):
        """Sorts score data into descending order and returns the top 7 scores for what can fit on screen"""
        sorted_list = sorted(self.data_list, key=lambda x: int(x[1]), reverse=True)
       
        return sorted_list[:7]
