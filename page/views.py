from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category, Product, Team
from django.core.mail import send_mail
# Create your views here.




#HOME
def home(request):
	return render(request,"index.html",{'categories':Category.objects.all()})

#about
def about(request):
	return render(request,"about.html",{'categories':Category.objects.all(),'teams':Team.objects.all()})

#contact
def contact(request):
	if request.method == 'POST':
		name = request.POST.get('author')
		email = request.POST.get('email')
		message = request.POST.get('message')
		print(name)
		message = str(name)+"\n"+str(email)+"\n"+str(message)
		send_mail('You got a mail!', message, '', ['fagoroyeayomide3243@gmail.com'])
	return render(request,"contact-us.html",{'categories':Category.objects.all()})

#service
def service(request):
	return render(request,"services.html",{'categories':Category.objects.all()})

#summer
def summer(request):
	return render(request,"summer.html",{'categories':Category.objects.all()})

#camp
def camp(request):
	return render(request,"summercamp.html",{'categories':Category.objects.all()})

#blog
def blog(request):
	return render(request,"blog.html",{'categories':Category.objects.all()})

#blog1
def blog1(request):
	return render(request,"blog-1.html",{'categories':Category.objects.all()})

#blog2
def blog2(request):
	return render(request,"blog-2.html",{'categories':Category.objects.all()})

#blog3
def blog3(request):
	return render(request,"blog-3.html",{'categories':Category.objects.all()})

#blog4
def blog4(request):
	return render(request,"blog-4.html",{'categories':Category.objects.all()})

#blog5
def blog5(request):
	return render(request,"blog-5.html",{'categories':Category.objects.all()})

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
	# print(dir(Category.objects.filter(name="religious")[0].product.all()))
	# print(Category.objects.filter(name="religious")[0].product.all())
	# #print(Category.objects.filter(name="religious")[0].objects.all())
	# cat = Category.objects.all()
	# paginator = Paginator(cat, 2)  # Show 25 contacts per page.
	product_list = Product.objects.filter(is_active=True)
	
	paginator = Paginator(list(product_list), 6)
	page = request.GET.get("page")

	products = paginator.get_page(page)
	
	# page_number = request.GET.get("page")
	# page_obj = paginator.get_page(page_number)
	return render(request, "store.html", {'products':products,'categories':Category.objects.all()})


def section(request,id=id):
	# print(dir(Category.objects.filter(name="religious")[0].product.all()))
	# print(Category.objects.filter(name="religious")[0].product.all())
	# #print(Category.objects.filter(name="religious")[0].objects.all())
	# cat = Category.objects.all()
	# paginator = Paginator(cat, 2)  # Show 25 contacts per page.
	category = Category.objects.filter(id=id)[0]
	product_list = Product.objects.filter(category=category)
	print(product_list)
	paginator = Paginator(product_list, 6)
	page = request.GET.get("page")

	products = paginator.get_page(page)
	
	# page_number = request.GET.get("page")
	# page_obj = paginator.get_page(page_number)
	return render(request, "section.html", {'products':products,'cat':Category.objects.filter(id=id)[0],'categories':Category.objects.all()})