# Write your code here
def process_data(string_data):
    new = {}
    for i in string_data:
        name, age, *courses = i.split(",")
        new[name] = {
            "age" : int(age),
            'courses' : courses
        }  
    return new
print(process_data(['John Smith,20,Math,Physics', 'Jane Doe,21,Biology,Chemistry,Math']))

def average_age(data):
    sum = 0
    num_students = 0
    for i in data.values():
        sum += i["age"]
        num_students += 1
    return sum/num_students

def courses(data):
    courses = set()
    for c in data.values():
        courses.update(c['courses'])
    return courses

def most_common_courses(data):
    course_count = {}
    for s in data.values():
        for c in s['courses']:
            if c not in course_count:
                course_count[c] = 0
            course_count[c] += 1
        max_count = max(course_count.values())
    return { 
        course
        for course in course_count.keys()
        if course_count[course] == max_count
    }
        



