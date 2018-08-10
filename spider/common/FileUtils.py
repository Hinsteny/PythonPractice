"""file operate utils
1. write content to file

"""
# !/usr/bin/python

import os


def mk_file_folder(file_path):
    folder_path = os.path.dirname(file_path)
    is_exists = os.path.exists(folder_path)
    if not is_exists:
        os.makedirs(folder_path)


def write_content_to_file(filePath, content):
    mk_file_folder(filePath)
    with open(filePath, 'w') as f:
        f.write(content)
    print("write file success!")


if __name__ == '__main__':
    filePath = "E:/data/python/test.txt"
    content = "Hello World!"
    write_content_to_file(filePath, content)
