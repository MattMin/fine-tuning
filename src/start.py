import openai

openai.api_key = ''

job_list = openai.FineTuningJob.list(limit=10)
print(job_list)

create = openai.File.create(file=open("mydata.jsonl", "rb"), purpose='fine-tune')
print(create)
