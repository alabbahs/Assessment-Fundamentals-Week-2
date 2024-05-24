from datetime import date

#####
#
# COPY YOUR CODE FROM LEVEL 1 BELOW
#
#####

class Assessment:
    def __init__(self, name: str, type: str, score: float):
        self.name = name
        self.type = type
        self.score = score

        if type not in ["multiple-choice", "technical", "presentation"]:
            raise ValueError("Error! Invalid assessment type")

        if not (0 <= score <= 100):
            raise ValueError("Error! Assessment score is out of range 0-100")


class Trainee:
    def __init__(self, name: str, email: str, date_of_birth: date) -> None:
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments: list[Assessment] = []

    def get_age(self) -> int:
        delta_time = date.today() - self.date_of_birth
        days = delta_time.days
        age = int(days//365.25)
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        if not isinstance(assessment, Assessment):
            raise TypeError("Error! Tried to add non-assessment object to list")
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        for assessment in self.assessments:
            if name == assessment.name:
                return assessment
        return None
    
    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        list_of_homogeneous_assessments = []
        for assessment in self.assessments:
            if assessment.type == type:
                list_of_homogeneous_assessments.append()
        return list_of_homogeneous_assessments



#####
#
# COPY YOUR CODE FROM LEVEL 1 ABOVE
#
#####


class MultipleChoiceAssessment(Assessment):
    def __init__(self, name, score) -> None:
        super().__init__(name, "multiple-choice", score)

    def calculate_score(self):
        score = self.score*0.7
        return score


class TechnicalAssessment(Assessment):
    def __init__(self, name, score) -> None:
        super().__init__(name, "technical", score)

    def calculate_score(self):
        return self.score

class PresentationAssessment(Assessment):
    def __init__(self, name, score) -> None:
        super().__init__(name, "presentation", score)

    def calculate_score(self):
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
