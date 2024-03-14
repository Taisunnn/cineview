import requests
import pandas as pd
from sqlalchemy import create_engine

from airflow.hooks.base import BaseHook
from airflow.providers.mysql.hooks.mysql import MySqlHook


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
    titles_df = pd.DataFrame(combined)[COLUMNS].rename(columns={"title": "title_name"})

    return titles_df


def load_titles(filtered_titles: pd.DataFrame) -> None:
    airflow_conn_id = "mysql_apifun"
    table = "titles"

    # Using Basehook
    conn = BaseHook.get_connection(airflow_conn_id)
    engine = create_engine(
        f"mysql+pymysql://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}"
    )

    # Using MySqlHook
    # mysql_hook = MySqlHook(mysql_conn_id=airflow_conn_id)
    # engine = mysql_hook.get_sqlalchemy_engine({"echo": True})

    filtered_titles.to_sql(
        name=table,
        con=engine,
        if_exists="append",
        index=False,
    )


def movie_pipeline(titles_list: list) -> None:
    titles = extract_titles(titles_list)
    clean_data = transform_titles(titles)
    _ = load_titles(clean_data)
