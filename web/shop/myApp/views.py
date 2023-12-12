from django.shortcuts import render
from.models import Details
from django.http import HttpResponse
from django.template import loader


def home(request):
    return render(request,"shop/index.html")
def login(request):
    return render(request,'shop/login.html')

def signup(request):
    return render(request,'shop/signup.html')

def forgotpassword(request):
    return render(request,'shop/forgotpassword.html')

def studentform(request):
    return render(request,'student/studentform.html')

def transferToFile(request):
    sname = request.POST['txtName']
    regno = request.POST['txtRegno']
    mark1 = int(request.POST['txtMark1'])
    mark2 = int(request.POST['txtMark2'])
    content = f"{sname},{regno},total Marks:{mark1 + mark2}\n"
    with open("D:/S5/PYTHON LAB/text.txt", "a") as outfile:
        outfile.write(content)
        status = 'Content Saved on File'
        val=oddEven(mark1)
        content = {
            'status': status,
            'tstatus': val }
    return render(request, 'student/studentform.html', content)

def ValidateMobile(request):
    context={}
    if request.method == "POST":
        mobilenumber = request.POST['mobileTxt']
        if len(mobilenumber) == 10:
            status = 'valid Number'
        else:
            status = 'invalid Number'
        context = {
            'status': status,
            'mobileNo': mobilenumber
        }
    return render(request, 'mobilenumber/mobilenumber.html', context)

def oddEven(m):
    if m%2==0 :
        val='Even'
    else:
        val='odd'
    return val
def table(request):
    objList = []
    template = loader.get_template('inputtotable/details.html')
    context = {}

    if request.method == "POST":
        fn = request.POST['firstname']
        sn = request.POST['secondname']
        mob = request.POST['mobileTxt']
        obj = Details()
        obj.firstName = fn
        obj.secondName = sn
        obj.mobile = mob
        obj.save()

        formDetails = Details.objects.all().values()
        for i in formDetails:
            objList.append(i)

        context = {
            'formDetails': formDetails,
        }

    print("objList:", objList)  # Add this line for debugging
    print("context:", context)  # Add this line for debugging

    return HttpResponse(template.render(context, request))


def input(request):
    return render(request,'inputtotable/input.html')
