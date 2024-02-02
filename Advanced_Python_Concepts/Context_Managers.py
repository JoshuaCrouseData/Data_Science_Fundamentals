'''
Context Managers provide a convenient way to allocate and 
release resources precisely when you want to. The most common
way to write a context manager is using the 'with' statement
in conjunction with defining '__enter__' and '__exit__' methods.

Implement a simple context manager for opening and closing 
files, demonstrating resource management.
'''

class FileOpen:
    def __init__(self, filename, mode):
        self.filename = filename # Stores the filename to be opened
        self.mode = mode # Stores the mode in which the file should be opened
    
    def __enter__(self):
        self.file = open(self.filename, self.mode) # Opens the file and stores the file object
        return self.file # Returns the file object to be used within the 'with' block
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close() # Closes the file when exiting the 'with' block


# Using the context manager
        with FileOpen("sample.txt", "w") as f:
            f.write("Hello, Python!")

# The file is automatically closed after the with block