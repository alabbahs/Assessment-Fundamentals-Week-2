"""task_three"""

from datetime import date

#####
#
# COPY YOUR CODE FROM LEVEL 1 BELOW
#
#####

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

#####
#
# COPY YOUR CODE FROM LEVEL 1 ABOVE
#
#####

#####
#
# COPY YOUR CODE FROM LEVEL 1 BELOW
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

#####
#
# COPY YOUR CODE FROM LEVEL 2 ABOVE
#
#####

class Question:
    """
    Question class carries the question, answer given by the trainee, 
    and the correct answer.
    """

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:
    """
    Quiz class contains quiz name,
    type of quiz from multiple choice, technical and presentation,
    lastly a list of questions of type Question
    """
    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:
    """
    Marking class contains the quiz to be marked and assesses the
    answers of the trainee compared to the correct answers.
    """

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
        """
        score is calculated as a percentage of...
        number of correct answers / length of question list
        """
        if len(self.quiz.questions) == 0:
            return 0
        num_of_correct_answers = 0
        for question in self.quiz.questions:
            if question.chosen_answer == question.correct_answer:
                num_of_correct_answers += 1
            else:
                continue
        num_of_questions = len(self.quiz.questions)
        total_score = int((num_of_correct_answers / num_of_questions) * 100)
        return total_score
    def generate_assessment(self) -> Assessment:
        """
        creates a species of assessment object based on type of quiz,
        accessed via Quiz class
        """
        if self.quiz.type == "multiple-choice":
            assessment = MultipleChoiceAssessment(self.quiz.name, self.mark())
        elif self.quiz.type == "technical":
            assessment = TechnicalAssessment(self.quiz.name, self.mark())
        elif self.quiz.type == "presentation":
            assessment = PresentationAssessment(self.quiz.name, self.mark())
        return assessment


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
