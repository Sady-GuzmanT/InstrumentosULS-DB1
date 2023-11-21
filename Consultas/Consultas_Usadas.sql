''' Toma como referencia documento: 
    https://docs.google.com/document/d/1VQyJzgVV1gXmsIAhjuolz2r5riNUH5Zb7hGrNDDUxS8/edit '''

-- --> {selected_item} se saca usando '.get()' sobre elementos ComboBox de cada consulta.

-- --> Consulta 1
SELECT * FROM estudiante;

-- --> Consulta 2

SELECT NombreDePila AS Nombre_Estudiante,
    rut AS rut_Estudiante,
    i.numSerie AS Num_Serie_Intrumento
FROM Estudiante e
INNER JOIN prestamo_eventual p ON e.rut = p.rutest
INNER JOIN Instrumento i ON p.NumSerieInst = i.NumSerie;


-- --> Consulta 3
if selected_item == "Todos":
        query = f"SELECT * FROM instrumento;"
else:
    query = f"SELECT * FROM instrumento WHERE nombre = '{selected_item}'"

-- --> Consulta 4

SELECT e.RUT AS RUT_Estudiante,
    i.NumSerie AS Num_Serie_Instrumento,
    s.EstadoSolicitud,
    COUNT(s.RutEst) AS Cant_Veces_Prestado
FROM Estudiante e
INNER JOIN Solicita s ON e.RUT = s.RutEst
INNER JOIN Instrumento i ON i.NumSerie = s.NumSerieInst
WHERE e.RUT = '{selected_item}'
GROUP BY e.RUT, s.RutEst, i.NumSerie, s.EstadoSolicitud;