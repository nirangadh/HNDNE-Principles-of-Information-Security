-- taxila-db.sql: builds a small copy of Taxila College's SIS (Student Information System) database
-- for the Day 7 lab, full tier.
--
-- Run it on your own Kali virtual machine only, as the database administrator:
--     sudo mariadb < taxila-db.sql
--
-- Every row below is invented. No real student appears in it. This is the kind of realistic
-- but not real data that masking gives a test system: the shape of the real data, without the people.
--
-- The script creates the database and its two tables, and fills them. It creates no accounts:
-- you create the account the portal uses yourself, in the lab, with only the rights it needs.
-- To remove everything it made:
--     sudo mariadb -e 'DROP DATABASE `taxila-db`;'

CREATE DATABASE IF NOT EXISTS `taxila-db`;
USE `taxila-db`;

-- One row for each student: an identifier, a programme and a campus.
CREATE TABLE IF NOT EXISTS students (
  student_id VARCHAR(12) NOT NULL PRIMARY KEY,
  programme  VARCHAR(40) NOT NULL,
  campus     VARCHAR(10) NOT NULL
);

-- One row for each grade: which student, which module, and the mark.
CREATE TABLE IF NOT EXISTS grades (
  student_id VARCHAR(12) NOT NULL,
  module     VARCHAR(6)  NOT NULL,
  mark       INT         NOT NULL,
  PRIMARY KEY (student_id, module)
);

INSERT IGNORE INTO students (student_id, programme, campus) VALUES
  ('student01', 'Diploma in Computing', 'Colombo'),
  ('student02', 'Diploma in Computing', 'Colombo'),
  ('student03', 'Diploma in Business',  'Kandy'),
  ('student04', 'Diploma in Design',    'Colombo'),
  ('student05', 'Diploma in Computing', 'Kandy'),
  ('student06', 'Diploma in Business',  'Colombo');

INSERT IGNORE INTO grades (student_id, module, mark) VALUES
  ('student01', 'M1', 58), ('student01', 'M2', 61),
  ('student02', 'M1', 72), ('student02', 'M2', 66),
  ('student03', 'M1', 49), ('student03', 'M2', 55),
  ('student04', 'M1', 81), ('student04', 'M2', 77),
  ('student05', 'M1', 63), ('student05', 'M2', 59),
  ('student06', 'M1', 70), ('student06', 'M2', 68);

SELECT 'taxila-db is ready: 6 students, 12 grades' AS status;
