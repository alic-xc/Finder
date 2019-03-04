import os
import pathlib

class finder:
    valid_actions = ['delete','copy','move', 'rename']
    def __init__(self):
        self.files = []
        self.folders = []
        self.
        self.path = '.'
        self.ext = ''
        self.action = ''

    def run(self, action):
        pass

    def search(self, query, folder=False, file=True):
        ''' specify & search for any files or folder and return a list '''
        try:

            if query is None:
                raise queryError(" No query input ")

            if folder is False and file is False:
                raise argsError(" either arg(s) is required")

            for currentFolder, subFolder, files in os.walk(self.path):

                # if query in currentFolder or query in files:
                #     print(f"Match Found : {currentFolder} : { files }")
                if folder is True :
                    pass





        except:
            pass

