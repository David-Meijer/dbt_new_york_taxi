Project for learning DBT using the New York Taxi dataset.

optional: edit source files to be downloaded by specifying them in the files_to_download.txt in the raw_files folder
1. Run download_files.py to download all the files from the New York Taxi dataset (specified are all yellow cab files over 2024, from https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
2. Run ingestion.py to ingest the files to a seperate 'raw' database (raw_database.duckdb) in the raw_files folder.
3. Build and run the DBT project. A database file (database.duckdb) will be created in the dbt project folder.
