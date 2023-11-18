-- Cambio propuesto por Maria: Num telefono deberia ser char para agregar +569. 15 largo

ALTER TABLE estudiante
ALTER COLUMN telefono TYPE VARCHAR(15);


-- Agregando el +56 .. (el 9 ya estaba puesto)
UPDATE estudiante
SET telefono = CONCAT('+56', telefono);
