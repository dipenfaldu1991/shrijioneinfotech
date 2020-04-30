from django.shortcuts import render,redirect
from shrijioneinfotech import settings
from django.core.mail import EmailMessage
# Create your views here.
def index(request):
    return render(request,'index.html')


def about_us(request):
    return render(request,'about-us.html')


def website_development(request):
    return render(request,'website-development.html')


def application_development(request):
    return render(request,'application-development.html')

def e_commerce_solution(request):
    return render(request,'e-commerce-solution.html')

def graphic_design(request):
    return render(request,'graphic-design.html')

def contact_us(request):
    return render(request,'contact-us.html')


def php(request):
    return render(request,'php.html')

def asp(request):
    return render(request,'asp.html')

def python(request):
    return render(request,'python.html')

def java(request):
    return render(request,'java.html')

def android(request):
    return render(request,'android.html')

def send_message(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        content=request.POST.get('content')

        mail_subject = 'Activate your account.'
        email_body = """\
                        <html>
                        <head></head>
                        <body>
                            <h2>Name:-%s</h2>
                            <h2>Email:-%s</h2>
                            <h2>Phone:-%s</h2>
                            <h2>content:-%s</h2>
                        </body>
                        </html>
                        """ % (name, email, phone,content)
        to_email = 'faldu.faldu1991@gmail.com'
        from_email= settings.EMAIL_HOST_USER
        email = EmailMessage(mail_subject, email_body, from_email,to=[to_email])
        email.content_subtype = "html"
        email.send()
        return redirect('index')
    return render(request,'contact-us.html')