import requests
import pandas as pd
from sqlalchemy import create_engine

from airflow.hooks.base import BaseHook

def get_titles(title: str) -> dict:
    response = requests.get(f"https://api.jikan.moe/v4/anime?q={title}&sfw")
    
    return response.json()

def extract_titles(titles_list: list) -> list:
    combined = []
    for title in titles_list:
        titles_raw_info = get_titles(title)["data"]
        combined += titles_raw_info

    return combined

def transform_titles(combined: list) -> pd.DataFrame:
    COLUMNS = ["title", "score", "synopsis", "episodes"]
    titles_df = pd.DataFrame(combined)
    titles_df = titles_df[COLUMNS]

    return titles_df

def load_titles(filtered_titles: pd.DataFrame) -> None:

    AIRFLOW_CONN_ID = "movies"

    conn = BaseHook.get_connection(AIRFLOW_CONN_ID)
    engine = create_engine(f"mysql+pymysql://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{AIRFLOW_CONN_ID}")

    filtered_titles.to_sql(
    name=conn.schema,
    con=engine,
    if_exists="replace",
    index=False,
    )

def movie_pipeline(titles_list: list) -> None:
    titles = extract_titles(titles_list)
    clean_data = transform_titles(titles)
    _          = load_titles(clean_data)