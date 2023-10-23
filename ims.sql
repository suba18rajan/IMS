-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 17, 2023 at 04:59 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ims`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `cid` int(25) NOT NULL,
  `name` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`cid`, `name`) VALUES
(1, 'Electronics'),
(2, 'Furnitures');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `cusid` int(25) NOT NULL,
  `cid` varchar(25) NOT NULL,
  `name` varchar(25) NOT NULL,
  `email` varchar(25) NOT NULL,
  `gender` varchar(25) NOT NULL,
  `contact` varchar(25) NOT NULL,
  `address` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`cusid`, `cid`, `name`, `email`, `gender`, `contact`, `address`) VALUES
(5, '100', 'subashini', 'suba@gmail.com', 'Female', '9876543210', 'abc\n\n'),
(6, '101', 'Jane', 'jane@gmail.com', 'Female', '9378502004', 'xyz\n\n\n'),
(7, '102', 'Tamil', 'tamil@gmail.com', 'Male', '8743467890', 'No:79,Tiruchendur\n');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `empid` int(25) NOT NULL,
  `id` varchar(25) NOT NULL,
  `name` varchar(25) NOT NULL,
  `email` varchar(25) NOT NULL,
  `gender` varchar(25) NOT NULL,
  `contact` varchar(25) NOT NULL,
  `dob` varchar(25) NOT NULL,
  `doj` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `utype` varchar(25) NOT NULL,
  `salary` varchar(25) NOT NULL,
  `address` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`empid`, `id`, `name`, `email`, `gender`, `contact`, `dob`, `doj`, `password`, `utype`, `salary`, `address`) VALUES
(1, '100', 'suba', 'suba444@gmail.com', 'Female', '8248640358', '18/07/2003', '15/08/2023', 'suba@18', 'Admin', '50000', 'xyz\n\n'),
(2, '101', 'raj', 'raj@gmail.com', 'Male', '9876543210', '02/09/2002', '15/08/2023', '987', 'Employee', '60000', 'abc\n'),
(13, '102', 'Jane', 'janaraj3627@gmail.com', 'Female', '9377572309', '20/05/2003', '30/09/2023', '1873', 'Employee', '50000', 'No.7,Kovilpatti\n'),
(18, '103', 'Mathi', 'mathi@gmail.com', 'Female', '7865465730', '03/06/1994', '20/03/2017', '1234', 'Admin', '70000', 'No:34,Dindigul\n'),
(19, '104', 'Tamil', 'tamil@gmail.com', 'Female', '9873441504', '25/09/1997', '13/09/2023', '100', 'Employee', '60000', 'No:67,Tiruchendur\n');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `pid` int(25) NOT NULL,
  `pno` varchar(25) NOT NULL,
  `category` varchar(25) NOT NULL,
  `supplier` varchar(25) NOT NULL,
  `name` varchar(25) NOT NULL,
  `price` varchar(25) NOT NULL,
  `qty` varchar(25) NOT NULL,
  `status` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`pid`, `pno`, `category`, `supplier`, `name`, `price`, `qty`, `status`) VALUES
(2, '100', 'Electronics', 'Raj', 'TV', '40000', '59', 'Active'),
(4, '101', 'Furnitures', 'Sam', 'Sofa', '20000', '35', 'Active'),
(5, '102', 'Electronics', 'Sam', 'Iron Box', '3000', '90', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `supplier`
--

CREATE TABLE `supplier` (
  `supid` int(25) NOT NULL,
  `supno` varchar(25) NOT NULL,
  `invoice` varchar(25) NOT NULL,
  `name` varchar(25) NOT NULL,
  `contact` varchar(25) NOT NULL,
  `address` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `supplier`
--

INSERT INTO `supplier` (`supid`, `supno`, `invoice`, `name`, `contact`, `address`) VALUES
(5, '100', '1', 'Raj', '9688378838', 'xyz\n'),
(6, '101', '2', 'Sam', '7889587832', 'abc\n\n');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`cusid`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`empid`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`supid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `cid` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `cusid` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `empid` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `pid` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `supplier`
--
ALTER TABLE `supplier`
  MODIFY `supid` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
