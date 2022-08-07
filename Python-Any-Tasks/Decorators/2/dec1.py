class Store(object):
    def get_food(self, username, food):
        if username != 'admin':
            raise Exception("This user is not allowed to get food")
        return self.storage.get(food)

    def put_food(self, username, food):
        if username != 'admin':
            raise Exception("This user is not allowed to get food")
        return self.storage.put(food)


def check_is_admin(username):
    if username != 'admin':
        raise Exception("This user is not allowed to get food")


class Storage2(object):
    def get_food(self, username, food):
        check_is_admin(username)
        return self.storage.get(food)

    def put_food(self, username, food):
        check_is_admin(username)
        return self.storage.put(food)


def check_is_admin2(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper


class Storage3(object):
    @check_is_admin2
    def get_food(self, username, food):
        return self.storage.get(food)

    @check_is_admin2
    def put_food(self, username, food):
        return self.storage.put(food)
