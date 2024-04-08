#codes to define the class
class students(object):
    """
    record the students' names, majors (BMS/BMI), and scores of each ICA(marked out of 100)
    """
    def __init__(self,name:str,major:str,code_portfolio_score:float,group_project_score:float,exam_score:float):
        self.name=name
        self.major=major
        self.code_portfolio_score=code_portfolio_score
        self.group_project_score=group_project_score
        self.exam_score=exam_score
    def detail(self):
        return print('name:',self.name,';major:',self.major,';score of code portfolio:',self.code_portfolio_score,';score of group project:',self.group_project_score,';score of the exam:',self.exam_score)

#example of using the class
Tom = students('Tom','BMI',90.5,80,70) #first record one's information
print(Tom.code_portfolio_score) #call the attribute (code_portfolio_score as an example)
#show the student's all information in a single line. No need to 'print' here because this step is involved in the function
Tom.detail() #method 1
students.detail(Tom) #method 2