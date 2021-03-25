import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    return re.findall('[A-Z]\w+',simple_string)

def grades():
    with open ("grades1.txt", "r") as file:
        grades = file.read()

    name=re.finditer('(?P<name>.*\w+)(?P<grade>:\sB)',grades)
    lst=list()
    for item in name:
        z=item.groupdict()['name']
        lst.append(z)
    return len(lst)

# For first question
#Only regex expression can be used for solving the assignment
print((grades()))

#For second question
#Functions can be used separately or only the regex expression can be used for the assignment. 
print(names())

#For third question
with open('grades.txt','r') as grades:
    simple_string=grades.read()
    #print(simple_string)
    pattern=('''
    (?P<host>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})
    (?P<user_name>\s[a-z]+\d{4})
    (?P<time>\[.*?\])
    (?P<request>\".*?\")
    ''')
    answer=re.findall(pattern,simple_string,re.VERBOSE)
    print(answer)
    for item in answer:
        print('item is ',item.groupdict())
        
        
        #For solving the assignment it is advised to use only the regex written below to work. 
        #For better experience Jupyter notebook is advised to use.
    print('answer is ',answer)
    name=re.findall('(?P<host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',simple_string)
    print(name)
    user_name=re.findall('(?P<user_name>\s[a-z]+\d{4})',simple_string)
    print(user_name)
    time=re.findall('(?P<time>(?<=\[).+?(?=\]))',simple_string)
    print((time))
    request=re.findall('(?P<request>\".*?\")',simple_string)
    print(request)
