from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from apps.views import paginate
from datetime import date
from forms import *
from models import *

def list(request, language):
	congress_records = Congress.objects.all().order_by('priority').order_by('-opening_date')
	congress_records = paginate(request, congress_records, 20)
	return render_to_response('congress/list.html', {'congresses': congress_records}, context_instance=RequestContext(request))

def detail(request, language, slug):
	congress = get_object_or_404(Congress, slug=slug)
	return render_to_response('congress/detail.html', {'congress': congress}, context_instance=RequestContext(request))

def up_coming(request, language):
	try:
		congress_records = Congress.objects.filter(is_open=1).order_by('-pk')
		congress_records = paginate(request, congress_records, 20)
		return render_to_response('congress/list.html', {'congresses': congress_records}, context_instance=RequestContext(request))
	except:
		msg = 'There is no Upcoming Congress Available'
		return render_to_response('congress/list.html', {'msg':msg}, context_instance=RequestContext(request))

def board_directory(request, language, slug):
	board = BoardDirectory.objects.filter(congress__slug=slug)
	return render_to_response('congress/board.html', {'board': board}, context_instance=RequestContext(request))

def time_table(request, language, slug):
	fee = get_object_or_404(Fee, congress__slug=slug)
	return render_to_response('congress/time_table.html', {'fee': fee}, context_instance=RequestContext(request))

# def members_confirmation(request,slug):
# 	congress = get_object_or_404(Congress, is_open=True,slug=slug)
# 	if request.method == 'POST':
# 		form = ConfirmForm(request.POST)
# 		if form.is_valid():
# 			code = form.cleaned_data["code"]
# 			member = Member.objects.get(code=code,congress__slug=slug)
# 			return render_to_response('congress/member_confirm_form.html', {'member': member,'congress': congress}, context_instance=RequestContext(request))
# 		else:
# 			return render_to_response('congress/member_confirm_form.html', {'form': form,'congress': congress}, context_instance=RequestContext(request))
# 	else:
# 		form = ConfirmForm()
# 	return render_to_response('congress/member_confirm_form.html', {'form': form,'congress': congress}, context_instance=RequestContext(request))

# def register(request, slug):
# 	congress = get_object_or_404(Congress, slug=slug)
# 	if request.method == 'POST':
# 		form = RegisterForm(request.POST, prefix = 'congress_form')
# 		if form.is_valid():
# 			member = form.save(commit=False)
# 			member.congress = congress
# 			member.save()
# 			member.code = str(date.today().year)+str(member.id)
# 			member.save()
# 			return render_to_response('congress/form.html', {'congress': congress,'code': member.code}, context_instance=RequestContext(request))
# 		else:
# 			return render_to_response('congress/form.html', {'congress': congress,'form': form}, context_instance=RequestContext(request))
# 	else:
# 		form = RegisterForm(prefix = 'congress_form')
# 	return render_to_response('congress/form.html', {'congress': congress,'form': form}, context_instance=RequestContext(request))
#
# def articles_confirmation(request,slug):
# 	congress = get_object_or_404(Congress, is_open=True,slug=slug)
# 	if request.method == 'POST':
# 		form = ArticleConfirmForm(request.POST)
# 		if form.is_valid():
# 			code = form.cleaned_data["code"]
# 			article = Article.objects.get(code=code,congress__slug=slug)
# 			return render_to_response('congress/article_confirm_form.html', {'article': article,'congress': congress}, context_instance=RequestContext(request))
# 		else:
# 			return render_to_response('congress/article_confirm_form.html', {'form': form,'congress': congress}, context_instance=RequestContext(request))
# 	else:
# 		form = ArticleConfirmForm()
# 	return render_to_response('congress/article_confirm_form.html', {'form': form,'congress': congress}, context_instance=RequestContext(request))
#
# def articles_submission(request, slug):
# 	congress = get_object_or_404(Congress, slug=slug)
# 	if request.method == 'POST':
# 		form = ArticleForm(request.POST, prefix = 'congress_form')
# 		if form.is_valid():
# 			article = form.save(commit=False)
# 			article.congress = congress
# 			article.save()
# 			article.code = str(date.today().year)+str(date.today().month)+str(article.id)
# 			article.save()
# 			return render_to_response('congress/submission_form.html', {'congress': congress,'code': article.code}, context_instance=RequestContext(request))
# 		else:
# 			return render_to_response('congress/submission_form.html', {'congress': congress,'form': form}, context_instance=RequestContext(request))
# 	else:
# 		form = ArticleForm(prefix = 'congress_form')
# 	return render_to_response('congress/submission_form.html', {'congress': congress,'form': form}, context_instance=RequestContext(request))