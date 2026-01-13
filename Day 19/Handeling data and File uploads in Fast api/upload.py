from fastapi import FastAPI, Form, UploadFile, File
from typing import List

app = FastAPI()

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "message": "Login successful"}

#uploading file
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

#save uploaded file
@app.post("/savefile/")
async def save_upload_file(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(file.file.read())
    return {"message": f"File '{file.filename}' saved successfully"}

#multiple file upload
@app.post("/uploadfiles/")
async def upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}