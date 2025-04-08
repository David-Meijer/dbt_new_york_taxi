import os
import duckdb

script_dir = os.path.dirname(os.path.abspath(__file__))
yellow_taxi_trips_file_paths =  os.path.join(script_dir, 'raw_files\\yellow_tripdata_*.parquet')
raw_database_path = os.path.join(script_dir, 'raw_files\\raw_database.duckdb') #the database that will be populated

con = duckdb.connect(raw_database_path)

con.sql('CREATE SCHEMA IF NOT EXISTS raw;')

sql ="""
DROP TABLE IF EXISTS raw.yellow_trip_data;
CREATE TABLE raw.yellow_trip_data (
     VendorID int
    ,tpep_pickup_datetime datetime
    ,tpep_dropoff_datetime datetime
    ,passenger_count int
    ,trip_distance double
    ,RatecodeID int
    ,store_and_fwd_flag varchar
    ,PULocationID int 
    ,DOLocationID int 
    ,payment_type int
    ,fare_amount double
    ,extra double
    ,mta_tax double
    ,tip_amount double
    ,tolls_amount double
    ,improvement_surcharge double
    ,total_amount double
    ,congestion_surcharge double
    ,Airport_fee double
);
"""
con.sql(sql)
print('table: raw.yellow_trip_data created')

sql = f"""
INSERT INTO raw.yellow_trip_data 
SELECT
     VendorID
    ,tpep_pickup_datetime
    ,tpep_dropoff_datetime
    ,passenger_count
    ,trip_distance
    ,RatecodeID
    ,store_and_fwd_flag
    ,PULocationID
    ,DOLocationID
    ,payment_type
    ,fare_amount
    ,extra
    ,mta_tax
    ,tip_amount
    ,tolls_amount
    ,improvement_surcharge
    ,total_amount
    ,congestion_surcharge
    ,Airport_fee
FROM read_parquet('{yellow_taxi_trips_file_paths}', union_by_name=true)
"""
con.sql(sql)
print('table: raw.yellow_trip_data ingestion completed')
