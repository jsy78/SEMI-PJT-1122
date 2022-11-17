from django.shortcuts import render
from cafes.models import Article, Review
from django.views.decorators.http import require_safe
from django.core.paginator import Paginator


@require_safe
def main(request):
    articles = Article.objects.order_by("-pk")

    page = request.GET.get("page", "1")
    paginator = Paginator(articles, 6)
    page_obj = paginator.get_page(page)

    context = {
        "articles": articles,
        "page_obj": page_obj,
    }
    return render(request, "main.html", context)
