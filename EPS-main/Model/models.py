from django.db import models
from django.contrib.auth.models import User
from numpy import random

class Student (models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User  , on_delete=models.CASCADE)

    Calculus = models.PositiveIntegerField(null=True)
    DataBase = models.PositiveIntegerField(null=True)
    LinerAlgebra = models.PositiveIntegerField(null=True)
    Intro_to_CS = models.PositiveIntegerField(null=True)
    Intro_to_IS = models.PositiveIntegerField(null=True)
    Discrete_Math = models.PositiveIntegerField(null=True)
    ObjectOriented = models.PositiveIntegerField(null=True)
    Statistics = models.PositiveIntegerField(null=True)
    ProgramingLanguage = models.PositiveIntegerField(null=True)
    DifferentialEquation = models.PositiveIntegerField(null=True)
    Operations_Researsh = models.PositiveIntegerField(null=True)
    DataStructure = models.PositiveIntegerField(null=True)
    FileProcessing = models.PositiveIntegerField(null=True)
    AdvancedMathematics = models.PositiveIntegerField(null=True)
    Physics = models.PositiveIntegerField(null=True)
    Stochastic = models.PositiveIntegerField(null=True)
    Multimedia = models.PositiveIntegerField(null=True)
    InformationTheory = models.PositiveIntegerField(null=True)
    SystemAnalysis_And_Design = models.PositiveIntegerField(null=True)
    Department_DS = models.CharField(max_length=2,null =True , blank=True)
    Department_SVM = models.CharField(max_length=2,null =True , blank=True)
    Department_KNN = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Quiz_2(models.Model):
    DIFF_CHOICE = (
        ('easy', 'easy'),
        ('medium', 'medium'),
        ('hard', 'hard'),
    )
    name = models.CharField(max_length=5000)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Quiz Time in minutes")
    required_score_to_pass = models.IntegerField(help_text="Quiz degree to pass")
    difficulty = models.CharField(max_length=20 , choices=DIFF_CHOICE)

    def __str__(self):
        return f"{self.name} - {self.topic} "

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]


class Question(models.Model):
    text = models.TextField(max_length=200)
    quiz = models.ForeignKey(Quiz_2 , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answer(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question , on_delete=models.CASCADE )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text} , answer: {self.text} , correct: {self.correct}"



class Result(models.Model):
    quiz = models.ForeignKey(Quiz_2 , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    score = models.FloatField()


    def __str__(self):
        return str(self.pk)