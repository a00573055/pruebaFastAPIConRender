from fastapi import FastAPI, Form
from typing import Annotated
from pydantic import BaseModel  
from fastapi.middleware.cors import CORSMiddleware
import aiocron
import requests

app = FastAPI()

origins = ["*"]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

class FormData(BaseModel):
	primero: str
	segundo: str

@aiocron.crontab("*/5 * * * *")
async def self_ping():
	response=requests.get("https://testfastapi-y81m.onrender.com")
	print(response["message"])
	

@app.get("/")
async def root():
	return {"message": "HelloWorld"}

@app.post("/suma")
def suma(item: Annotated[FormData, Form()]):
	return str(int(item.primero) + int(item.segundo))

@app.post("/resta")
def suma(item: Annotated[FormData, Form()]):
	return str(int(item.primero) - int(item.segundo))

@app.post("/multi")
def suma(item: Annotated[FormData, Form()]):
	return str(int(item.primero) * int(item.segundo))

@app.post("/divi")
def suma(item: Annotated[FormData, Form()]):
	if (int(item.segundo) != 0):
	    return str(int(item.primero) / int(item.segundo))
	return "unable to divide by 0"
