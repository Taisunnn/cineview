import time

from fastapi import Request

async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    duration_ms = (end_time - start_time) * 1000

    print(f"Request to {request.url.path} took {duration_ms:.2f} ms")

    return response