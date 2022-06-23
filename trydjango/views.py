"""
To render html web pages
"""
import random
from django.shortcuts import render
from articles.models import Article

def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    name = "Justin" # hard coded
    # random_id = random.randint(1, 4) # pseudo random
    
    # from the database??
    # article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    # context = {
    #     "object_list": article_queryset,
    #     "object": article_obj,
    #     "title": article_obj.title,
    #     "id": article_obj.id,
    #     "content": article_obj.content
    # }
    # Django Templates
    # HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = """
    # <h1>{title} (id: {id})!</h1>
    # <p>{content}!</p>
    # """.format(**context)
    return render(request, "home-view.html", {"context": article_queryset})


def page_404(request, exception):
    return render(request, "404.html", status=404)