from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://perkrucible.vercel.app",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    print("remove-bg: request received")

    from rembg import remove
    print("remove-bg: rembg imported")

    input_bytes = await file.read()
    print("remove-bg: file read, bytes =", len(input_bytes))

    output_bytes = remove(input_bytes)
    print("remove-bg: background removed, output bytes =", len(output_bytes))

    return Response(content=output_bytes, media_type="image/png")