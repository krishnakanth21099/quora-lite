from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    icon = models.ImageField(upload_to='user_icons/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username


class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(default=timezone.now)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return f'Answer by {self.answered_by.username} on {self.question.title}'

    class Meta:
        ordering = ['-created_at']


class AnswerLike(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='likes')
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_answers')
    liked_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['answer', 'liked_by']

    def __str__(self):
        return f'{self.liked_by.username} liked {self.answer.answered_by.username}\'s answer'
# Create your models here.
