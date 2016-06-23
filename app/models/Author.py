from system.core.model import Model

class Author(Model):
    def __init__(self):
        super(Author, self).__init__()

    def create_author(self, name):
    	sql = "insert into authors(name, created_at, updated_at) values(:name, NOW(), NOW())"
    	data = {
    		"name": name
    	}
    	result = self.db.query_db(sql, data)

    	return { "status": True, "author_id": result}

    def get_all_authors(self):
    	sql = "select * from authors"
    	return self.db.query_db(sql)