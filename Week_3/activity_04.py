import sqlite3
import os

class DatabaseHandler:
    def __init__(self, db_name):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, "data")
        os.makedirs(data_dir, exist_ok=True)
        self.db_file = os.path.join(data_dir, f"{db_name}.db")
        if os.path.exists(self.db_file):
            os.remove(self.db_file)

    def run(self, sql):
        conn = sqlite3.connect(self.db_file)
        conn.execute(sql)
        conn.commit()
        conn.close()

    def fetch(self, sql, multi=True):
        conn = sqlite3.connect(self.db_file)
        cur = conn.execute(sql)
        rows = cur.fetchall() if multi else cur.fetchone()
        conn.close()
        return rows


def create_tables(db):
    db.run("""
        CREATE TABLE Teacher(
            Teacher_ID INTEGER PRIMARY KEY,
            Name TEXT,
            Email TEXT,
            Company TEXT,
            Job_Title TEXT,
            Department TEXT
        )
    """)

    db.run("""
        INSERT INTO Teacher (Name, Email, Company, Job_Title, Department)
        VALUES (
            'Saveeta Bai',
            'saveeta.bai@yoobeecolleges.com',
            'Yoobee Colleges',
            'Lecturer - Technology',
            'Teaching'
        )
    """)

    db.run("""
        CREATE TABLE Student(
            Student_ID INTEGER PRIMARY KEY,
            Name TEXT,
            Email TEXT
        )
    """)

    students = [
        ("Harsha Weerathunga", "harsha.w@yoobeestudent.ac.nz"),
        ("Dinithi Abeysekara", "dinithi.abeysekara@yoobeestudent.ac.nz"),
        ("Tharushi Wijesinghe", "tharushi.w@yoobeestudent.ac.nz"),
        ("Sajith Senanayake", "sajith.s@yoobeestudent.ac.nz"),
        ("Malithi Perera", "malithi.p@yoobeestudent.ac.nz"),
        ("Kasun Jayasuriya", "kasun.j@yoobeestudent.ac.nz")
    ]

    for n, e in students:
        db.run(f"INSERT INTO Student (Name, Email) VALUES ('{n}', '{e}')")

    db.run("""
        CREATE TABLE Course(
            Course_ID INTEGER PRIMARY KEY,
            Name TEXT,
            Credit INTEGER
        )
    """)

    courses = [("MSE800", 30), ("MSE801", 30), ("MSE802", 20), ("MSE803", 25)]
    for n, c in courses:
        db.run(f"INSERT INTO Course (Name, Credit) VALUES ('{n}', {c})")

    db.run("""
        CREATE TABLE CourseDelivery(
            CourseDelivery_ID INTEGER PRIMARY KEY,
            Teacher_ID INTEGER,
            Course_ID INTEGER
        )
    """)

    deliveries = [(1, 1), (1, 2), (1, 3), (1, 4)]
    for t, c in deliveries:
        db.run(f"INSERT INTO CourseDelivery (Teacher_ID, Course_ID) VALUES ({t}, {c})")

    db.run("""
        CREATE TABLE CourseAssign(
            CourseAssign_ID INTEGER PRIMARY KEY,
            Student_ID INTEGER,
            Course_ID INTEGER
        )
    """)

    assigns = [
        (1,1),(1,2),(1,3),(1,4),
        (2,1),(2,2),
        (3,1),(3,2),(3,3),
        (4,1),(4,2),(4,4),
        (5,3),(5,4),
        (6,2),(6,3),
        (4,4)
    ]

    for s, c in assigns:
        db.run(f"INSERT INTO CourseAssign (Student_ID, Course_ID) VALUES ({s}, {c})")


def main():
    db = DatabaseHandler("W3_A4_DB")
    create_tables(db)

    count = db.fetch("""
        SELECT COUNT(*)
        FROM CourseAssign
        WHERE Course_ID = (SELECT Course_ID FROM Course WHERE Name='MSE800')
    """, multi=False)[0]

    print("Students in MSE800:", count)

    teachers = db.fetch("""
        SELECT Name
        FROM Teacher
        WHERE Teacher_ID IN (
            SELECT Teacher_ID
            FROM CourseDelivery
            WHERE Course_ID = (SELECT Course_ID FROM Course WHERE Name='MSE801')
        )
    """)

    print("Teachers for MSE801:")
    for t in teachers:
        print("-", t[0])


if __name__ == "__main__":
    main()
