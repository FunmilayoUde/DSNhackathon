create schema Bestbrain_school

CREATE TABLE Bestbrain_school.Students (
    Student_ID INT PRIMARY KEY,  -- Unique identifier for each student
    First_Name VARCHAR(50) NOT NULL,  -- Assuming a maximum length of 50 for first name
    Last_Name VARCHAR(50) NOT NULL,  -- Assuming a maximum length of 50 for last name
    Gender VARCHAR(6) CHECK (Gender IN ('Male', 'Female')) NOT NULL,  -- Gender can only be 'Male' or 'Female'
    Date_of_Birth DATE NOT NULL,  -- Date of birth field
    Admission_Date DATE NOT NULL,  -- Admission date field
    Class_Section CHAR(4) CHECK (Class_Section IN ('A', 'B', 'C', 'D')) NOT NULL,  -- Class section should be one of A, B, C, D
    Class_Level VARCHAR(4) CHECK (Class_Level IN ( 'SS1', 'SS2', 'SS3')) NOT NULL,  -- Class level choices
    Religion VARCHAR(50),  -- Assuming religion name with a max length of 50 characters
    Tribe VARCHAR(50),  -- Assuming tribe name with a max length of 50 characters
    State_of_Origin VARCHAR(50),  -- Assuming state name with a max length of 50 characters
    Parent_Name VARCHAR(60),  -- Parent name, max 100 characters
    Parent_Occupation VARCHAR(60),  -- Parent occupation, max 100 characters
    Parent_Income FLOAT NOT NULL,  -- Income range constraint
    Academic_Performance INT CHECK (Academic_Performance BETWEEN 2 AND 100),  -- Academic performance score, constraint between 2 and 100
    Attendance_Rate FLOAT CHECK (Attendance_Rate BETWEEN 10.0 AND 100.0),  -- Attendance rate as a percentage
    Special_Needs VARCHAR(5) CHECK (Special_Needs IN ('Yes', 'No'))  -- Special needs status
);

select * from Bestbrain_school.Student

CREATE TABLE Bestbrain_school.Teachers (
    Teacher_ID INT PRIMARY KEY,  -- Unique identifier for each teacher
    Student_ID INT,  -- Foreign key referencing the students table
    Marital_Status VARCHAR(20),
    Education_Level VARCHAR(50),
    Gender VARCHAR(10),
    Age INT,
    Subject_Taught VARCHAR(50),
    Degree_own VARCHAR(50),
    Parental_Status VARCHAR(20),
    Teacher_Training VARCHAR(50),
    Distance_From_Home_to_School_km DECIMAL(5, 2),
    Disability VARCHAR(50),
    Health_Issue VARCHAR(100),
    Resumption_Time TIME,
    Have_Lesson_Note BOOLEAN,
    Salary_NGN DECIMAL(12, 2),
    Teaching_Experience_Years INT,
    FOREIGN KEY (Student_ID) REFERENCES Bestbrain_school.Students (Student_ID)  -- Reference the students table
);

select * from Bestbrain_school.Teachers

CREATE TABLE Bestbrain_school.Activities (
    Activity_ID SERIAL PRIMARY KEY,  -- Unique identifier for each activity
    Student_ID INT,  -- Foreign key referencing the students table
    Activity_Type VARCHAR(100),  -- Type of the activity (e.g., sports, academics, etc.)
    Activity_Category VARCHAR(50),  -- Category of the activity (e.g., extracurricular, co-curricular)
    Frequency_of_Participation VARCHAR(50),  -- How often the student participates in the activity
    Duration_per_Session_Hours DECIMAL(5, 2),  -- Duration of each session in hours
    Impact_on_Performance VARCHAR(50),  -- Description of how the activity affects performance
    Teacher_Supervisor VARCHAR(100),  -- Name of the teacher supervising the activity
    Parental_Support BOOLEAN,  -- Whether the student receives parental support for the activity
    FOREIGN KEY (Student_ID) REFERENCES Bestbrain_school.Students (Student_ID)  -- Reference the students table
);

select * from Bestbrain_school.Activities

CREATE TABLE Bestbrain_school.Schooldata (
    Student_ID INT PRIMARY KEY,  -- Unique identifier for each student
    Teacher_Student_Ratio float,  -- Ratio of teachers to students
    Average_Teacher_Experience_Years INT,  -- Average experience of teachers in years
    Average_Class_Size INT,  -- Average number of students per class
    Scholarship_Per_Student INT,  -- School funding per student in USD
    School_Extracurricular_Activities VARCHAR(50),  -- Extracurricular activities (e.g., Sports, Arts, Both, None)
    Parental_Involvement_Score float,  -- Parental involvement score (on a scale from 1 to 10)
    School_Facilities_Rating float,  -- School facilities rating (on a scale from 1 to 10)
    Internet_Access_In_School BOOLEAN,  -- Whether the school has internet access (True/False)
    School_Distance_From_Home_km float,  -- Distance of the school from the student's home in km
    Student_Attendance_Rate float,  -- Student's attendance rate as a percentage
    Disciplinary_Actions_Taken INT,  -- Number of disciplinary actions taken against the student
    Student_Performance_Score float  -- Student's performance score (range from 20 to 100)
);

select * from Bestbrain_school.Schooldata

-- Create Classes Table
CREATE TABLE Bestbrain_school.class (
    class_id INT PRIMARY KEY,
	student_id INT NOT NULL REFERENCES Bestbrain_school.students(Student_ID) ON DELETE CASCADE,
    class_level VARCHAR(10) NOT NULL,
    class_section CHAR(2) NOT NULL,
    teacher_id INT NOT NULL REFERENCES Bestbrain_school.Teachers(Teacher_ID) ON DELETE SET NULL
   
);

select * from Bestbrain_school.class

--CREATE TABLE class_students (
    ---id SERIAL PRIMARY KEY,
    --class_id INT NOT NULL REFERENCES classes(class_id) ON DELETE CASCADE,
    --student_id INT NOT NULL REFERENCES students(Student_ID) ON DELETE CASCADE
--)
select connection_user, now()
