import psycopg2


class ConnectionBD:

    def __init__(self, dbname, host, user, password, port):
        self.connection = psycopg2.connect(dbname=dbname,
                                           host=host,
                                           user=user,
                                           password=password,
                                           port=port)
        # Создаём необходимые таблицы для работы приложения
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS links( id SERIAL PRIMARY KEY, link text not NULL)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS hashes( id_link integer, hash_link text not null, CONSTRAINT fk_link_hash"
            " FOREIGN KEY(id_link) REFERENCES links(id) ON DELETE CASCADE)"
        )
        self.connection.commit()
        cursor.close()

    def get_link(self, hash_link: str):
        cursor = self.connection.cursor()
        cursor.execute("SELECT links.link FROM links join hashes on hashes.id_link=links.id WHERE hashes.hash_link=%s",
                       (hash_link,))
        result = cursor.fetchall()
        cursor.close()
        if len(result) == 0:
            return None
        return result[0][0]

    def get_id_link(self, link):
        cursor = self.connection.cursor()
        cursor.execute("SELECT links.id FROM links WHERE links.link=%s", (link,))
        result = cursor.fetchall()
        cursor.close()
        if len(result) == 0:
            return None
        return result[0][0]

    def insert(self, link, hash_link):
        id_link = self.get_id_link(link)
        cursor = self.connection.cursor()
        if id_link is None:
            cursor.execute("INSERT INTO links  (link) VALUES (%s) RETURNING id", (link,))
            id_link = cursor.fetchall()[0][0]
        cursor.execute("INSERT INTO hashes  (id_link, hash_link) VALUES (%s, %s)", (id_link, hash_link))
        self.connection.commit()
        cursor.close()

    def is_hash_free(self, hash_link: str):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM hashes WHERE hashes.hash_link=%s", (hash_link,))
        result = cursor.fetchall()
        cursor.close()
        if len(result) == 0:
            return True
        return False

    def close(self):
        self.connection.close()