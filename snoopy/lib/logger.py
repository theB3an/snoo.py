import os

class Logger:
    def __init__(self, path=None):
        if path is None:
            self.path = os.path.join(os.path.expandser("~"),"snoopy")
        else:
            self.path = path
        
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def open(self, file):
        self.file.open(os.path.join(self.path, file), "w")

    def log(self, message):
        self.file.write(message + "\n")

    def close(self):
        self.file.close()

    def __del__(self):
        self.close()