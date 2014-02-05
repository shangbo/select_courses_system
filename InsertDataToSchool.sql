use school
SET NAMES 'utf8';

insert into Departments(departId,departName,departAddress,departPhoneNum)
					values(01,'计算机学院','上大东校区三号楼',65347567);
insert into Departments(departId,departName,departAddress,departPhoneNum)
					values(02,'通讯学院','上大东校区二号楼',65341234);
insert into Departments(departId,departName,departAddress,departPhoneNum)
					values(03,'材料学院','上大东校区四号楼',65347890);



insert into	Students(stuId,stuName,stuGender,stuBirthday,stuNativePlace,stuPhoneNum,departId)
					values(1101,'李明','男',date("1993-03-06"),'上海',"13613005486",02);
insert into	Students(stuId,stuName,stuGender,stuBirthday,stuNativePlace,stuPhoneNum,departId)
					values(1102,'刘晓明','男',date("1992-12-08"),'安徽',"18913457890",01);
insert into	Students(stuId,stuName,stuGender,stuBirthday,stuNativePlace,stuPhoneNum,departId)
					values(1103,'张颖','女',date("1993-01-05"),'江苏',"18826490423",01);
insert into	Students(stuId,stuName,stuGender,stuBirthday,stuNativePlace,stuPhoneNum,departId)
					values(1104,'刘晶晶','女',date("1994-11-06"),'上海',"13331934111",01);
insert into	Students(stuId,stuName,stuGender,stuBirthday,stuNativePlace,stuPhoneNum,departId)
					values(1105,'刘成刚','男',date("1991-06-07"),'上海',"18015872567",01);
insert into	Students(stuId,stuName,stuGender,stuBirthday,stuNativePlace,stuPhoneNum,departId)
					values(1106,'李二丽','女',date("1993-05-04"),'江苏',"18107620945",01);
insert into	Students(stuId,stuName,stuGender,stuBirthday,stuNativePlace,stuPhoneNum,departId)
					values(1107,'张晓峰','男',date("1992-08-16"),'浙江',"13912341078",01);


insert into Teachers(teaId,teaName,teaGender,teaBirthday,teaPost,teaBasicSalary,departId)
					values(0101,'陈迪茂','男',date("1973-03-06"),'副教授',3567.00,01);
insert into Teachers(teaId,teaName,teaGender,teaBirthday,teaPost,teaBasicSalary,departId)
					values(0102,'马小红','女',date("1972-12-08"),'讲师',2845.00,01);
insert into Teachers(teaId,teaName,teaGender,teaBirthday,teaPost,teaBasicSalary,departId)
					values(0201,'张心颖','女',date("1973-01-05"),'教授',4200.00,02);
insert into Teachers(teaId,teaName,teaGender,teaBirthday,teaPost,teaBasicSalary,departId)
					values(0103,'吴宝钢','男',date("1973-11-06"),'讲师',2554.00,01);


insert into Courses(courId,courName,courCredit,courTimes,departId)
					values(08305001,'离散数学',4,40,01);
insert into Courses(courId,courName,courCredit,courTimes,departId)
					values(08305002,'数据库原理',4,50,01);
insert into Courses(courId,courName,courCredit,courTimes,departId)
					values(08305003,'数据结构',4,50,01);
insert into Courses(courId,courName,courCredit,courTimes,departId)
					values(08305004,'系统结构',6,60,01);
insert into Courses(courId,courName,courCredit,courTimes,departId)
					values(08301001,'分子物理学',4,40,03);
insert into Courses(courId,courName,courCredit,courTimes,departId)
					values(08302001,'通信学',3,30,02);


insert into OpenClasses(semester,courId,teaId,workTime)
					values('2012-2013 秋季',08305001,0103,'星期三 5-8');
insert into OpenClasses(semester,courId,teaId,workTime)
					values('2012-2013 冬季',08305002,0101,'星期三 1-4');
insert into OpenClasses(semester,courId,teaId,workTime)
					values('2012-2013 冬季',08305002,0102,'星期三 1-4');
insert into OpenClasses(semester,courId,teaId,workTime)
					values('2012-2013 冬季',08305002,0103,'星期三 1-4');
insert into OpenClasses(semester,courId,teaId,workTime)
					values('2012-2013 冬季',08305003,0102,'星期五 5-8');
insert into OpenClasses(semester,courId,teaId,workTime)
					values('2013-2014 秋季',08305004,0101,'星期二 1-4');
insert into OpenClasses(semester,courId,teaId,workTime)
					values('2013-2013 秋季',08305001,0102,'星期一 5-8');
insert into OpenClasses(semester,courId,teaId,workTime)
					values('2013-2014 冬季',08305001,0101,'星期一 5-8');

				
insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade)
					values(1101,'2012-2013 秋季',08305001,0103,60,60,60);
insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade)
					values(1102,'2012-2013 秋季',08305001,0103,87,87,87);
insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade)
					values(1102,'2012-2013 冬季',08305002,0101,82,82,82);
insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade)
					values(1102,'2013-2014 秋季',08305004,0101,null,null,null);
insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade)
					values(1103,'2012-2013 秋季',08305001,0103,56,56,56);
insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade)
					values(1103,'2012-2013 冬季',08305002,0102,75,75,75);
insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade)
					values(1103,'2012-2013 冬季',08305003,0102,84,84,84);
insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade)
					values(1103,'2013-2014 秋季',08305001,0102,null,null,null);
insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade)
					values(1103,'2013-2014 秋季',08305004,0101,null,null,null);
insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade)
					values(1104,'2012-2013 秋季',08305001,0103,74,74,74);
insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade)
					values(1104,'2013-2014 冬季',08305001,0101,null,null,null);
insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade)
					values(1106,'2012-2013 秋季',08305001,0103,85,85,85);
insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade)
					values(1106,'2012-2013 冬季',08305002,0103,66,66,66);
insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade)
					values(1107,'2012-2013 秋季',08305001,0103,90,90,90);
insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade)
					values(1107,'2012-2013 冬季',08305003,0102,79,79,79);
insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade)
					values(1107,'2013-2014 秋季',08305004,0101,null,null,null);

create index idx1 on Students (departId asc,stuName desc);
create index idx2 on Courses (courName);





























					
					











