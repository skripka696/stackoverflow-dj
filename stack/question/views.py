from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from question.models import Question


class QuestionsView(ListView):
    model = Question
    template_name = 'question_list.html'

    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        return render(request, self.template_name, {'questions': questions})


class QuestionDetail(DetailView):
    model = Question
    template_name = 'question_detail.html'

