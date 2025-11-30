-- 範例：針對考題描述生成的資料集
-- 假設考題：
-- "有一個學生資料庫，包含 Student (ID, Name, Dept) 和 Course (CourseID, Title, Credits) 以及 Enroll (StudentID, CourseID, Grade)。
-- 請寫出 SQL 查詢所有成績大於 80 分的學生姓名。"

-- 1. 建立資料表 (Schema)
CREATE TABLE IF NOT EXISTS Student (
    ID VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(50),
    Dept VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Course (
    CourseID VARCHAR(10) PRIMARY KEY,
    Title VARCHAR(50),
    Credits INT
);

CREATE TABLE IF NOT EXISTS Enroll (
    StudentID VARCHAR(10),
    CourseID VARCHAR(10),
    Grade INT,
    PRIMARY KEY (StudentID, CourseID),
    FOREIGN KEY (StudentID) REFERENCES Student(ID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);

-- 2. 插入模擬資料 (Mock Data)
INSERT INTO Student (ID, Name, Dept) VALUES 
('S001', 'Alice', 'CS'),
('S002', 'Bob', 'Math'),
('S003', 'Charlie', 'CS'),
('S004', 'David', 'Physics');

INSERT INTO Course (CourseID, Title, Credits) VALUES 
('C101', 'Database', 3),
('C102', 'Data Structure', 3),
('C103', 'Calculus', 4);

INSERT INTO Enroll (StudentID, CourseID, Grade) VALUES 
('S001', 'C101', 85), -- Alice, DB, 85
('S001', 'C102', 78),
('S002', 'C101', 90), -- Bob, DB, 90
('S002', 'C103', 60),
('S003', 'C101', 55), -- Charlie, DB, 55
('S004', 'C102', 88); -- David, DS, 88

-- 3. 驗證查詢 (User can run this to check)
-- SELECT Name FROM Student s JOIN Enroll e ON s.ID = e.StudentID WHERE e.Grade > 80;
