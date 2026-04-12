import argparse
import os


# parser = argparse.ArgumentParser(description='Folder Name to size of all files.')

# parser.add_argument('folder_path', help='give the name of folder')

# args = parser.parse_args()

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    return total_size



size = get_folder_size(r"D:\STUDY")
print(f'size : {size/ (1024*1024):.2f} MB')

























# def get_folder_size(folder_path):
#     total_size = 0
#     for dirpath, dirnames, filenames in os.walk(folder_path):
#         print("Current folder:", dirpath)
#         print("Subfolders:", dirnames)
#         print("Files:", filenames)
#         print("-" * 40)
#         for f in filenames:
#             fp = os.path.join(dirpath, f)
#             print(fp)
#             if os.path.exists(fp):
#                 total_size += os.path.getsize(fp)
#     return total_size

# a = get_folder_size(r'D:\STUDY\Python\practice start 30-03-2026\08-File IO')
# print(a)
