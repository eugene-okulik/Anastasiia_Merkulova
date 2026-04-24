import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Enter file name")
parser.add_argument("-t", "--text", help="Text for search")
parser.add_argument("--full", action="store_true", help="text for search")
args = parser.parse_args()
print(args.file, args.text)

path = args.file
if os.path.isdir(path):
    os.listdir(path)
    for file in os.listdir(path):
        file_path = os.path.join(path,file)
        open(file_path, 'r').read()

# elif os.path.isfile(path):












