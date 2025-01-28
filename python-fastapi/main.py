from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"Shinomiyaa": "( •̀ ω •́ )✧"}


# uvicorn main:app --port 8013 --workers 13
