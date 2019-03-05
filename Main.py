from .FinderException import argsError, queryError, extensionError, actionError
from shutil import copy, move
import os

class finder:

    valid_actions = ['delete','copy','move', 'rename']

    def __init__(self):
        self.files = []
        self.folders = []
        self.path = '.'
        self.destination = ''
        self.ext = ''
        self.action = ''

    def run(self, action):
        pass

    def extension_searcher(self, ext, action):
        """ retrieve all specific extension and perform an action on them """
        try:

            if ext is None:
                raise extensionError(" Please, specify your extension")

            if action is None or action not in finder.valid_actions:
                raise actionError(" Please, specify valid action ")

            for currentFolder, subFolder, files in os.walk(self.path):

                for file in files:

                    if file.endswith(ext):

                        copy(f"{currentFolder}/{file}", self.destination)

        except extensionError as e :

            print(f" Error found : {e}")

        except actionError as e:

            print(f"Error found : {e}")

        except Exception as e :

            print(f"Error Found : {e}")



    def search(self, query, folder=False, file=True):
        ''' specify & search for any files or folder and return a list '''
        try:

            if query is None:
                raise queryError(" No query input ")

            if folder is False and file is False:
                raise argsError(" either one of the arg(s) is required")

            for currentFolder, subFolder, files in os.walk(self.path):


                if folder is True :
                    if query in currentFolder:
                        print(f" Match Found (Folder) : {currentFolder}  ")

                if file is True:
                    file = [x for x in files if query in x]
                    print(f" Match Found (File) : { file }")




        except queryError as q:
            print(f"Error Found: {q}")

        except argsError as a:
            print(f"Error Found: {a}")

        except Exception as e:
            print(f"Error Found: {e}")

    
    def required_action(self, action, data ):
        """ mapped string with function on working on files or folders """
        try:
            if action is None or data is None:
                raise argsError('either one of the args is required')

            if action == 'copy':
                copy(data, self.destination)

            if action == 'move':
                move(data, self.destination)

            if action == 'delete':
                os.unlink(data)

        except argsError as a:

            print(f"Error found : {a} ")