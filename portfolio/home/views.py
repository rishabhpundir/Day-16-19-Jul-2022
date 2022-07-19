from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.

def index(request):
    # return HttpResponse("This is a index page.")
    context = {'name':'Rishabh Pundir', 'occupation':'Web Developer Intern'}
    return render(request, 'index.html', context)
    
def about(request):
    return render(request, 'about.html')
    
def login(request):
    return render(request, 'login.html')
    
def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['mail_id']
        phone_no = request.POST['phone_no']
        query = request.POST['query']

        #saving data to DB
        ins = Contact(name=name, email=email, phone_no=phone_no, query=query)
        ins.save()

        print('Entries saved!')
    return render(request, 'contact.html')
