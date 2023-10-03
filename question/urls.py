from django.urls import path 
from . import views

urlpatterns = [
    path('', views.questions_view, name = "questions"),
    path('create-question', views.create_question_view, name = "create-question"),
    path('related-question', views.questions_related_user, name = "related-question"),
    #path('add-comment/<int:question_id>', views.add_comment_to_answer, name = "add-comment"),

]