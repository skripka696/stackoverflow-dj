from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from question.models import Question, Comment
from django.db.models import Count


class QuestionsView(ListView):
    model = Question
    template_name = 'question_list.html'

    def get(self, request, *args, **kwargs):
        questions = Question.objects.annotate(Count('comment'), Count('answers'), Count('vote'))
        return render(request, self.template_name, {'questions': questions})


class QuestionDetail(DetailView):
    model = Question
    template_name = 'question_detail.html'
