from fastapi import FastAPI
from pydantic import BaseModel
from ia.testopenia import Document, Profe


app = FastAPI()

#correr la aplicacion en cmd con:
#uvicorn main:app --port= #puerto
#para cambiar el puerto.

@app.get("/")
def index():
    return "probando servidor..."

@app.post("/Profe", status_code=200)
def Profe_endpoint(doc: Document):
    response = Profe(doc.prompt)
    return {"Profe": response[0], "tokens usados": response[1]}
