-- Create the 'departments' table
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

-- Create the 'employees' table with a foreign key referencing 'departments'
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Insert some data into departments
INSERT INTO departments (department_id, department_name)
VALUES (1, 'Sales'), (2, 'Marketing');

-- Insert employees, linking them to departments
INSERT INTO employees (employee_id, employee_name, department_id)
VALUES (101, 'John Doe', 1), (102, 'Jane Smith', 2);