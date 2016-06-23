from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model("User")
        self.load_model("Book")

    def index(self):
    	books = self.models["Book"].get_books_have_reviews()
    	reviews = self.models["Book"].get_last_3_reviews()
    	return self.load_view("users/index.html", user_curr = session["user_curr"], reviews = reviews, books = books)

    def user_detail(self, user_id):
        user = self.models["User"].get_user_info(user_id)
        review_num = self.models["User"].get_reviews_number_by_user_id(user_id)
        reviewed_books = self.models["User"].get_reviewed_books_by_user_id(user_id)
        print reviewed_books
    	return self.load_view("users/user_detail.html", user = user, review_num = review_num, reviewed_books = reviewed_books)

