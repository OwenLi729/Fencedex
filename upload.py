import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://user:password@host/db")

for file in os.listdir("csv_files"):
    if file.endswith(".csv"):
        df = pd.read_csv(f"csv_folder/{file}")
        df.to_sql("my_data", engine, if_exists="append", index=False)
