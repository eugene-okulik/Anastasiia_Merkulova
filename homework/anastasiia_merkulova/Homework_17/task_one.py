import os
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Enter file name")
parser.add_argument("-t", "--text", help="Text for search")
parser.add_argument("--full", action="store_true", help="text for search")
args = parser.parse_args()

path = args.file
def read_file(path):
    block = {}
    current_key = None
    if os.path.isdir(path):
        all_files = os.listdir(path)
        for file in all_files:
            file_name = f"Название файла: {file}"
            all_files_path = os.path.join(path,file)
            if os.path.isfile(all_files_path):
                with open(all_files_path, 'r') as content_file:
                    for line in content_file.readlines():
                        if re.match(r"^\d{4}-\d{2}-\d{2}", line):
                            current_key = line[:23]
                            block[current_key] = file_name +  '\n' + line[24:]
                        else:
                            if current_key:
                                block[current_key] += line
    return block
block = read_file(path)

def find_text(block):
    if args.full:
        for key, text in block.items():
            if args.text.lower() in text.lower():
                print(key, text)
    else:
        for key, text in block.items():
            if args.text.lower() in text.lower():
                words_block = text.split()
                words_block_lower = [word.lower() for word in words_block]
                for index, word in enumerate(words_block_lower):
                    if args.text.lower() in word:
                        word_index = index
                        break
                start = max(0, word_index - 5)
                end = word_index + 6
                result = words_block[start:end]
                result = ' '.join(result)
                print(key, result)


find_text(block)














