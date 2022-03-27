class DataList:
    list = [
                {"type":"Square", "area":150.5},
                {"type":"Rectangle", "area":80},
                {"type":"Rectangle", "area":660},
                {"type":"Circle", "area":68.2},
                {"type":"Triangle","area": 20},
            ]

l1 = DataList()
for i in range(len(l1.list)):
    print(f'{i+1}- {l1.list[i]["type"]} with area size {l1.list[i]["area"]}')
