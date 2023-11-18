-- Se hacen consultas de relevancia a la necesidad de informacion del proyecto

-- > Consulta 11: Nombre de estudiantes que tienen un préstamo eventual y qué instrumento tienen

SELECT  NombreDePila AS Estudiante, 
        Nombre AS Instrumento
FROM Estudiante, Instrumento, Prestamo_eventual
WHERE Prestamo_eventual.RutEst = Estudiante.Rut
AND Prestamo_eventual.NumSerieInst = Instrumento.NumSerie;


-- > Consulta 17: Cual es el instrumento más solicitado?

SELECT instrumento, COUNT(*) AS cantidad
FROM ContratoDeComodato
GROUP BY instrumento
ORDER BY cantidad DESC
LIMIT 1;



SELECT numserieinst, COUNT(*) AS Cantidad
FROM Solicita
GROUP BY numserieinst
ORDER BY Cantidad DESC;
--LIMIT 1;


/*
--> Consulta 20: ¿Cuál es la suma del avalúo de los instrumentos prestados 
                entre las fechas ‘D-M-A’ y ‘D-M-A’ 
                para la cátedra con mayor cantidad de préstamos efectuados por contrato de comodato? 
*/

SELECT SUM(Avaluo) as AvaluoTotal
FROM instrumento AND 