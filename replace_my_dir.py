import os
import shutil
from config import *


def main():
    for dir_map in dirs_map:
        copy_path = dir_map["copy_path"]
        target_path = dir_map["target_path"]
        re_copy_dir(copy_path, target_path)
        for cur_dir, sub_dir, files in os.walk(target_path):
            if files:
                for file in files:
                    dir_path = cur_dir.replace(copy_path, target_path)
                    file_path = dir_path + "/" + file
                    try:
                        suffix = file.split(".")[1]
                        if suffix in words_map.keys():
                            replace_file(file_path, words_map[suffix])
                            print("Replace Success: " + file_path)
                    except AttributeError:
                        print("Error with: " + file_path)


def re_copy_dir(copy_path, target_path):
    try:
        shutil.rmtree(target_path)
        print("Remove: " + target_path)
    except FileNotFoundError:
        pass
    shutil.copytree(copy_path, target_path)
    print("Copy: " + target_path)


def replace_file(file_path, words_map_rexp):
    content = read_file(file_path)
    for word_map in words_map_rexp:
        content = content.replace(word_map["re"], word_map["value"])
    rewrite_file(file_path, content)


def read_file(file):
    with open(file, encoding='UTF-8') as f:
        read_all = f.read()
        f.close()
    return read_all


def rewrite_file(file, data):
    with open(file, 'w', encoding='UTF-8') as f:
        f.write(data)
        f.close()


if __name__ == "__main__":
    main()
