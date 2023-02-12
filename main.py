from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import json
import pkg_resources
import time
import uvicorn
from starlette.responses import PlainTextResponse, RedirectResponse, JSONResponse, FileResponse





app = FastAPI()

app.mount("/static", StaticFiles(directory=pkg_resources.resource_filename(__name__, 'static')), name="static")
# app.mount("/img", StaticFiles(directory=pkg_resources.resource_filename(__name__, 'img')), name="img")


origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081","http://127.0.0.1:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Devices = [["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"]]

Devices = '{"status":"success","data":[{"name":"Router-1","ip":"1.1.1.1","status": "Managed","row": true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false}],"message":"Successfully! All records has been fetched."}'
Devices2 = '{"status":"success","data":[{"name":"Router-1","ip":"1.1.1.1","status": "Managed","row": false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":true},{"name":"Router-2","ip":"2.2.2.2","status": "Unmanaged","row":false}],"message":"Successfully! All records has been fetched."}'


@app.get("/")
async def home():
        return FileResponse('static/index.html')

        

@app.get("/getDevices")
async def home():
        return json.loads(Devices)


@app.get("/manage/")
async def manage(ip):
    time.sleep(3)
    return json.loads('{"status":"success","data":{ "ip":"'+ip+'"},"message":"Successfully! All records has been fetched."}')

@app.get("/unmanage/")
async def manage(ip):
    time.sleep(3)
    return json.loads('{"status":"success","data":{ "ip":"'+ip+'"},"message":"Successfully! All records has been fetched."}')

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, log_level="info")