# Introduction-to-data-science-with-python
Cover assignment of the coursera course Introduction to Data Science with python by Michigan university
Regex cheat sheet should be used for better understang of the concept.
1. groups in regex:
  For searching different groups of regex out of the data we use paranthesis () and write regex expression in them.
  for example:
  (?P<host>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})
    (?P<user_name>\s[a-z]+\d{4})
    (?P<time>\[.*?\])
  Here we have 3 groups of regular expression , we also used (?P<name>regex_expression) this is used to create a dcitionary with key=name and value=outputs according to the regex expression.
  
