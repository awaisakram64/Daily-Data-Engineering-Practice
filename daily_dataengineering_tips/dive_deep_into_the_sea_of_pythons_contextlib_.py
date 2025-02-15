from contextlib import ExitStack

files = ['file1.txt', 'file2.txt', 'file3.txt']

with ExitStack() as stack:
    file_objects = [stack.enter_context(open(fname, 'r')) for fname in files]
    
    for f in file_objects:
        print(f.read())