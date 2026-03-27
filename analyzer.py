import pandas as pd
from database import get_connection

def load_questions_dataframe():

    conn = get_connection()

    query = "SELECT * FROM questions"

    df = pd.read_sql(query, conn)

    conn.close()

    return df


def category_analysis():

    df = load_questions_dataframe()

    if df.empty:
        return {}

    result = df["category"].value_counts().to_dict()

    return result