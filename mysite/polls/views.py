from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Post
from django.views.generic import ListView, DetailView


from .models import Choice, Question
# Create your views here.


# def index(request):
#     return HttpResponse("Hello, world.You're at the polls")


# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


post = [  # DUMMY data in list of dictionary
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'first oost content',
        'date_posted': 'December 13,2020'
    },
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'first oost content',
        'date_posted': 'December 13,2020'
    }
]


def about(request):
    context = {  # creating a context dictionary!
        # 'posts': post, not using the dummy data anymore :)
        'posts': Post.objects.all(),
        'title': 'yeasss'

    }
    # the third argument lets us access data from our template.
    return render(request, 'polls/about.html', context)


def about2(request):
    return render(request, 'polls/about2.html', {'title': 'About'})


class PostListView(ListView):
    model = Post
    template_name = 'polls/about.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
