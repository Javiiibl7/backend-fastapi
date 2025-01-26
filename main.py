from fastapi import FastAPI

app = FastAPI()

@app.get("/", operation_id="get_root")
def read_root():
    return {"message": "¡Tu backend está funcionando correctamente!"}
