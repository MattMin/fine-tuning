# OpenAI Fine-Tuning 示例

一个简单的 OpenAI Fine-Tuning 接口 Demo

## 结构说明

### src
代码目录

#### validate_dataset.py 
用于验证数据集是否符合要求, 将代码中引用的文件修改为想要验证的文件, 执行即可

#### start.py 
包含以下功能, 使用时打开对应的注释即可
1. 上传训练数据
2. 查询数据
3. 创建 Fine-Tuning 任务
4. 查询 Fine-Tuning 任务
5. 使用 Fine-Tuning 好的模型聊天

### data
训练数据集目录

## 其他说明
可以对已经 Fine-Tuning 的模型继续 Fine-Tuning, 这样可以在数据集有追加时不用重新训练模型

方法: 在创建 Fine-Tuning  任务时, `model` 填已经 Fine-Tuning 的模型即可
