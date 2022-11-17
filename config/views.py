from django.shortcuts import render
from cafes.models import Article, Review
from django.views.decorators.http import require_safe


@require_safe
def main(request):
    articles = Article.objects.order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "main.html", context)
