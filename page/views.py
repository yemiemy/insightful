from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category, Product, Team, Blog, Summer
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.


#HOME
def home(request):
	return render(
		request,
		"index.html",
		{
			'categories':Category.objects.all(),
			'blogs':Blog.objects.all()[:3]
		}
	)

#about
def about(request):
	return render(request,"about.html",{'categories':Category.objects.all(),'teams':Team.objects.all()})

#contact
def contact(request):
	if request.method == 'POST':
		name = request.POST.get('author')
		email = request.POST.get('email')
		message = request.POST.get('message')
		message = str(name)+"\n"+str(email)+"\n"+str(message)
		send_mail('You got a mail!', message, '', ['info@insightfuleduworld.ca'])
		messages.success(request, 'Submission successful')
	return render(request,"contact-us.html",{'categories':Category.objects.all()})

#service
def service(request):
	return render(request,"services.html",{'categories':Category.objects.all()})

#summer
def summer(request):
	return render(request,"summer.html",{'categories':Category.objects.all(),'summers':Summer.objects.order_by("-id")})

#camp
def camp(request,id=id):
	return render(request,"summercamp.html",{'categories':Category.objects.all(),'summer':Summer.objects.filter(id=id)[0]})

#blog
def blog(request):
	return render(request,"blog.html",{'categories':Category.objects.all(),'blogs':Blog.objects.order_by("-id") })

#blogpage
def blogpage(request,id=id):
	return render(request,"blogpage.html",{'categories':Category.objects.all(),'blog':Blog.objects.filter(id=id)[0]})

#tutor
def tutor(request):
	return render(request,"tutor.html",{'categories':Category.objects.all()})

#insight
def insight(request):
	return render(request,"insight.html",{'categories':Category.objects.all()})

#daycare
def daycare(request):
	return render(request,"daycare.html",{'categories':Category.objects.all()})

#study
def study(request):
	return render(request,"study.html",{'categories':Category.objects.all()})


def store(request):
	product_list = Product.objects.filter(is_active=True).order_by("-id")

	paginator = Paginator(list(product_list), 6)
	page = request.GET.get("page")

	products = paginator.get_page(page)

	return render(request, "store.html", {'products':products,'categories':Category.objects.all()})


def section(request,id=id):
	category = Category.objects.filter(id=id)[0]
	product_list = Product.objects.filter(category=category, is_active=True).order_by("-id")
	paginator = Paginator(product_list, 6)
	page = request.GET.get("page")

	products = paginator.get_page(page)

	return render(request, "section.html", {'products':products,'cat':Category.objects.filter(id=id)[0],'categories':Category.objects.all()})