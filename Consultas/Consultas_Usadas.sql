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




--- ->>>>
-- Consultas para actualizar [UPDATE] tablas; REGISTRO

''' TODO: Registrar Profesor, Registrar Estudiante, Registrar Instrumento,
Registrar Prestamo Eventual, Registrar Prestamo Anual'''

''' Nota: usando '\d table_name' se puede obtener detalles de una tabla'''

-- Formato de UPDATE:
UPDATE NOMBRE_TABLA
SET VALUE1 = 123,
    VALUE2 = '123-abc',
    VALUE3 = 'asd';
-- En Python se puede usar {abd} para concat un string

-- Registrar Estudiante.

UPDATE estudiante
SET rut = '{rut_ingresado}',
    nombredepila = '{nombre_ingresado}',
    apellido1 = '{apellido1_ingresado}',
    apellido2 = '{apellido2_ingresado}',
    telefono = '{telefono_ingresado}',
    carrera = '{carrera_ingresada}',
    certificadoar = '{certificado_ingresado}',
    email = '{email_ingresado}';


-- Registrar Profesor.

UPDATE profesor
SET rut = '{rut_ingresado}',
    nombredepila = '{nombre_ingresado}',
    apellido1 = '{apellido1_ingresado}',
    apellido2 = '{apellido2_ingresado}';

-- Registrar Instrumento.

UPDATE instrumento
SET numserie = '{numserie_ingresado}',
    numinventario = '{num_inventario_ingresado}',
    nombre = '{nombre_ingresado}',
    marca = '{marca_ingresada}',
    medidas = '{medida_ingresada}',
    avaluo = {avaluo_ingresado},
    estado = '{estado_ingresado}';

-- Registrar Prestamo Eventual.
-- Fechas inicio y termino son tipo 'DATE' El formato es 'YYYY-MM-DD'

UPDATE prestamo_eventual
SET rutest = '{rut1_ingresado}',
    rutenc = '{rut2_ingresado}',
    numserieinst = '{num_serie_ingresado}',
    fechainicio = '{fecha1_ingresado}',
    fechatermino = '{fecha2_ingresada}';

 
-- Registrar prestamo anual.

UPDATE contratodecomodato
SET codigocontrato = {codigo_ingresado},
    callealumno = '{calle_ingresada}',
    numcallealumno = {num_calle_ingresado},
    comunaalumno = '{comuna_ingresada}',
    telefonoalumno = '{telefono_ingresado}';
    nombredirector = '{nombre_director_ingresado}'
    rutdirector = '{rut_director_ingresado}'
    fechacontrato = '{fecha_contrato_ingresada}'
    fechainicio = '{fecha_inicio_ingresada}'
    fechatermino = '{fecha_termino_ingresada}';
 
 
 
 -- ---> Creacion de Tabla de prueba para Estas UPDATE queries.
 -- Va a tener todos los campos necesarios para ingresar los datos de 
 -- la tab 3, REGISTRO

 CREATE TABLE Fechas_de_prestamos(
    Column_Name DATA_TYPE PK/REFERENCES,
);


CREATE TABLE Test_Registros(
    nombredepila VARCHAR(50), 
    apellido1 VARCHAR(50), 
    apellido2 VARCHAR(50), 
    telefono VARCHAR(50), 
    carrera VARCHAR(50), 
    certificadoar VARCHAR(50), 
    email VARCHAR(50), 
    numserie VARCHAR(50), 
    numinventario VARCHAR(50), 
    nombre VARCHAR(50), 
    marca VARCHAR(50), 
    medidas VARCHAR(50), 
    avaluo INTEGER, 
    estado VARCHAR(50), 
    rutest VARCHAR(50), 
    rutenc VARCHAR(50), 
    numserieinst VARCHAR(50), 
    codigocontrato INTEGER, 
    callealumno VARCHAR(50), 
    numcallealumno INTEGER, 
    comunaalumno VARCHAR(50), 
    telefonoalumno VARCHAR(50), 
    nombredirector VARCHAR(50), 
    rutdirector VARCHAR(50), 
    fechacontrato VARCHAR(50), 
    fechainicio VARCHAR(50), 
    fechatermino VARCHAR(50)
);





 





