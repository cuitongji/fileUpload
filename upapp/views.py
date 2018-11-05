# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from . import user_decorator
from django.shortcuts import render
from .forms import UserForm
from .models import UserInfo, UpInfo
from hashlib import sha1
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# def register(request):
# 	return render(request, 'upapp/register.html')

# def registerHandle(request):
# 	return render('upapp/index.html')

# @csrf_exempt
def login(request):
	uname = request.COOKIES.get('uname', '')
	return render(request, 'upapp/login.html')

def login_handle(request):
	# 接受请求信息
	post = request.POST
	uname = post.get('username')
	upwd = post.get('pwd')
	# jizhu = post.get('jizhu', 0)
	# 根据用户名查询对象
	users = UserInfo.objects.filter(uname=uname)  # []
	print(uname)
	print(1)
	# 判断：如果未查到用户名错，如果查到则判断密码是否正确，正确则转向用户中心
	if len(users) == 1:
		print(2)
		# s1 = sha1()
		# s1.update(upwd)
		# if s1.hexdigest() == users[0].upwd:
		print(upwd)
		print(users[0].upwd)
		if upwd == users[0].upwd:
			print(3)
			url = request.COOKIES.get('url', '/')
			red = HttpResponseRedirect(url)
			# 成功后删除转向地址，防止以后直接登录造成的转向
			red.set_cookie('url', '', max_age=-1)
			# 记住用户名
			# if jizhu != 0:
			# 	red.set_cookie('uname', uname)
			# else:
			# 	red.set_cookie('uname', '', max_age=-1)
			request.session['user_id'] = users[0].id
			request.session['user_name'] = uname
			return red
		else:
			context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1,
					   'uname': uname, 'upwd': upwd}
			return render(request, 'upapp/login.html', context)
	else:
		context = {'title': '用户登陆', 'error_name': 1, 'error_pwd': 0, 'uname': uname,
				   'upwd': upwd}
		return render(request, 'upapp/login.html', context)

	return render('upapp/index.html')

def logout(request):
	request.session.flush()
	return redirect('/login')

@user_decorator.login
def index(request):
	if request.method == 'POST':
		userform = UserForm(request.POST, request.FILES)
		if userform.is_valid():
			user = UpInfo()
			user.uname = userform.cleaned_data['uname']
			user.uploadFile = userform.cleaned_data['uploadFile']
			user.save()
			return render(request, 'upapp/uploadOK.html')
	else:
		userform = UserForm(initial={'uname': request.session['user_name']})
	return render(request, 'upapp/index.html', {'userform': userform})
