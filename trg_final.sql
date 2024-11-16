ALTER TRIGGER trg_employee_Ch_sync
ON Tbl_employee_Ch
AFTER INSERT, UPDATE, DELETE 
AS
BEGIN
DECLARE @Eid as int,
		@Ename as varchar (30),
		@sal as numeric 
		@des as varachar (20)
SELECT @Eid = EmpId, @Ename = EmplyeeName, @sal = Salary, @des = Designation FROM INSERTED 
	
	IF(EXISTS(SELECT * FROM INSERTED) AND EXISTS (SELECT * FROM DELETED))
	BEGIN
		IF UPDATE(EmployeeName)
			BEGIN
				UPDATE Tbl_employee_Ch_backup SET EmployeeName = @Ename
				WHERE EmpId = @Eid
			END
		IF UPDATE(Designation)
			BEGIN
			     UPDATE Tbl_employee_Ch_backup SET Designation = @des
				 WHERE Empid = @Eid
			END
		IF UPDATE (Salary)----WE CAN ADD COLUMNS IF WE WNTED 
			BEGIN
				UPDATE Tbl_employee_Ch_backup SET salary = @sal 
				WHERE Empid = @Eid
			END
	END
	ELSE IF(EXISTS(SELECT * FROM INSERTED))
	BEGIN
		INSERT INTO Tbl_employee_Ch_backup 
		SELECT * FROM INSERTED 
	END
	ELSE IF (EXISTS(SELECT * FROM DELETED))
	BEGIN
		DELETE Tbl_employee_Ch_backup
		WHERE EmpId IN (SELECT EmpId FROM DELETED) 
	END

END
