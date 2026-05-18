from fastapi import FastAPI

from api.loan import router as loan_router
from api.emi import router as emi_router
from api.insurance import router as insurance_router
from api.analytics import router as analytics_router

app = FastAPI(
    title="Fintech AI Backend",
    version="1.0.0"
)

app.include_router(loan_router)
app.include_router(emi_router)
app.include_router(insurance_router)
app.include_router(analytics_router)


@app.get("/")
def home():
    return {
        "message": "AI Fintech Backend Running"
    }