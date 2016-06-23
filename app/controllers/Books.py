from system.core.controller import *

class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)
        self.load_model("Book")
        self.load_model("Author")

    def index(self, book_id):
    	book = self.models["Book"].get_book_info(book_id)
        reviews = self.models["Book"].get_reviews_by_book_id(book_id)
    	return self.load_view("books/index.html", user = session["user_curr"], book = book, reviews = reviews)

    def add(self):
        authors = self.models["Author"].get_all_authors()
    	return self.load_view("books/add.html", authors = authors)

    def add_book_and_review(self):
        author_id = request.form["author"]
        if author_id == "0":
            result = self.models["Author"].create_author(request.form["author_new"])
            if result["status"] == False:
                return redirect("/books/add")

            author_id = result["author_id"]

        book = {
            "title": request.form["title"],
            "author_id": author_id
        }
        result = self.models["Book"].create_book(book)
        if result["status"] == False:
            return redirect("/books/add")

        book_id = result["book_id"]

        review = {
            "review": request.form["review"],
            "rating": request.form["rating"],
            "user_id": session["user"]["id"],
            "book_id": book_id
        }

        result = self.models["Book"].add_review(review)
        if result["status"] == False:
            return redirect("/books/add")

        return redirect("/books/" + str(book_id))

    def add_review(self, book_id):
        review = {
            "review": request.form["review"],
            "rating": request.form["rating"],
            "user_id": session["user"]["id"],
            "book_id": book_id
        }

        result = self.models["Book"].add_review(review)
        if result["status"] == False:
            return redirect("/books/add")

        return redirect("/books/" + str(book_id))

    def delete_review(self, book_id, review_id):
        self.models["Book"].delete_review(review_id)

        return redirect("/books/" + str(book_id))