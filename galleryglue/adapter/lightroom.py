import os


class Lightroom:
    
    
    def __init__(self, directory):
        subdirectories = next(os.walk(directory))[1]

        for subdir in subdirectories:

