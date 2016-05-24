import os


class Lightroom:
    INDEX_FILE = 'index.html'
    galleries = []

    def __init__(self, directory):
        self.galleries = []
        subdirectories = next(os.walk(directory))[1]

        for subdir in subdirectories:
            fullpath = os.path.normpath(os.path.join(directory, subdir, self.INDEX_FILE))

            if os.path.exists(fullpath) and os.path.isfile(fullpath):
                self.galleries.append(fullpath)
