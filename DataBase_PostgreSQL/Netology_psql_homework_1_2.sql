CREATE TABLE IF NOT EXISTS departments (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS employees (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	patronymic VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	department_id INT REFERENCES departments(id) DEFAULT NULL,
	superior_id INT REFERENCES employees(id) DEFAULT NULL
);



