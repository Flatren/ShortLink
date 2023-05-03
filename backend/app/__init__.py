import random

from app.db_connection import ConnectionBD


class App:
    chars: str = "0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    count_chars: int

    def __init__(self, dbname="postgres", host="localhost", user="postgres", password="postgres", port="5432"):
        self.bd = ConnectionBD(dbname, host, user, password, port)
        self.count_chars = len(self.chars)
        self.beg = 0
        self.short_links = {}
        self.rev_short_links = {}

    def shuffle_chars(self):
        list_chars = list(self.chars)
        random.shuffle(list_chars)
        return list_chars

    def to_number_systems(self, number: int, chars):
        result = ""
        system = len(chars)
        while number > 0:
            surplus = number % system
            number = number // system
            result += chars[surplus]
        return result

    def get_hash_rand(self, link: str):
        return self.to_number_systems(abs(hash(link))//(62*62*62*62*62*62), self.shuffle_chars())

    def get_hash_static(self, link: str):
        return self.to_number_systems(abs(hash(link))//(62*62*62*62*62*62), self.chars)

    def get_short_link(self, long_link: str):
        result_hash = self.get_hash_static(long_link)
        while not self.bd.is_hash_free(result_hash):
            result_hash = self.get_hash_rand(long_link)
        self.bd.insert(long_link, result_hash)
        return result_hash

    def get_long_link(self, link_hash: str):
        return self.bd.get_link(link_hash)
