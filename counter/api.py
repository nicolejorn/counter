from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/hello")
def hello(request):
    return "Hello world"

@api.get("/about")
def about(request):
    return "0.1.0"