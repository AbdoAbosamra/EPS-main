from django.shortcuts import render
from django.contrib import auth
from numpy.core.fromnumeric import cumprod
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .form import *
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import *
from .decorators import unauthenticated_user , allowed_users , admin_only
from django.views.generic import ListView
from django.http import JsonResponse


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn import svm
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier




def frist_page(request):
    return render(request , 'FristPage.html')

@unauthenticated_user
def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect("admin_Home")
        else:
            messages.info(request , 'Username Or Password is invalid')
    context = {}
    return render(request , 'login.html' , context)

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
           user = form.save()
           return redirect('login')
    context = {'form':form}
    return render(request , 'register.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def User_Home(request):
    pk = request.user.id
    student = Student.objects.get(user = pk)
    context = {'student' : student}
    return render(request, 'user_home.html', context)

@login_required(login_url='login')
@admin_only
def Admin_Home(request):
    return render(request, 'admin_home.html')

def logout1(request):
    logout(request)
    return  redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def Form(request):
    pk = request.user.id
    student = Student.objects.get(user = pk)
    formset = StudentObj(instance= student)
    if request.method == 'POST':
        formset = StudentObj(request.POST, instance=student)
        if formset.is_valid():
            formset.save()
            DecisionTree(request)
            SVM(request)
            KNN(request)
            return redirect('user_home')

    context = {'forms': formset}

    return render(request, 'from1.html', context)

Data = pd.read_csv(r'https://raw.githubusercontent.com/abdel99073616/Data/main/Data-V1.0.csv')
X = Data.drop(["ID" , "Department" ,"IS_Chance" , "CS_Chance"], axis=1)
y = Data["Department"]


'''def Render_info(request):
    pk = request.user.id
    student = Student.objects.get(user=pk)
    df = pd.DataFrame(list(Student.objects.all().values()))
    df = df.loc[df['user_id'] == pk]
    df = df.drop(["user_id", "id", "Department_DS", "Department_SVM", "Department_KNN", "DS_acc",
                  "SVM_acc", "KNN_acc"], axis=1)
    D = df.loc[: , :][0]
    form = StudentObj(instance=student)
    form = StudentObj(request.POST, instance=student)
    if form.is_valid():
        form.save()
    return request
'''
# To do Later

@login_required(login_url='login')
def DecisionTree(request):
    pk = request.user.id
    student = Student.objects.get(user=pk)
    df = pd.DataFrame(list(Student.objects.all().values()))
    df = df.loc[df['user_id'] == pk]
    df = df.drop(["user_id", "id", "Department_DS", "Department_SVM","Department_KNN" ,"DS_acc",
                   "SVM_acc" , "KNN_acc"], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3,random_state=1)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    Dep_pred = clf.predict(df)
    accuracy = clf.score(X_test, y_test)
    student.Department_DS = list(Dep_pred)[0]
    student.DS_acc = format(accuracy * 100,".2f")
    form = StudentObj(instance=student)
    form = StudentObj(request.POST, instance=student)
    if form.is_valid():
        form.save()
    return request


@login_required(login_url='login')
def SVM(request):
    pk = request.user.id
    student = Student.objects.get(user=pk)
    df = pd.DataFrame(list(Student.objects.all().values()))
    df = df.loc[df['user_id'] == pk]
    df = df.drop(["user_id", "id", "Department_DS", "Department_SVM","Department_KNN" ,"DS_acc",
                   "SVM_acc" , "KNN_acc"], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True)
    svm = SVC(kernel="linear", C=0.025, random_state=101)
    svm.fit(X_train, y_train)
    y_pred = svm.predict(X_test)
    Dep_pred = svm.predict(df)
    accuracy = svm.score(X_test, y_test)
    student.Department_SVM = list(Dep_pred)[0]
    student.SVM_acc = format(accuracy * 100,".2f")
    form = StudentObj(instance=student)
    form = StudentObj(request.POST, instance=student)
    if form.is_valid():
        form.save()
    return request

def KNN(request):
    pk = request.user.id
    student = Student.objects.get(user=pk)
    df = pd.DataFrame(list(Student.objects.all().values()))
    df = df.loc[df['user_id'] == pk]
    df = df.drop(["user_id", "id", "Department_DS", "Department_SVM","Department_KNN" ,"DS_acc",
                   "SVM_acc" , "KNN_acc"], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=27)
    neighbors = np.arange(1, 30)
    # train_accuracy =np.empty(len(neighbors))
    # test_accuracy = np.empty(len(neighbors))

    for i, k in enumerate(neighbors):
        # Setup a knn classifier with k neighbors
        knn = KNeighborsClassifier(n_neighbors=k)

        # Fit the model
        knn.fit(X_train, y_train)

        # Compute accuracy on the training set
        # train_accuracy[i] = knn.score(X_train, y_train)

        # Compute accuracy on the test set
        # test_accuracy[i] = knn.score(X_test, y_test)

    knn = KNeighborsClassifier(n_neighbors=24)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = knn.score(X_test, y_test)
    Dep_pred = knn.predict(df)
    student.Department_KNN = list(Dep_pred)[0]
    student.KNN_acc = format(accuracy * 100,".2f")
    print(student.Department_KNN)
    form = StudentObj(instance=student)
    form = StudentObj(request.POST, instance=student)
    if form.is_valid():
        form.save()
    return request


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
class QuizListVeiw(ListView):
    model = Quiz_2
    template_name = 'quizes/quiz.html'

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def quiz_veiw(request):
    quiz = Quiz_2.objects.all()
    context = {'obj': quiz}
    print(context)
    return render(request, 'sidebar.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def quizpk_veiw(request , pk):
    quiz = Quiz_2.objects.get(pk = pk)
    context = {'obj':quiz}
    return render (request, 'quizes/quiz.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def quiz_data_view(request , pk):
    quiz = Quiz_2.objects.get(pk =pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answer():
            answers.append(a.text)
        questions.append({str(q):answers})
    return JsonResponse({
        'data' : questions,
        'time' : quiz.time
    })

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def save_quiz_view(request , pk):
    #print(request.POST)
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        
        for k in data_.keys():
            print('keys:' , k)
            question = Question.objects.get(text= k)
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz_2.objects.get(pk = pk)

        score = 0
        multiplier = 100/quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)
            print('selected:',a_selected)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score+=1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text
                results.append({str(q): {'correct_answer':correct_answer , 'answered':a_selected}})
            else:
                results.append({str(q): 'not answered' })
                
        score_ = score * multiplier
        Result.objects.create(quiz=quiz , user=user , score= score_)
        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'Passed':True , 'score':score_ , 'results':results})
        else:
            return JsonResponse({'Passed': False, 'score': score_, 'results': results})











