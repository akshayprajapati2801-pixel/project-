from service.login_service import LoginService

class LoginController:

    def __init__(self):
        self.login_service = LoginService()

    def login(self, username, password):
        return self.login_service.login(username, password)