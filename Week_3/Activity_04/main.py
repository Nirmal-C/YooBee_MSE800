from database import Database

db = Database()
db.create_tables()
db.insert_sample_data()

# Number of students enrolled in MSE800
db.cursor.execute("""
    SELECT COUNT(student_id)
    FROM Assign
    WHERE course_code = 'MSE800'
""")

count = db.cursor.fetchone()[0]
print("Number of students enrolled in MSE800:", count)

# List all teachers teaching MSE801
db.cursor.execute("""
    SELECT Teacher.name
    FROM Teacher
    JOIN Deliver ON Teacher.id = Deliver.teacher_id
    WHERE Deliver.course_code = 'MSE801'
""")

teachers = db.cursor.fetchall()

print("\nTeachers teaching MSE801:")
for teacher in teachers:
    print("-", teacher[0])
