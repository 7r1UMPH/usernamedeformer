import argparse
import sys
import os
import re

ASCII_ART = r"""
.___      _____                                   
 __ __  ______ ___________  ____ _____    _____   ____   __| _/_____/ ____\___________  _____   ___________ 
|  |  \/  ___// __ \_  __ \/    \\__  \  /     \_/ __ \ / __ |/ __ \   __\/  _ \_  __ \/     \_/ __ \_  __ \\
|  |  /\___ \\  ___/|  | \/   |  \/ __ \|  Y Y  \  ___// /_/ \  ___/|  | (  <_> )  | \/  Y Y  \  ___/|  | \/
|____//____  >\___  >__|  |___|  (____  / /|_|  /\___  >____ |\___  >__|  \____/|__|  |__|_|  /\___  >__|   
           \/     \/           \/     \/      \/     \/     \/    \/                        \/     \/   
"""

def generate_usernames(names):
    usernames = set()
    allowed_characters = re.compile(r'[^a-zA-Z0-9_-]')

    for name in names:
        parts = name.split()
        if len(parts) == 0:
            continue  # 如果名字为空，则跳过这一行

        first_name = allowed_characters.sub('', parts[0].lower())
        last_name = allowed_characters.sub('', parts[1].lower()) if len(parts) > 1 else ''

        # 姓名缩写 + 姓氏
        if last_name:
            usernames.add(first_name[0] + last_name)
        # 全名
        if last_name:
            usernames.add(first_name + last_name)
        # 姓氏 + 姓名首字母
        if last_name:
            usernames.add(last_name + first_name[0])
        # 只用名字
        if first_name:
            usernames.add(first_name)
        # 只用姓氏
        if last_name:
            usernames.add(last_name)
        # "j.carlson"
        if last_name:
            usernames.add(first_name[0] + '.' + last_name)
        # "john.c"
        if last_name:
            usernames.add(first_name + '.' + last_name[0])
        # "j.c"
        if last_name:
            usernames.add(first_name[0] + '.' + last_name[0])

    return sorted(usernames)  # 返回排序后的用户名列表

def read_names_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"错误: 文件 {file_path} 未找到。")
        sys.exit(1)
    if not os.access(file_path, os.R_OK):
        print(f"错误: 文件 {file_path} 没有读取权限。")
        sys.exit(1)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            names = f.readlines()
    except IOError as e:
        print(f"错误: 无法读取文件 {file_path}。详情: {e}")
        sys.exit(1)
    # 去除每行末尾的换行符
    return [name.strip() for name in names]

def write_usernames_to_file(usernames, output_file_path):
    if os.path.exists(output_file_path) and not os.access(output_file_path, os.W_OK):
        print(f"错误: 文件 {output_file_path} 没有写入权限。")
        sys.exit(1)
    
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            for username in usernames:  # 直接写入排序后的用户名列表
                f.write(username + '\n')
    except IOError as e:
        print(f"错误: 无法写入文件 {output_file_path}。详情: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="根据名字列表生成用户名，用于渗透测试。")
    parser.add_argument("-l", "--list", required=True, help="包含名字的文件")
    parser.add_argument("-o", "--output", help="保存生成用户名的输出文件")
    args = parser.parse_args()

    file_path = args.list
    output_file_path = args.output

    names = read_names_from_file(file_path)
    usernames = generate_usernames(names)

    if output_file_path:
        print(ASCII_ART)
        write_usernames_to_file(usernames, output_file_path)
        print(f"用户名已成功写入文件 {output_file_path}。")
    else:
        for username in usernames:  # 直接打印排序后的用户名列表
            print(username)

if __name__ == "__main__":
    main()
