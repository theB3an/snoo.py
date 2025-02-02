import os

class Logger:
    def __init__(self, path=None, verbose=False):
        if path is None:
            self.path = os.path.join(os.path.expanduser("~"),"snoopy")
        else:
            self.path = path
        
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        self.verbose = verbose

        print(f"\n[+] Output Directory: {self.path}")

    def open(self, file):
        self.file = open(os.path.join(self.path, file), "w+")

    def log(self, message):
        self.file.write(message + "\n")
        if self.verbose:
            print(f"[INFO] {message}")

    def close(self):
        self.file.close()