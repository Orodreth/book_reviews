from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def create_user(self, user):
        pwd = self.bcrypt.generate_password_hash(user["pwd"])
        sql = "insert into users(name, alias, email, password, created_at, updated_at) " \
            "values(:name, :alias, :email, :password, NOW(), NOW())"
        data = {
            "name": user["name"],
            "alias": user["alias"],
            "email": user["email"],
            "password": pwd
        }

        user_id = self.db.query_db(sql, data)

        sql = "select * from users where id = :id"
        data = {
            "id": user_id
        }
        result = self.db.query_db(sql, data)

        return { "status": True, "user": result[0] }

    def login_user(self, info):
        sql = "select * from users where email = :email"
        data = {
            "email": info["email"]
        }
        result = self.db.query_db(sql, data)

        if result == None or len(result) == 0:
            return { "status": False }

        if self.bcrypt.check_password_hash(result[0]["password"], info["pwd"]):
            return { "status": True, "user": result[0] }

        return { "status": False }

    def get_user_info(self, user_id):
        sql = "select * from users where id = :id"
        data = {
            "id": user_id
        }
        return self.db.get_one(sql, data)

    def get_reviews_number_by_user_id(self, user_id):
        sql = "select count(*) as count from reviews where user_id = :id"
        data = {
            "id": user_id
        }
        result = self.db.query_db(sql, data)

        return int(result[0]["count"])

    def get_reviewed_books_by_user_id(self, user_id):
        sql = "select id, title from books where (select book_id from reviews where user_id = :id) "
        data = {
            "id": user_id
        }

        return self.db.query_db(sql, data)


