from django import forms
from .models import Article, Review, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "name",
            "address",
            "sido",
            "sigungu",
            "roadname",
            "number",
            "opening_hour",
            "menu",
            "parking",
            "dayoff",
            "category",
            "image",
        ]
        labels = {
            "name": "가게 이름",
            "address": "주소",
            "sido": "시/도",
            "sigungu": "시/군/구",
            "roadname": "도로명",
            "number": "전화번호",
            "opening_hour": "개점 시간",
            "menu": "메뉴",
            "parking": "주차",
            "dayoff": "휴일",
            "category": "분류",
            "image": "사진",
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "content",
            "rate",
            "image",
        ]
        labels = {
            "title": "제목",
            "content": "내용",
            "rate": "평점",
            "image": "사진",
        }
        widgets = {
            "rate": forms.NumberInput(
                attrs={
                    "step": "0.5",
                    "max": "5.0",
                    "min": "0.5",
                }
            ),
        }


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "댓글을 남겨보세요 💬",
            }
        ),
    )

    class Meta:
        model = Comment
        fields = [
            "content",
        ]


class ReplyForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "대댓글을 남겨보세요 💬",
            }
        ),
    )

    class Meta:
        model = Comment
        fields = [
            "content",
        ]
