from django.shortcuts import render

def index(request):
	return render(request,"siapp/index.html")
def silogic(request):
	p = request.POST["txtp"]
	r = request.POST["txtr"]
	t = request.POST["txtt"]
	si = (float(p)*float(r)*float(t))/100
	return render(request,"siapp/silogic.html",{'res':si,'p1':p,'r1':r,'t1':t})

