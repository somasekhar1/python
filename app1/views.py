from django.shortcuts import render

# Create your views here.
def showindex(request):
    return render(request,"index.html")


def register(request):
    return render(request,"regester.html")


def savedetails(request):
    id=request.POST.get("id")
    name=request.POST.get("name")
    birth=request.POST.get("birth")
    email=request.POST.get("email")
    contact=request.POST.get("contact")
    username=request.POST.get("username")
    password=request.POST.get("password")
    address=request.POST.get("address")
    d1={"name":name,"birth":birth,"email":email,"contect":contact,"uname":username,"upass":password,"address":address}
    from firebase import firebase as fab
    fir=fab.FirebaseApplication("https://djangoweb2.firebaseio.com/",None)
    fir.put("Employee/",id,d1)
    return render(request,"regester.html",)


def login(request):
    return render(request,"login.html")


def logindetails(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    from firebase import firebase as fab
    fir = fab.FirebaseApplication("https://djangoweb2.firebaseio.com/Employee",None)
    d1=fir.get("Employee/",110)
    if d1["username"]==username and d1["password"]==password:
       return render(request,"welcome.html")
    else:
       return render(request,"login.html",{"messsage":"invalid user"})


