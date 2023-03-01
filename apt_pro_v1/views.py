from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import AptdealToday
from .serializers import TestDataSerializer
# from django.utils import timezone
# from django.utils.html import urlize
from django.http import HttpResponse
from apt_pro_v1 import serializers

# Create your views here.
# -------------------------------------------------------------------------------------------------
# real project start
# # -------------------------------------------------------------------------------------------------
# @api_view(['GET'])
# def getTestDatas(request):
#     datas = AptdealToday.objects.all()
#     serializers = TestDataSerializer(datas, many=True)
#     return Response(serializers.data)

# @api_view(['GET'])
# def getTestData(request, price):
#     data = AptdealToday.objects.get(price=price)
#     serializers = TestDataSerializer(data, many=False)
#     return Response(serializers.data)

@api_view(['POST'])
def postMember(request):
    reqData = request.data
    serializer = TestDataSerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def Aptdata(request, aptid):
    data = AptdealToday.objects.get(id = aptid)
    serializers = TestDataSerializer(data, many=False)
    return Response(serializers.data)

def apt_list(request):
    aptid = AptdealToday.objects.get(aptid=id)
    if request.method == 'POST':
        aptid = request.POST['id']  # 입력받은 문자열
        linked_text = urlize(input_text)  # URL 자동 링크 거는 함수 호출
    return render(request, 'apt_pro_v1/apt_list.html', {'id': id})

def main(request):
    return render(request, 'apt_pro_v1/main.html', {})

def apt2me(request):
    return render(request, 'apt_pro_v1/apt2me.html', {})

















# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# real project end
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     if request.method == 'POST':
#         input_text = request.POST['input_text']  # 입력받은 문자열
#         linked_text = urlize(input_text)  # URL 자동 링크 거는 함수 호출
#     return render(request, 'apt_pro_v1/post_list.html', {'posts': posts})
    

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'apt_pro_v1/post_detail.html', {'post': post})

# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'apt_pro_v1/post_edit.html', {'form': form})

# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'apt_pro_v1/post_edit.html', {'form': form})