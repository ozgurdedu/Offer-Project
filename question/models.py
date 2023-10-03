from django.db import models
from django.contrib.auth.models import User
from offer.models import RFQ

class Question(models.Model):

    rfq = models.ForeignKey(RFQ, on_delete=models.CASCADE)
    question = models.TextField(max_length=255)
    answer_1 = models.TextField(max_length=255, blank=True, null=True)
    answer_2 = models.TextField(max_length=255, blank=True, null=True)
    answer_3 = models.TextField(max_length=255, blank=True, null=True)
    answer_4 = models.TextField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    question_created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="question_creator")
    related_person = models.ManyToManyField(User, related_name='related_questions')

    def __str__(self): 
        return self.question



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(max_length=255)
    answer_comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)  
    answer_created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_creator')

    def __str__(self):
        return self.answer
    


class Comment(models.Model):
    comment = models.TextField(max_length=255, blank=True, null=True)
    comment_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="comment_answer_creator")
    
    def __str__(self):
        return self.comment
