import sqlite3

class Database:
    def __init__(self, db_name="university.db"):
        # Create or connect to database
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        """Create tables based on ER diagram"""

        # Teacher table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Teacher(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE,
                degree TEXT
            )
        """)

        # Student table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Student(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE
            )
        """)

        # Course table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Course(
                code TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT
            )
        """)

        # Deliver table (Teacher teaches Course)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Deliver(
                teacher_id INTEGER,
                course_code TEXT,
                PRIMARY KEY (teacher_id, course_code),
                FOREIGN KEY (teacher_id) REFERENCES Teacher(id),
                FOREIGN KEY (course_code) REFERENCES Course(code)
            )
        """)

        # Assign table (Student enrolls in Course)
        # One student can do many courses
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Assign(
                student_id INTEGER,
                course_code TEXT,
                PRIMARY KEY (student_id, course_code),
                FOREIGN KEY (student_id) REFERENCES Student(id),
                FOREIGN KEY (course_code) REFERENCES Course(code)
            )
        """)

        self.conn.commit()

    def insert_sample_data(self):
        """Insert sample records"""

        teachers = [
            (1, "Dr. Arun", "arun.kumar@yoobeecolleges.com", "PhD"),
            (2, "Dr. Mohammad", "mohammad.norouzifard@yoobeecolleges.com", "PhD"),
            (3, "Dr. Saveeta", "saveeta.bai@yoobeecolleges.com", "PhD")
        ]

        students = [
            (1, "Nirmal Unagalle", "nirmal@yoobeecolleges.com"),
            (2, "Kavindu Deshan", "kavindu@yoobeecolleges.com"),
            (3, "Sahan Ranwala", "sahan@yoobeecolleges.com"),
            (4, "Dulanjana Senarathne", "dulanjana@yoobeecolleges.com")
        ]

        courses = [
            ("MSE800", "Professional Software Engineering", "Software engineering principles"),
            ("MSE801", "Research Methods", "Research methodologies"),
            ("MSE802", "Quantum Computing", "Quantum computing basics")
        ]

        delivers = [
            (1, "MSE802"),
            (2, "MSE800"),
            (3, "MSE801")
        ]

        assigns = [
            (1, "MSE800"),
            (1, "MSE801"),
            (1, "MSE802"),
            (2, "MSE800"),
            (3, "MSE801"),
            (4, "MSE801")
        ]

        self.cursor.executemany(
            "INSERT OR IGNORE INTO Teacher VALUES (?, ?, ?, ?)", teachers
        )
        self.cursor.executemany(
            "INSERT OR IGNORE INTO Student VALUES (?, ?, ?)", students
        )
        self.cursor.executemany(
            "INSERT OR IGNORE INTO Course VALUES (?, ?, ?)", courses
        )
        self.cursor.executemany(
            "INSERT OR IGNORE INTO Deliver VALUES (?, ?)", delivers
        )
        self.cursor.executemany(
            "INSERT OR IGNORE INTO Assign VALUES (?, ?)", assigns
        )

        self.conn.commit()
