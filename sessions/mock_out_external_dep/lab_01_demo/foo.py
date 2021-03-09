class Database:
    def __init__(self, size):
        self.storage = []
        self.size = size

    def add(self, num):
        if len(self.storage) >= self.size:
            raise OverflowError("storage is already full.")
        self.storage.append(num)
        return True

    def get_all(self):
        return self.storage


my_database = Database(5)


def store_num(num):
    if not isinstance(num, int):
        raise ValueError(f"expected to receive integer, got {num}")
    return my_database.add(num)
