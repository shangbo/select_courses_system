create database school
CHARACTER SET 'utf8'
COLLATE 'utf8_general_ci';
	use school;
	create table Departments(
			departId int(2) not null,
			departName varchar(20) not null,
			departAddress varchar(20) not null,
			departPhoneNum int(8) not null,
			primary key (departId)
		)ENGINE=InnoDB DEFAULT CHARSET=utf8;
	create table Students(
			stuId int(4) not null,
			stuName varchar(8) not null,
			stuGender char(2) not null,
			stuBirthday date not null,
			stuNativePlace varchar(8) not null,
			stuPhoneNum char(11) not null,
			departId int(2) not null,
			primary key (stuId),
			foreign key (departId) references Departments(departId)
		)ENGINE=InnoDB DEFAULT CHARSET=utf8;
	create table Teachers(
			teaId int(4) not null,
			teaName varchar(8) not null,
			teaGender char(2) not null,
			teaBirthday date not null,
			teaPost varchar(6) not null,
			teaBasicSalary float(7,2) not null,
			departId int(2) not null,
			primary key (teaId),
			foreign key (departId) references Departments(departId),
			check(teaPost in('教授','副教授','讲师')),
    		check(teaId between 100 and 399),
    		check(teaGender in('男','女'))
		)ENGINE=InnoDB DEFAULT CHARSET=utf8;
	create table Courses(
			courId int(8) not null,
			courName varchar(10) not null,
			courCredit int(1) not null,
			courTimes int(2) not null,
			departId int(2) not null,
			primary key (courId),
			foreign key (departId) references Departments(departId)
		)ENGINE=InnoDB DEFAULT CHARSET=utf8;
	create table OpenClasses(
			semester char(14) not null,
			courId int(8) not null,
			teaId int(4) not null,
			workTime char(10) not null,
			primary key (semester,courId,teaId),
			foreign key (courId) references Courses(courId),
			foreign key (teaId) references Teachers(teaId)
		)ENGINE=InnoDB DEFAULT CHARSET=utf8;
	create table SelectCourses(
			stuId int(4) not null,
			semester char(14) not null,
			courId int(8) not null,
			teaId int(4) not null,
			regularGrade int(2),
			examGrade int(2),
			totalGrade int(2),
			primary key (stuId,semester,courId),
			foreign key (stuId) references Students(stuId),
			foreign key (semester) references OpenClasses(semester),
			foreign key (teaId) references Teachers(teaId),
			foreign key (courId) references Courses(courId),
			check(regularGrade between 0 and 100),
			check(examGrade between 0 and 100),
			check(totalGrade between 0 and 100)
		)ENGINE=InnoDB DEFAULT CHARSET=utf8;
