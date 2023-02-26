import polars as pl

# show csv files in data directory with python
import os

csv_files = [file for file in os.listdir('data') if file.endswith('.csv')]

print(f"data dir containes the following .csv files: {csv_files}")
for file in csv_files:
    # read csv file
    df = pl.read_csv(f"data/{file}")
    # convert to parquet
    df.write_parquet(f"data-parquet/{file.replace('.csv', '.parquet')}")
    print(f"converted {file} to parquet")