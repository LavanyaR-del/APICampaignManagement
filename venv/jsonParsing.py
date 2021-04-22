import json

# courses = '{"name":"Lavanya","languages":["Java","Python","Ruby"]}'
# #loads method parse json String and it returns dictionary
#
# print(courses)
#
# dict_courses = json.loads(courses)
# print(type(dict_courses))
# print(dict_courses)
# print(dict_courses['name'])
# list_language = dict_courses['languages']
# print(type(list_language[0]))
# print(list_language[2])
# print(dict_courses['languages'][0])

#*********parse content  present in JSon file
with open('C:\\Users\\Lavanya.R\\OneDrive\\Documents\\PyxisPerformanceNotes\\APITesting.txt') as f:

     #return type of load is Dictionary
     data = json.load(f)
     print(data)
     print(type(data))
     print(data['courses'])
     print(data['courses'][2])
     print(data['courses'][1]['title'])

     print("#########################################")
     print(data['dashboard'])
     print(type(data['dashboard']))
     print(data['dashboard']['website'])

     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
     print("using  for each loop iterate the elements")

     for course in data['courses']:
        #print(course)
        if(course['title'] == "RPA"):
            print(course['price'])
        #adding assertion
            assert course['price'] == 60

     print("comparing 2 JSON files")

     with open('C:\\Users\\Lavanya.R\\OneDrive\\Documents\\PyxisPerformanceNotes\\Duplicate.txt') as f:

         # return type of load is Dictionary
         data2 = json.load(f)
         print(data2)
         assert(data == data2)