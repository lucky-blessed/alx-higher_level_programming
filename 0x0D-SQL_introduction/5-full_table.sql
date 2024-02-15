-- Prints the full description of the table first_table

-- Print the full description using INFORMATION_SHEMA
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABKE_NAME = 'first_table';
