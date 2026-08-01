from dao.enquiry_dao import EnquiryDao


class EnquiryService:

    def __init__(self):
        self.dao = EnquiryDao()


    # Save Enquiry
    def save_enquiry(self, enquiry):
        self.dao.save_enquiry(enquiry)


    # Get All Enquiries
    def get_all_enquiries(self):
        return self.dao.get_all_enquiries()


    # Delete Enquiry
    def delete_enquiry(self, enquiry_id):
        self.dao.delete_enquiry(enquiry_id)


    # Update Enquiry
    def update_enquiry(self, enquiry):
        self.dao.update_enquiry(enquiry)