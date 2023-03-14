from django.shortcuts import render

# Create your views here.
def ifcondition(request):
    d={'a':10,'b':20}
    return render(request,'if_condition.html',context=d) 
def ifelse(request):
    d={'a':10,'b':20}
    return render(request,'if_else.html',context=d)
def ifelif(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'if_elif.html',context=d)
def nestedif(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'nested_if.html',context=d)
def forloop(request):
    d={'a':'vani'}
    return render(request,'for_loop.html',context=d)