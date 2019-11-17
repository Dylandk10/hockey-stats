import os
from sys import platform
import pandas as pd
import numpy as np

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
        if os.path.isfile(self.file_handler.get_file_path() + year):
            print("File exist...")
        else:
            os.makedirs(file_handler.get_file_path + years + "/" + team)
    #write to the so AI can read data
    def update_team_file(self, goals, win, lost):
        file = open(self.file_handler.get_file_path + year + "/" + team, "w")
        file.write("goals: " + goals)
        file.write("wins : " + wins)
        file.write("lost : " + lost)
        file.close()
    #read the data from file
    def read_data(self):
        file = open(self.file_handler.get_file_path + year + "/" + team, "r")
        goals_line = file.readline().split(" :")
        win_line = file.readline().split(" :")
        lost_line = file.readline().split(" :")
        goal_token = goals_line[1].strip()
        win_token = win_line[1].strip()
        lost_token = lost_line[1].strip

        return goal_token, win_token, lost_token


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

df2 = df1[['Date','Season','Visitor','Home','G-V','G-H']]
df2.set_index('Date',inplace = True)
df2['Winner'] = np.where(df2['G-V']>=df2['G-H'], df2['Visitor'], df2['Home'])
df2['Season'] = df2['Season'].str[:4]
df2.head()

#HEAD
years_list = df2.Season.values
years = []
for i in years_list:
    if i[:4] not in years:
        years.append(i[:4])
#print(years)
        
team_list = df2.Visitor.values
teams = []
for i in team_list:
    if i not in teams:
        teams.append(i)


year_team_dict = {}

for year in years:
    season_df = df2.loc[df2.Season == year]
    existing_teams = []
    for i in team_list:
        if i in season_df.Home:
            if i not in existing_teams:
                existing_teams.append(i)
    year_team_dict[year] = existing_teams
    
print(year_team_dict)


df2.head()
    
        

G_H = df1.G-H.values
table_name = df1.Home
table_season = df1.Season
team_name = "Montreal Candiens"
for i in G_H:
    if table_name[i] == team_name and table_season[:4] == 1942:
        adder = int(i)
        accumlator = 0
        accumlator += adder
print(accumlator)

#print(years)


<<<<<<< HEAD
df1.head()
=======
>>>>>>> a67dc4db3e1f5fceba4ffa593c1b0df67422d961
>>>>>>> 54331602514afa2a983c753ce7d378b1834b78fa
