from django.shortcuts import render
from .models import Post
import pyrebase


config={
    apiKey: "AIzaSyCmD_ctc82-77-PwrslQ00VI0bJK59EbBA",
    authDomain:"",
    databaseURL:"",
    projectId:"test-75f3e",
    storageBucket:"",
    messaginSendId:"",
    appId:""
}
# Create your views here.

def index(request):
    trending_posts = Post.objects.filter(trending=True)  # Fetch trending posts
    posts = Post.objects.filter(trending=False)  # Fetch non-trending posts

    return render(request, 'blogapp/index.html', {'trending_posts': trending_posts, 'posts': posts})
def readmore(request):
    return render(request, 'blogapp/readmore.html')
