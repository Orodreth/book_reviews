"""
    You can also use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<id>'] = 'users#update'

    Note that the parameter can have a specified type (int, string, float, path). 
    If the type is not specified it will default to string
"""

from system.core.router import routes

routes['default_controller'] = 'Sessions'
routes["POST"]["/register"] = "Sessions#register"
routes["POST"]["/login"] = "Sessions#login"
routes["/logout"] = "Sessions#logout"

routes["/books"] = "Users#index"
routes["/users/<user_id>"] = "Users#user_detail"

routes["/books/<book_id>"] = "Books#index"
routes["/books/add"] = "Books#add"
routes["POST"]["/add_book_review"] = "Books#add_book_and_review"
routes["/delete/<book_id>/<review_id>"] = "Books#delete_review"
routes["POST"]["/add_review/<book_id>"] = "Books#add_review"
