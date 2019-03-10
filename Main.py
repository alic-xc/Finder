from .FinderException import argsError, queryError, extensionError, actionError, directoryError
from shutil import copy, copytree, move
import random
import os


class Finder:

    valid_actions = ['delete','copy','move', 'rename']

    def __init__(self, path='.'):
        self.files = 0
        self.folders = 0
        self.path = path
        self.destination = f"{self.path}/{random.randint(1,100000)}"

    def extension_searcher(self, ext, action):
        """ retrieve all specific extension and perform an action on them """
        try:

            if ext is None:

                raise extensionError(" Please, specify your extension")

            if action is None or action not in Finder.valid_actions:

                raise actionError(" Please, specify valid action ")

            if not self.set_directory():

                return False

            counter = 0

            for currentFolder, subFolder, files in os.walk(self.path):

                temp_ = r''+currentFolder.replace("\\","/")
                if self.destination in temp_:
                    # skip the loop if folders matched
                    continue

                for file in files:

                    if file.endswith(ext):

                        # perform a required action with the file
                        print(f" [100%]  {file}  :  [{currentFolder}]")
                        full_file_path = f"{currentFolder}/{file}"
                        self.required_action(action=action, data=full_file_path)
                        counter += 1

            print(f'Total files found: {counter} file(s)')

        except extensionError as e :

            print(f" Error found : {e}")

        except actionError as e:

            print(f"Error found : {e}")

        except Exception as e :

            print(f"Error Found : {e}")

    def search(self, query, folder=False, file=True, action=''):
        ''' specify & search for any files or folder and return a list '''
        try:

            if query is None:
                raise queryError(" No query input ")

            if folder is False and file is False:
                raise argsError(" either one of the arg(s) is required")

            if action not in Finder.valid_actions:
                raise actionError(" action is required")

            if not self.set_directory():

                return False

            for currentFolder, subFolder, files in os.walk(self.path):

                temp_ = r'' + currentFolder.replace("\\", "/")
                if self.destination in temp_:
                    # skip the loop if folders matched
                    continue

                if folder is True :
                    if query in currentFolder:
                        print(f" Match Found (Folder) : {currentFolder}")

                if file is True:
                    for x in files:
                        if query in x:
                            print(f" Match Found (File) : { x }")
                            self.required_action(action, f"{currentFolder}/{x}")

        except actionError as a:
            print(f"Error Found: {a}")
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
                print(f" ** copying {data} **")
                if os.path.isdir(data):
                    copytree(data, self.destination)

                if os.path.isfile(data):
                    copy(data, self.destination)


            if action == 'move':
                print(f" ** moving {data} **")
                move(data, self.destination)


            if action == 'delete':
                print(f" ** deleting {data} **")
                os.unlink(data)

            print("done")
            return True

        except argsError as a:

            print(f"Error found : {a} ")

    def set_directory(self):

        try:
            if self.destination is None:
                raise directoryError('no folder name ')
            
            if not os.path.exists(self.destination):
                os.mkdir(self.destination)

            return True

        except directoryError as d:

            print(f" Error found : {d} ")

        except Exception as e:

            print(f"Error found : {e}")

        return False
