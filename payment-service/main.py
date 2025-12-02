from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Payment(BaseModel):
    user: str
    amount: float


@app.get("/health")
def health():
    return {"status": "healthy", "service": "payment-service"}


@app.post("/pay")
def make_payment(payment: Payment):
    if payment.amount <= 0:
        return {"status": "fail", "message": "Invalid amount"}

    return {
        "status": "success",
        "message": f"Payment of {payment.amount} received from {payment.user}"
    }

