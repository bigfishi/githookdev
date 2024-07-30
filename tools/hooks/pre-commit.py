# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import sys, os

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            file_size = os.path.getsize(file_path)
            print("file name: {}, fiel size: {}".format(file_path, file_size))
            if (file_size>1024*1024*10):
                print ("return False")
                return False
            # print file_path
            # # 如果文件是软链接，跳过不计算大小
            # if not os.path.islink(file_path):
            #     total_size += os.path.getsize(file_path)
    # return total_size
    print ("return True")
    return True

# def check_file_size(directory, min_size):
#     """
#     检查指定目录下的文件大小，如果小于指定大小则打印文件名和大小。
#     :param directory: 要检查的目录路径。
#     :param min_size: 文件大小下限（单位：字节）。
#     """
#     for filename in os.listdir(directory):
#         file_path = os.path.join(directory, filename)
#         if os.path.isfile(file_path) and os.path.getsize(file_path) < min_size:
#             file_size = os.path.getsize(file_path)
#             print("文件名: %s, 大小: %d 字节", (filename, file_size))

print ("当前路径是:{}".format(os.getcwd()))
print ("测试中文")
# 使用示例
# check_file_size('.', 0)  # 假设检查1KB以下的文件

noBigImage = get_folder_size('Resources')
errCode = 1
if noBigImage:
	errCode = 0
print ("errCode:{}".format(errCode))
sys.exit(errCode)