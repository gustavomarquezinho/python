# 009 - Write a Python program to display the examination schedule. (extract the date from exam_st_date).

examDate = (11, 12, 2014)
print(f'\nExamination date: {str(examDate)[1:-1].replace(", ", "/")}\n')