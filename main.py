import os
from sys import platform

class OSFileHandler:
    def __init__(self):
        #if windows set all paths
        if platform == "win32":
            self.data = os.getcwd() + "/Data/"
        #else mac and linux set paths
        else :
            self.data = "/data"
def main():
    print("Start up")
    file_handler = OSFileHandler()


if __name__ == "__main__":
    main()
