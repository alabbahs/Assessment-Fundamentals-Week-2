from datetime import date

#####
#
# COPY YOUR CODE FROM LEVEL 2 BELOW
#
#####

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
            raise TypeError(
                "Error! Tried to add non-assessment object to list")
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
                list_of_homogeneous_assessments.append(assessment)
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

#####
#
# COPY YOUR CODE FROM LEVEL 2 ABOVE
#
#####


class Question:

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:

    def __init__(self, quiz: Quiz) -> None:
        self._quiz = quiz
        pass

    @property
    def quiz(self):
        return self._quiz
    
    @quiz.setter
    def quiz(self, quiz):
        self.quiz = quiz

    def mark(self) -> int:
        if len(self.quiz.questions) == 0:
            return 0
        num_of_correct_answers = 0
        for question in self.quiz.questions:
            if question.chosen_answer == question.correct_answer:
                num_of_correct_answers += 1
                print("correct")
                print(num_of_correct_answers)
            else:
                print("wrong")
                continue
        num_of_questions = len(self.quiz.questions)
        total_score = int((num_of_correct_answers / num_of_questions) * 100)
        return total_score


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "."),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "."),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
    marking = Marking(quiz)
    marking.mark()