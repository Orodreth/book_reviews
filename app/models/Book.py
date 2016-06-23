from system.core.model import Model

class Book(Model):
    def __init__(self):
        super(Book, self).__init__()

    def create_book(self, book):
    	sql = "insert into books(title, author_id, created_at, updated_at) values(:title, :author_id, NOW(), NOW())"
    	data = {
    		"title": book["title"],
    		"author_id": book["author_id"]
    	}
    	result = self.db.query_db(sql, data)

    	return { "status": True, "book_id": result }

    def get_reviews_by_book_id(self, book_id):
    	sql = "select a.id as book_id, b.id as review_id, b.review, b.rating, c.id as user_id, c.alias, b.created_at as review_date from books a " \
			"join reviews b on a.id = b.book_id " \
			"join users c on b.user_id=c.id " \
			"where a.id = :id " \
			"order by review_date desc"
        data = {
			"id": book_id
		}

        return self.db.query_db(sql, data)

    def get_last_3_reviews(self):
    	sql = "select a.id as book_id, a.title, b.review, b.rating, b.user_id, c.alias, b.created_at as review_date from books a " \
			"join reviews b on a.id = b.book_id " \
			"join users c on b.user_id=c.id " \
			"order by review_date desc " \
			"limit 3"
        return self.db.query_db(sql)

    def get_books_have_reviews(self):
    	sql = "select * from books where id in (select distinct(book_id) from reviews)"
    	return self.db.query_db(sql)

    def add_book(self, book):
        sql = "insert into books(title, author_id, created_at, updated_at) " \
            "values(:title, :author_id, NOW(), NOW())"
        data = {
            "title": book["title"],
            "author_id": book["author_id"]
        }
        self.db.query_db(sql, data)

        return { "status": True }

    def add_review(self, review):
    	sql = "insert into reviews(review, rating, user_id, book_id, created_at, updated_at) " \
    		"values(:review, :rating, :user_id, :book_id, NOW(), NOW())"
    	data = {
    		"review": review["review"],
    		"rating": review["rating"],
    		"user_id": review["user_id"],
    		"book_id": review["book_id"]
    	}
    	self.db.query_db(sql, data)

    	return { "status": True }

    def get_book_info(self, book_id):
        sql = "select a.id as book_id, a.title, b.name as author_name from books a " \
            "join authors b on a.author_id = b.id " \
            "where a.id = :id"
        data = {
            "id": book_id
        }
        return self.db.query_db(sql, data)[0]

    def delete_review(self, review_id):
        sql = "delete from reviews where id = :id"
        data = {
            "id": review_id
        }
        self.db.query_db(sql, data)


