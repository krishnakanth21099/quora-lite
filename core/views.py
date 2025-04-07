from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import UserRegistrationForm, QuestionForm, AnswerForm
from .models import Question, Answer, AnswerLike
from django.db.models import Count

def register(request):
    """
    Handle user registration process.

    This view manages both GET and POST requests for user registration:
    - GET: Displays an empty registration form
    - POST: Processes form submission, creates a new user, and logs them in

    Args:
        request (HttpRequest): The incoming HTTP request

    Returns:
        HttpResponse: Rendered registration page or redirect to home page after successful registration
    """
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
    """
    Render the home page with all questions.

    Retrieves all questions from the database, ordered by creation date (most recent first),
    and displays them on the home page with their answer count.

    Args:
        request (HttpRequest): The incoming HTTP request

    Returns:
        HttpResponse: Rendered home page with list of questions and their answer counts
    """
    # Annotate questions with their answer count
    questions = Question.objects.annotate(
        answer_count=Count('answers')
    ).order_by('-created_at')
    
    return render(request, 'core/home.html', {'questions': questions})

@login_required
def question_create(request):
    """
    Handle the creation of a new question.

    This view is only accessible to authenticated users:
    - GET: Displays an empty question creation form
    - POST: Processes form submission, creates a new question, and redirects to its detail page

    Args:
        request (HttpRequest): The incoming HTTP request

    Returns:
        HttpResponse: Rendered question creation form or redirect to question detail page
    """
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
    """
    Display details of a specific question.

    Retrieves a specific question by its primary key and renders its detail page,
    including all associated answers.

    Args:
        request (HttpRequest): The incoming HTTP request
        pk (int): Primary key of the question to be displayed

    Returns:
        HttpResponse: Rendered question detail page with answers
    """
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
            return redirect('question_detail', pk=question.pk)
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
    """
    Handle liking/unliking an answer.

    Allows authenticated users to like or unlike an answer. If the user has already 
    liked the answer, the like will be removed.

    Args:
        request (HttpRequest): The incoming HTTP request
        answer_id (int): Primary key of the answer to be liked/unliked

    Returns:
        JsonResponse: JSON response indicating the like status and total likes
    """
    answer = get_object_or_404(Answer, id=answer_id)
    
    # Check if user has already liked the answer
    like, created = AnswerLike.objects.get_or_create(
        answer=answer, 
        liked_by=request.user
    )
    
    if not created:
        # If like already exists, delete it (unlike)
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
