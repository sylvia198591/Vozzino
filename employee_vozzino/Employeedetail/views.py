
from django.http import JsonResponse
from django.shortcuts import *
from django.views.generic import *
from django.urls import *
from Employeedetail.models import *
from Employeedetail.forms import *
# Create your views here.

class createEmployee(TemplateView):
    form_class=Employeecreateform
    model_name=Employee
    template_name = "Employeedetail/Employeecreate.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            Name = form.cleaned_data["Name"]
            Telephone = form.cleaned_data["Telephone"]
            Age = form.cleaned_data["Age"]
            if 'Profile_pic' in request.FILES:
                Profile_pic = request.FILES['Profile_pic']
            Profile_pic = form.cleaned_data["Profile_pic"]
            Email = form.cleaned_data["Email"]
            Username = form.cleaned_data["Username"]
            Password = form.cleaned_data["Password"]
            # isActive=True
            qs = Employee.objects.create(Name=Name, Telephone=Telephone,Age=Age,Profile_pic=Profile_pic,\
                    Email=Email,Username=Username,Password=Password,isActive=True)
            print("d1")
            # form.save(commit=False)
            print("d2")
            qs.save()
            print("d3")
            return JsonResponse({"message": "loginSuccess", 'status': 200})

        else:
            return render(request, self.template_name,{"form":form})

class loginEmployee(TemplateView):
    form_class=Employeelogin
    model_name=Employee
    template_name = "Employeedetail/Employeelogin.html"
    template_name1 = "Employeedetail/home.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        print("Hi0000")
        if form.is_valid():
            print("Hi1111")
            Username = form.cleaned_data["Username"]
            Password = form.cleaned_data["Password"]
            qs=Employee.objects.get(Username=Username)
            print("Hi")
            print("Active:",qs.isActive)
            if((qs.Username==Username)&(qs.Password==Password)):
                request.session['Username']=Username
                context = {}
                context["qs"] = qs
                # context["user"] = user
                print("hiiiiiiiiiiiiii")
                return render(request, self.template_name1, context)
                # return HttpResponseNotFound('<h1>Page not found</h1>')
            else:
                print("Hi2222")
                return redirect("User_login")
                # return HttpResponse('<h1>Page was not found</h1>')

        else:
            print("Hi33333")
            return render(request, self.template_name,{"form":form})

class viewEmployee(TemplateView):
    model_name=Employee
    template_name = "Employeedetail/viewEmployee.html"
    # Username = request.session["Username"]
    # def get_queryset(self):
    #
    #     return self.model_name.objects.filter(Username=request.session["Username"])
    def get(self, request, *args, **kwargs):
        # form.fields['Paymode'].queryset = Account.objects.filter(Username=request.session["Username"])
        qs=Employee.objects.all()
        print("ddddd")
        context={}
        context["viewentry"]=qs
        return render(request,self.template_name,context)

def logoutEmployee(request):
        del request.session['Username']
        return redirect("Employee_login")