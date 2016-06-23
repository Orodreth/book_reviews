from system.core.controller import *

class Sessions(Controller):
    def __init__(self, action):
        super(Sessions, self).__init__(action)
        self.load_model("User")
   
    def index(self):
        if "user_curr" in session:
            return redirect("/books")

        return self.load_view('sessions/index.html')

    def register(self):
        user = {
            "name": request.form["name"],
            "alias": request.form["alias"],
            "email": request.form["email"],
            "pwd": request.form["pwd"],
            "pwd_confirm": request.form["pwd_confirm"]
        }

        result = self.models["User"].create_user(user)

        if result["status"] == False:
            return redirect("/")

        session["user_curr"] = result["user"]

        return redirect("/books")

    def login(self):
        info = {
            "email": request.form["email"],
            "pwd": request.form["pwd"]
        }

        result = self.models["User"].login_user(info)

        if result["status"] == False:
            return redirect("/")

        session["user_curr"] = result["user"]

        return redirect("/books")

    def logout(self):
        if "user_curr" in session:
            session.pop("user_curr")

        return redirect("/")

