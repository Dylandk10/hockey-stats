import os
from sys import platform
import pandas as pd

#to easily access file across systems
class OSFileHandler:
    def __init__(self):
        #if windows set all paths
        if platform == "win32":
            self.hockey_data = os.getcwd() + "/Data/nhlfile.xls"
            self.path = os.getcwd() +"/Data/"
        #else mac and linux set paths
        else:
            self.hockey_data = "/Data/nhlfile.xls"
            self.path = "/Data/"
    def get_hockey_data(self):
        return self.hockey_data
    def get_file_path(self):
        return self.path

#for storing the data file
class FileManager:
    def __init__(self, year, team):
        file_handler = OSFileHandler()
        self.year = year
        self.team = team
    #make file path for the hockey team data to sort
    def make_file_for_team(self):
        if os.path.isfile(file_handler.get_file_path() + year):
            print("File exist...")
        else:
            os.makedirs(file_handler.get_file_path + years + "/" + team)

def main():
    print("Start up")
    file_handler = OSFileHandler()
    print(file_handler.get_hockey_data())


if __name__ == "__main__":
    main()

nhlfile = pd.ExcelFile('nhlfile.xls')

worksheets = nhlfile.sheet_names[1:]

print('All of the worksheets', worksheets)

each_worksheet = {}
all_years_df = pd.DataFrame()

for year in worksheets:
    each_worksheet[year] = pd.read_excel('nhlfile.xls', sheet_name = year)
  
        
df1 = pd.concat(each_worksheet)

df2 = df1.iloc[]

df1.head()