class Enquiry:

    def __init__(self, enquiry_id, name, phone, email, course, source, status, remark):
        self.enquiry_id = enquiry_id
        self.name = name
        self.phone = phone
        self.email = email
        self.course = course
        self.source = source
        self.status = status
        self.remark = remark

    # Getter Methods

    def getId(self):
        return self.enquiry_id

    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email

    def getCourse(self):
        return self.course

    def getSource(self):
        return self.source

    def getStatus(self):
        return self.status

    def getRemark(self):
        return self.remark


    # Setter Methods

    def setName(self, name):
        self.name = name

    def setPhone(self, phone):
        self.phone = phone

    def setEmail(self, email):
        self.email = email

    def setCourse(self, course):
        self.course = course

    def setSource(self, source):
        self.source = source

    def setStatus(self, status):
        self.status = status

    def setRemark(self, remark):
        self.remark = remark


    def __str__(self):
        return f"{self.enquiry_id} {self.name} {self.phone} {self.course}"