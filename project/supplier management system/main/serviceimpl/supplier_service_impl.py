from service.login_service import LoginService
from daoimpl.login_dao_impl import LoginDAOImpl


class LoginServiceImpl(LoginService):

    def __init__(self):
        self.login_dao = LoginDAOImpl()

    def login(self, username, password):

        if username == "" or password == "":
            return None

        return self.login_dao.login(username, password)