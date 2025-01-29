from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/")
def hello(request):
    return {"Shinomiyaa": "( •̀ ω •́ )✧"}
