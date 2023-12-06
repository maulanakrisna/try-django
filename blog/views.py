from django.shortcuts import reverse, get_object_or_404

# Create your views here.
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .models import Article
from .forms import ArticleModelForm


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_success_url(self):
        return reverse('articles:article-list')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # success_url = '../'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    # def get_success_url(self):


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # success_url = '../'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    # def get_success_url(self):


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()
