import psycopg
DSN = "postgresql://postgres:postgres@localhost:5432/postgres"
def check():
    with psycopg.connect(DSN, autocommit=True) as c:
        c.execute("create extension if not exists vector")
        c.execute("drop table if exists circuit_check; create table circuit_check (id int, embedding vector(3))")
        c.execute("insert into circuit_check values (1, '[1,2,3]'), (2, '[9,9,9]')")
        (nearest,) = c.execute("select id from circuit_check order by embedding <-> '[1,2,2]' limit 1").fetchone()
        ver = c.execute("select extversion from pg_extension where extname = 'vector'").fetchone()[0]
    assert nearest == 1, f"nearest was {nearest}"
    return f"pgvector {ver}: nearest-neighbour query returned the right row"
