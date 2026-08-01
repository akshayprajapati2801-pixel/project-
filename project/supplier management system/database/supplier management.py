import mysql.connector

# Connect to MySQL Server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_password"
)

cursor = connection.cursor()

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS supplier_management")
cursor.execute("USE supplier_management")

# Create Admin Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
)
""")

# Create Supplier Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS supplier (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    company_name VARCHAR(150) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    gst_number VARCHAR(30) UNIQUE,
    status ENUM('Active','Inactive') DEFAULT 'Active',
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Insert Default Admin
cursor.execute("""
INSERT IGNORE INTO admin(username, password)
VALUES ('admin', 'admin123')
""")

# Insert Sample Suppliers
cursor.execute("""
INSERT IGNORE INTO supplier
(supplier_id, supplier_name, company_name, email, phone, address,
 city, state, country, gst_number, status)
VALUES
(1,'Rahul Sharma','ABC Traders','rahul@abctraders.com',
'9876543210','MG Road','Delhi','Delhi','India',
'GST123456789','Active'),

(2,'Amit Kumar','Global Electronics','amit@global.com',
'9988776655','Sector 18','Noida','Uttar Pradesh','India',
'GST987654321','Active'),

(3,'Neha Verma','Fresh Foods Pvt Ltd','neha@freshfoods.com',
'9123456789','Civil Lines','Jaipur','Rajasthan','India',
'GST456789123','Inactive')
""")

connection.commit()

print("Database Created Successfully!")
print("Tables Created Successfully!")
print("Sample Data Inserted!")

cursor.close()
connection.close()