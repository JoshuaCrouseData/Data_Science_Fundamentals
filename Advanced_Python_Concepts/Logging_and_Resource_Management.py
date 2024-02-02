import time
from Decorators import timing_decorator
from Context_Managers import FileOpen

@timing_decorator
def process_file(filename):
    with FileOpen(filename, "r") as f:
        lines = f.readlines()
        print(f"Number of lines in the file: {len(lines)}")


process_file("samplefile.txt")
