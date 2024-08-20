import duckdb as ddb
conn = ddb.connect()

ddb.sql("CREATE SEQUENCE seq_userid START 1;") 
ddb.sql("""
CREATE TABLE users (
id INT PRIMARY KEY default nextval('seq_userid'),
username TEXT NOT NULL,
activated BOOLEAN NOT NULL
);""")

ddb.sql("""
INSERT INTO users (
    username,
    activated
)
SELECT
    md5(random()::text)::text AS username,
    random() > 0.9 AS activated
FROM
    generate_series(1, 1000000);
""")

ddb.sql("EXPORT DATABASE 'data' (FORMAT PARQUET);")
print("Created database and saved it to ./data folder")