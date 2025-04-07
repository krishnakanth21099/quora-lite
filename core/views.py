from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import UserRegistrationForm, QuestionForm, AnswerForm
from .models import Question, Answer, AnswerLike

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'core/home.html', {'questions': questions})

@login_required
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            question.save()
            messages.success(request, 'Question posted successfully!')
            return redirect('question_detail', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'core/question_form.html', {'form': form})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all().order_by('-created_at')
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.answered_by = request.user
            answer.save()
            messages.success(request, 'Answer posted successfully!')
            return redirect('question_detail', pk=pk)
    else:
        form = AnswerForm()
    
    return render(request, 'core/question_detail.html', {
        'question': question,
        'answers': answers,
        'form': form
    })

@login_required
@require_POST
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    like, created = AnswerLike.objects.get_or_create(
        answer=answer,
        liked_by=request.user
    )
    
    if not created:
        like.delete()
        answer.like_count -= 1
        answer.save()
        liked = False
    else:
        answer.like_count += 1
        answer.save()
        liked = True
    
    return JsonResponse({
        'liked': liked,
        'like_count': answer.like_count
    })
