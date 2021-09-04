# ReplaceMyDir

# 替换批量文件夹内文件的内容

### python3环境运行

1. 配置config.py文件
   
   dirs_map配置文件路径
   
   copy_path为原始文件路径，target_path为修改后的输出路径

   可以在dirs_map数组中配置多个目录映射

   ```
   dirs_map = [
        {
            "copy_path": "/Users/xushuzhen/Project/coneys/Coneys-Blockchain/chia",
            "target_path": "./coneys"
        },
    ]
    ```

    words_map配置需要修改的文件的后缀，和该后缀文件内需要替换的文字

    下面实例是替换文件后缀为py和spec的文件，替换这两种文件中：chia替换为coneys，Chia替换为Coneys

    ```
    words_map = {
        "py": [
            {
                "re": "chia",
                "value": "coneys"
            },
            {
                "re": "Chia",
                "value": "Coneys"
            }
        ],
        "spec": [
            {
                "re": "chia",
                "value": "coneys"
            },
            {
                "re": "Chia",
                "value": "Coneys"
            }
        ],
    }
    ```

2. 运行replace_my_dir.py无脑替换

    ```
    python replace_my_dir.py
    ```
