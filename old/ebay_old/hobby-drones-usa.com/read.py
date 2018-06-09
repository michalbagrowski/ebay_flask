import json
with open('/tmp/categories_0') as data_file:
    c = json.load(data_file)
    for i in c:
        print(i)
