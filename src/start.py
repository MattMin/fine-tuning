import json

import openai

openai.api_key = ''

# 上传文件, 用于微调, 返回文件对象
create = openai.File.create(file=open("../data/fine_tuning_dataset.jsonl", "rb"), purpose='fine-tune')
print(create)


# 创建微调任务, training_file 是文件id, model: 基于哪个模型
# openai.FineTuningJob.create(training_file="file-p5765bVe46q1ZXpebFOoGPkD", model="gpt-3.5-turbo-0613")
# 查看微调任务状态
# job_list = openai.FineTuningJob.list()
# print(job_list)


# completion = openai.ChatCompletion.create(
#     model="ft:gpt-3.5-turbo-0613:personal::82sbSaT5",
#     messages=[
#         {"role": "system", "content": "Given a book name, provide the following fields in a JSON dict, where applicable: \"name\", \"author\", \"author_birthday\", \"content_abstract\""},
#         {"role": "user", "content": "34+43"}
#     ]
# )
# print(json.loads(json.dumps(completion.choices[0].message)))
