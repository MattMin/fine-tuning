import json

import openai

openai.api_key = 'sk-'

# 上传文件, 用于微调, 返回文件对象
# create = openai.File.create(file=open("../data/fine_tuning_dataset_lindaiyu.jsonl", "rb"), purpose='fine-tune')
# print(create)

# file_list = openai.File.list()
# print(file_list)

# 创建微调任务, training_file 是文件id, model: 基于哪个模型
# openai.FineTuningJob.create(training_file="file-EmWXH5JhGIp4G3uWTdegTF9f", model="gpt-3.5-turbo-0613")


# 查看微调任务状态
# job_list = openai.FineTuningJob.list()
# print(job_list)

# 取消任务
# job_cancel = openai.FineTuningJob.cancel(id='ftjob-eRwzSW0pulHPnK9zCnnLvNmX')
# print(job_cancel)

completion = openai.ChatCompletion.create(
    model="ft:gpt-3.5-turbo-0613:personal::88XiKf8B",
    messages=[
        {"role": "system", "content": "模仿林黛玉回答问题"},
        {"role": "user", "content": "Google这家公司怎么样"}
    ]
)
print(json.loads(json.dumps(completion.choices[0].message)))
