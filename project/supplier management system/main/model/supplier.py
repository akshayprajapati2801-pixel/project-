class Admin:

    def __init__(self, admin_id=None, username=None, password=None):
        self.admin_id = admin_id
        self.username = username
        self.password = password

    def __str__(self):
        return f"Admin(ID={self.admin_id}, Username={self.username})"