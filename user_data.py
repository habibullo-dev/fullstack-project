import sqlalchemy
import hashlib
from sqlalchemy.sql import text


engine = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/Project")

# # Create a connection
# conn = engine.connect()

# Create the table if not exists
# conn.execute(
#     text("""
# CREATE TABLE IF NOT EXISTS Users (
#     id INTEGER PRIMARY KEY AUTO_INCREMENT,
#     username VARCHAR(255) NOT NULL,
#     password VARCHAR(255) NOT NULL
# )
# """))


# Close the connection after the execution of create table statement
# conn.close()

# Reconnect to the engine to execute the sample insert statements
# conn = engine.connect()


# Generate sample hashed passwords
# username1, password1 = "thomas431", hashlib.sha256("thomaspassword".encode()).hexdigest()
# username2, password2 = "john", hashlib.sha256("mydogisgreat777".encode()).hexdigest()
# username3, password3 = "stacey2020", hashlib.sha256("Ilikeyou123".encode()).hexdigest()
# username4, password4 = "phil9999", hashlib.sha256("helloworld9999".encode()).hexdigest()
# username5, password5 = "judyBush80", hashlib.sha256("yourpass123".encode()).hexdigest()
# username6, password6 = "seventeen", hashlib.sha256("seventeenpassword".encode()).hexdigest()

# try:
#     conn.execute(
#         text("""
#         INSERT INTO Users (username, password) VALUES (:username1, :password1),
#                                                        (:username2, :password2),
#                                                        (:username3, :password3),
#                                                        (:username4, :password4),
#                                                        (:username5, :password5),
#                                                        (:username6, :password6)
#         """),
#         {
#             'username1': username1,
#             'password1': password1,
#             'username2': username2,
#             'password2': password2,
#             'username3': username3,
#             'password3': password3,
#             'username4': username4,
#             'password4': password4,
#             'username5': username5,
#             'password5': password5,
#             'username6': username6,
#             'password6': password6,
#         }
#     )
# except Exception as e:
#     print("Error occurred:", e)


# conn.execute(
#     text("""
# INSERT INTO Users (username, password) VALUES (:username1, :password1),
#                                                (:username2, :password2),
#                                                (:username3, :password3),
#                                                (:username4, :password4),
#                                                (:username5, :password5),
#                                                (:username6, :password6),
# """),
#     {
#         'username1': username1,
#         'password1': password1,
#         'username2': username2,
#         'password2': password2,
#         'username3': username3,
#         'password3': password3,
#         'username4': username4,
#         'password4': password4,
#         'username5': username5,
#         'password5': password5,
#         'username6': username6,
#         'password6': password6,
#     }
# )





# Close the connection again
# conn.close()