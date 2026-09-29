import os


from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client


load_dotenv()


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "HW03 server is running"}


@app.get("/api/case-studies")
def get_case_studies():
    response = (
        supabase
        .table("case_studies")
        .select("*")
        .order("id", desc=False)
        .execute()
    )

    return response.data


@app.get("/api/case-studies/{slug}")
def get_case_study(slug: str):
    response = (
        supabase
        .table("case_studies")
        .select("*")
        .eq("slug", slug)
        .execute()
    )

    if not response.data:
        raise HTTPException(
            status_code=404,
            detail="Case study not found"
        )

    return response.data[0]


@app.get("/api/team")
def get_team():
    response = (
        supabase
        .table("team")
        .select("*")
        .execute()
    )

    return response.data


@app.get("/api/blog")
def get_blog():
    response = (
        supabase
        .table("blog")
        .select("*")
        .execute()
    )

    return response.data