from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from .models import Question, Answer, Comment
from .forms import CreateQuestionForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required



def questions_view(request):
    questions = Question.objects.order_by('-created_time')
    context = {"questions":questions}
    return render(request, 'question/questions.html', context)


@login_required(login_url='login')
def create_question_view(request):

    if request.method == "POST":
        form = CreateQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.question_created_by = request.user 
            form.save()
            return redirect('questions')
    else:
        form = CreateQuestionForm()
    context = {'form':form}
    return render(request, 'question/create-question.html', context)


@login_required(login_url='login')
def questions_related_user(request):
    if request.user.is_authenticated:
        user_questions = Question.objects.filter(related_person=request.user)
    
    return render(request, 'question/questions-by-user.html', {'questions':user_questions})


# @login_required(login_url='login')
# def add_comment_to_answer(request, question_id):
#     return render(request, 'question/questions-by-user.html', {})