"""task_two"""
from datetime import date

#####
#
# COPY YOUR CODE FROM LEVEL 1 BELOW
#
#####


"""task_one"""


class Assessment:
    """
    Assessment class: an abstraction of an assessment, with attributes such as...
    Name of the assessment
    Type of the assessment
    Score achieved on assessment
    """

    def __init__(self, name: str, type: str, score: float):
        self.name = name
        self.type = type
        self.score = score

        if type not in ["multiple-choice", "technical", "presentation"]:
            raise ValueError("Error! Invalid assessment type")
        if not 0 <= score <= 100:
            raise ValueError("Error! Assessment score is out of range 0-100")


class Trainee:
    """
    Trainee class: an abstraction of a trainee who takes the assessments with attributes...
    Trainee name
    Trainee email
    Trainee date of birth
    Trainee assessments - list of assessments to be taken by trainee
    """

    def __init__(self, name: str, email: str, date_of_birth: date) -> None:
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments: list[Assessment] = []

    def get_age(self) -> int:
        """get_age method returns the age of our trainee from their date of birth"""
        delta_time = date.today() - self.date_of_birth
        days = delta_time.days
        age = int(days//365.25)
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        """add_assessment method adds an assessment to the list of assessments the trainee has"""
        if not issubclass(type(assessment), Assessment):
            raise TypeError()
        else:
            self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        """
        given a name, the method get_assessment finds the assessment with that name, 
        in the list of assessments the trainee has
        """
        for assessment in self.assessments:
            if name == assessment.name:
                return assessment
        return None
    
    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        list1 = []
        for assessment in self.assessments:
            if assessment.type == type:
                list1.append(assessment)
            else:
                continue
        return list1

#####
#
# COPY YOUR CODE FROM LEVEL 1 ABOVE
#
#####


class MultipleChoiceAssessment(Assessment):
    """
    MultipleChoiceAssessment is a child class of Assessment class,
    it is one of the three types of assessments
    """
    def __init__(self, name, score) -> None:
        super().__init__(name, "multiple-choice", score)

    def calculate_score(self):
        """returns score of assessment, technical assessments are weighted 70%"""
        score = self.score*0.7
        return score


class TechnicalAssessment(Assessment):
    """
    TechnicalAssessment is a child class of Assessment class,
    it is one of the three types of assessments
    """
    def __init__(self, name, score) -> None:
        super().__init__(name, "technical", score)

    def calculate_score(self):
        """returns score of assessment, technical assessments are weighted 100%"""
        return self.score

class PresentationAssessment(Assessment):
    """
    PresentationAssessment is a child class of Assessment class,
    it is one of the three types of assessments
    """
    def __init__(self, name, score) -> None:
        super().__init__(name, "presentation", score)

    def calculate_score(self):
        """returns score of assessment, technical assessments are weighted 60%"""
        score = self.score*0.6
        return score


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
