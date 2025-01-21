# username deformer

## 概述

根据名字列表生成用户名，用于渗透测试。

## 使用方法

生成用户名并打印到控制台

```bash
python3 usernamedeformer.py -l names.txt
```

`-l` 或 `--list`：指定包含名字的文件路径。

生成用户名并保存到文件

```bash
python3 usernamedeformer.py -l names.txt -o usernames.txt
```


`-l` 或 `--list`：指定包含名字的文件路径。

`-o` 或 `--output`：指定保存生成用户名的输出文件路径。
