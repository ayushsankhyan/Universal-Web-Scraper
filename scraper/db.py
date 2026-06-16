import psycopg2


DB_CONFIG = {
    "host": "localhost",
    "database": "scraper_db",
    "user": "postgres",
    "password": "12345"
}


def get_connection():

    return psycopg2.connect(
        host=DB_CONFIG["host"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )


def create_table():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scraped_products (
            id SERIAL PRIMARY KEY,
            url TEXT,
            title TEXT,
            price TEXT,
            stock TEXT,
            raw_record TEXT
        )
    """)

    connection.commit()

    cursor.close()
    connection.close()


def save_product(
    url,
    title,
    price,
    stock,
    raw_record
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO scraped_products
        (
            url,
            title,
            price,
            stock,
            raw_record
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s
        )
        """,
        (
            url,
            title,
            price,
            stock,
            raw_record
        )
    )

    connection.commit()

    cursor.close()
    connection.close()


def get_products():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM scraped_products
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows