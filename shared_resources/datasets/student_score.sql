-- Practice Question: student_score
-- 题目：查询分数大于 80 的学生姓名和分数
-- Created by db_practice_manager

CREATE DATABASE IF NOT EXISTS practice_student_score;
USE practice_student_score;

-- 定义表格
CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    score INT NOT NULL
);

-- 插入测试资料
INSERT INTO Student (student_id, name, score) VALUES
    (1, '张三', 95),
    (2, '李四', 78),
    (3, '王五', 88),
    (4, '赵六', 65),
    (5, '钱七', 92);

-- 练习题目：
-- 查询分数大于 80 的学生姓名和分数
-- 你的 SQL：
-- SELECT name, score FROM Student WHERE score > 80;
