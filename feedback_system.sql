-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 19, 2025 at 07:52 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `feedback_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `teacher_name` varchar(100) DEFAULT NULL,
  `teacher_sub` varchar(100) DEFAULT NULL,
  `teaching_sem` int(11) DEFAULT NULL,
  `q1` int(11) DEFAULT NULL,
  `q2` int(11) DEFAULT NULL,
  `q3` int(11) DEFAULT NULL,
  `q4` int(11) DEFAULT NULL,
  `q5` int(11) DEFAULT NULL,
  `q6` int(11) DEFAULT NULL,
  `q7_any_comments` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`teacher_name`, `teacher_sub`, `teaching_sem`, `q1`, `q2`, `q3`, `q4`, `q5`, `q6`, `q7_any_comments`) VALUES
('6', '', 0, 1, 1, 1, 1, 1, 1, 'test1'),
('6', '', 0, 1, 1, 1, 1, 1, 1, 'test2'),
('6', '', 0, 1, 1, 1, 1, 1, 1, '122'),
('chetan', 'python', 6, 1, 1, 5, 1, 1, 1, 'test 3'),
('Shripad', 'Machine learning', 6, 1, 1, 1, 1, 1, 1, 'test5'),
('Shripad', 'Machine learning', 6, 1, 1, 1, 1, 1, 1, 'test5'),
('ajay', 'toc', 6, 1, 1, 1, 1, 1, 1, 'test5'),
('Shripad', 'Machine learning', 6, 1, 1, 1, 1, 1, 1, 'test10'),
('Shripad', 'Machine learning', 6, 1, 1, 1, 1, 1, 1, '12344'),
('Shripad', 'Machine learning', 6, 1, 1, 1, 1, 1, 1, ''),
('Shripad', 'Machine learning', 6, 1, 1, 1, 1, 1, 1, ''),
('chetan', 'python', 6, 1, 1, 1, 1, 1, 1, ''),
('ajay', 'toc', 6, 1, 1, 1, 1, 1, 1, ''),
('Shripad', 'Machine learning', 6, 5, 1, 1, 1, 1, 1, ''),
('Shripad', 'Machine learning', 6, 4, 1, 1, 1, 1, 1, ''),
('Shripad', 'Machine learning', 6, 4, 1, 1, 1, 1, 1, ''),
('Shripad', 'Machine learning', 6, 4, 1, 1, 1, 1, 1, ''),
('Shripad', 'Machine learning', 6, 3, 1, 1, 1, 1, 1, ''),
('Shripad', 'Machine learning', 6, 5, 3, 3, 5, 4, 3, 'fgagjsfjh'),
('Shripad', 'Machine learning', 6, 1, 1, 1, 1, 1, 1, 'very bad'),
('Shripad', 'Machine learning', 6, 5, 3, 3, 4, 4, 3, 'very bad teacher'),
('Shripad', 'Machine learning', 6, 1, 1, 1, 1, 1, 1, ''),
('teacher 4', 'MCD', 2, 1, 1, 1, 1, 1, 1, 'good techaer'),
('Shripad', 'Machine learning', 6, 1, 1, 1, 1, 1, 1, 'all good');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `studnet_name` varchar(100) DEFAULT NULL,
  `s_year` int(11) DEFAULT NULL,
  `s_dep` varchar(100) DEFAULT NULL,
  `s_sem` int(11) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `password` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`studnet_name`, `s_year`, `s_dep`, `s_sem`, `user_id`, `password`) VALUES
('shripad chandrakant joshi', 3, 'cse', 6, 1234, 1234),
('somnath kardkar', 4, 'entc', 8, 9876, 9876),
('Anjali salve', 3, 'cse', 6, 1342, 1342),
('chanchal', 3, 'cse', 6, 0, 0),
('stud1', 1, 'mechanical', 2, 12345678, 12345678),
('stud2', 1, 'mechanical', 2, 1234567, 1234567),
('stud3', 1, 'mechanical', 2, 123456, 123456),
('stud4', 1, 'mechanical', 2, 12345, 12345),
('stud5', 1, 'mechanical', 2, 123450, 123450);

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `teacher_name` varchar(100) DEFAULT NULL,
  `teaching_subject` varchar(100) DEFAULT NULL,
  `teaching_department` varchar(100) DEFAULT NULL,
  `teaching_sem` int(11) DEFAULT NULL,
  `teaching_year` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`teacher_name`, `teaching_subject`, `teaching_department`, `teaching_sem`, `teaching_year`) VALUES
('vithhal', 'toc', 'entc', 8, 4),
('Shripad', 'Machine learning', 'cse', 6, 3),
('ajay', 'toc', 'cse', 6, 3),
('chetan', 'python', 'cse', 6, 3),
('aditya', 'daa', 'cse', 8, 4),
('adittya', 'daaa', 'entc', 8, 4),
('teacher1', 'MCA', 'mechanical', 2, 1),
('teacher 2', 'MCB', 'mechanical', 2, 1),
('teacher 3', 'MCC', 'mechanical', 2, 1),
('teacher 4', 'MCD', 'mechanical', 2, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
