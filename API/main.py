import uvicorn

def start():
    uvicorn.run(
        "api:app",
        host="127.0.0.1",
        port=5000,
        reload=True
    )

if __name__ == "__main__":
    print("Đang khởi động server trên http://127.0.0.1:5000 ...")
    start()
