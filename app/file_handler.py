class FileHandler:
    def __init__(self):
        self.files = {}

    def store(self, filename, content):
        self.files[filename] = content

    def retrieve(self, filename):
        return self.files.get(filename)

    def list_files(self):
        return list(self.files.keys())