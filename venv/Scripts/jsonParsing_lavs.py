import json

with open('C:\\Users\\Lavanya.R\\OneDrive\\Documents\\PyxisPerformanceNotes\\Duplicate.txt') as f:
    data = json.load(f)
    print(data)
    print(type(data))

    # print(data['dashboard'])
    # print(data['dashboard']['purchaseAmount'])
    # print(data['dashboard']['website'])

    print(data['courses'])
    print(data['courses'][1]['title'])
    # print(data['courses'][1])
    # print(data['courses'][2])

    #to avoid indexing use below concept

    for course in data['courses'] :
        if (course['title'] == 'RPA'):
            print (course['price'])
            assert course['price'] == 60


with open('C:\\Users\\Lavanya.R\\OneDrive\\Documents\\PyxisPerformanceNotes\\APITesting.txt') as f:
    data2 = json.load(f)
    assert (data == data2)
