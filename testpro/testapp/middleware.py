# middleware structure 
#every customized middleware should be py class and child class of object 
#it contains two mandatory methods and three optional methods 
from django.http import HttpResponse
class login(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        #line code executed at the time of pre request
        response=self.get_response(request)# a call to next level
        #this line of code executed at th time post response
        return response
class maintenance(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        return HttpResponse("<h1>this application is in maintenance please vist after three days")
class handel_response_error(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_exception(self,request,exception):
        return HttpResponse("<h1>currently this page is facing some problume please try later<h1>")
class to_display_rised_exception(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,response):
        response=self.get_response
        return response
    def process_exception(self,request,exception)
        s1="<h1>currently this page is facing some problume please try later<h1>"
        s2="<h1>raised error is {}<h1>".format(exception.__class__.__name__)
        s3="<h1>exception is {} <h1>".format(exception)
        return HttpResponse(s1+s2+s3)