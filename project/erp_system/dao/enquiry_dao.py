from config.db_config import DBConfig


class EnquiryDao:

    # Save Enquiry
    def save_enquiry(self, enquiry):

        conn = DBConfig.get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO enquiry
        (name, phone, email, course, source, status, remark)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        data = (
            enquiry.getName(),
            enquiry.getPhone(),
            enquiry.getEmail(),
            enquiry.getCourse(),
            enquiry.getSource(),
            enquiry.getStatus(),
            enquiry.getRemark()
        )

        cursor.execute(query, data)
        conn.commit()

        cursor.close()
        conn.close()


    # View All Enquiries
    def get_all_enquiries(self):

        conn = DBConfig.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM enquiry"

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows


    # Delete Enquiry
    def delete_enquiry(self, enquiry_id):

        conn = DBConfig.get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM enquiry WHERE enquiry_id=%s"

        cursor.execute(query, (enquiry_id,))
        conn.commit()

        cursor.close()
        conn.close()


    # Update Enquiry
    def update_enquiry(self, enquiry):

        conn = DBConfig.get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE enquiry
        SET name=%s,
            phone=%s,
            email=%s,
            course=%s,
            source=%s,
            status=%s,
            remark=%s
        WHERE enquiry_id=%s
        """

        data = (
            enquiry.getName(),
            enquiry.getPhone(),
            enquiry.getEmail(),
            enquiry.getCourse(),
            enquiry.getSource(),
            enquiry.getStatus(),
            enquiry.getRemark(),
            enquiry.getId()
        )

        cursor.execute(query, data)
        conn.commit()

        cursor.close()
        conn.close()