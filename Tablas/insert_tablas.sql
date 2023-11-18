CREATE TABLE test (
    Rut INT PRIMARY KEY
);

INSERT INTO test (Rut, Name) VALUES (123, 'John');

INSERT INTO estudiante (Rut, nombredepila, apellido1, apellido2, telefono, carrera, certificadoar, email)
VALUES
('10.718.806-1', 'Agustina', 'Alvarado', 'Guerrero', 945229164, 'Pedagogía en Educación Musical', 'A0001', 'Aguerrero@userena.cl'),
('10718806-2', 'Alejandra', 'Farias', 'Jara', 977709871, 'Licenciatura en Música', 'A0002', 'Afarias@userena.cl'),
('20125515-4', 'Leonardo', 'Donoso', 'Rojas', 931035827, 'Pedagogía en Educación Musical', 'A0003', 'Ldonoso@userena.cl'),
('19384291-6', 'Lorenzo', 'Muñoz', 'Rojas', 991853161, 'Licenciatura en Música', 'A0004', 'Lrojas@userena.cl'),
('25465994-k', 'Valeria', 'Medina', 'Poblete', 915328700, 'Pedagogía en Educación Musical', 'A0005', 'Vmedina@userena.cl'),
('29665354-2', 'Violeta', 'Carvajal', 'Quezada', 911588470, 'Licenciatura en Música', 'A0006', 'Vcarvajal@userena.cl'),
('17582256-8', 'Miguel', 'Bustos', 'Godoy', 999404124, 'Licenciatura en Música', 'A0007', 'Mbustos@userena.cl'),
('18582256-6', 'Gonzalo', 'Guzman', 'Soto', 932238870, 'Licenciatura en Música con mención', 'A0008', 'Gguzman@userena.cl');



-- Bloque para cambiar formato de Rut estudiante
UPDATE estudiante
SET rut = '18582256-6'
WHERE rut = '18.582.256-7';


-- Otro ejemplo de Update.
UPDATE estudiante
SET rut = 20987,
    nombredepila = 'Sady',
    apellido1 = 'GUzman',
    apellido2 = 'Tapia',
    telefono = 12345,
    carrera = 'IngC',
    certificadoar = '0001',
    email = 'aa@bb.com';


-- ToDO: Revisar estado de CertificadoAlumnoRegular




-- Catedras BRANKO

INSERT INTO Catedras (catedra, rutest, rutprof)
VALUES
('violin 4/4', '12345678-9', '987656432-1');




-- =======================================================       ToDo Oficializa y Renueva...
-- > Oficializa
codigocontrato | rutprof  | rutest      | fechaoficializacion
---------------+----------+-------------+---------------------
1000           |10366958-9|19509928-5   | 2023-09-19
1001           |10366958-9|20125515-4   | 2023-10-29
1002           |10456432-9|19384291-6   | 2023-10-28
1004           |10331567-9|17582256-8   | 2023-09-29


instrumentos=> SELECT * FROM renueva ;
-- > Renueva
 codigodelcontrato  | rutest    | fecharenovacion
--------------------+-----------+-----------------
1000                |19509928-5 | 2024-06-05
1001                |20125515-4 | 2023-11-23
1002                |19384291-6 | 2023-11-16
1004                |17582256-8 | 2024-03-04





-- > datos alumnos de SOLICITA que pidieron anual y no fueron rechazados
numserieinst |   rutest   |  rutprof   | tipodeprestamo | fechasolicitud | estadosolicitud
722318       | 17582256-8 | 10331567-9 | Anual          | 2022-03-15     | Finalizado
541          | 20125515-4 | 10366958-9 | Anual          | 2023-03-01     | Entregado
202535       | 19384291-6 | 10456432-9 | Anual          | 2023-03-25     | Entregado
54014        | 19509928-5 | 10366958-9 | Anual          | 2023-05-05     | Entregado


-- > datos alumnos en CONTRATOCOMODATO con rut coincide a alumos de SOLICITA de arriba
 codigocontrato |       callealumno        | numcallealumno | comunaalumno | telefonoalumno | nombredirector | rutdirector | fechacontrato | fechainicio | fechatermino
----------------+--------------------------+----------------+--------------+----------------+----------------+-------------+---------------+-------------+--------------
           1000 | Mateo de Toro y Zambrano |            492 | Vicuña       | +56945229164   | Carlos Robledo | 12683514-2  | 2023-10-22    | 2023-09-19  | 2024-06-08
           1001 | Balmaceda                |            972 | Coquimbo     | +56931035827   | Carlos Robledo | 12683514-2  | 2023-10-30    | 2023-10-29  | 2023-11-27
           1002 | 5 Oriente                |            847 | La Serena    | +56991853161   | Carlos Robledo | 12683514-2  | 2023-09-19    | 2023-10-28  | 2023-11-16
           1003 | 5 Oriente                |            705 | Coquimbo     | +56915328700   | Carlos Robledo | 12683514-2  | 2023-10-21    | 2023-09-16  | 2024-07-07
           1004 | 5 Oriente                |            908 | Vicuña       | +56999404124   | Carlos Robledo | 12683514-2  | 2023-09-20    | 2023-09-29  | 2024-03-10


instrumentos=> SELECT * FROM estudiante ;
    rut     | nombredepila | apellido1 | apellido2 |   telefono   |              carrera               | certificadoar |        email
------------+--------------+-----------+-----------+--------------+------------------------------------+---------------+----------------------
 19509928-5 | Agustina     | Alvarado  | Guerrero  | +56945229164 | Pedagogía en Educación Musical     | A0001         | Aguerrero@userena.cl
 10718806-2 | Alejandra    | Farias    | Jara      | +56977709871 | Licenciatura en Música             | A0002         | Afarias@userena.cl
 20125515-4 | Leonardo     | Donoso    | Rojas     | +56931035827 | Pedagogía en Educación Musical     | A0003         | Ldonoso@userena.cl
 19384291-6 | Lorenzo      | Muñoz     | Rojas     | +56991853161 | Licenciatura en Música             | A0004         | Lrojas@userena.cl
 25465994-k | Valeria      | Medina    | Poblete   | +56915328700 | Pedagogía en Educación Musical     | A0005         | Vmedina@userena.cl
 29665354-2 | Violeta      | Carvajal  | Quezada   | +56911588470 | Licenciatura en Música             | A0006         | Vcarvajal@userena.cl
 17582256-8 | Miguel       | Bustos    | Godoy     | +56999404124 | Licenciatura en Música             | A0007         | Mbustos@userena.cl
 18582256-6 | Gonzalo      | Guzman    | Soto      | +56932238870 | Licenciatura en Música con mención | A0008         | Gguzman@userena.cl

INSERT INTO oficializa (CodigoContrato, rutprof, rutest, fechaoficializacion)
VALUES
();





-- > Ingresando los valores a la tabla actualmente vacia: RENUEVA

--> VALORES A INGRESAR:
-- > Renueva
 codigodelcontrato  | rutest    | fecharenovacion
--------------------+-----------+-----------------
1000                |19509928-5 | 2024-06-05
1001                |20125515-4 | 2023-11-23
1002                |19384291-6 | 2023-11-16
1004                |17582256-8 | 2024-03-04



-- > UPDATE PARA EFECTUAR INGRESO:

INSERT INTO Renueva (codigodelcontrato, rutest, fecharenovacion)
VALUES
('1000', '19509928-5', '2024-06-05'),
('1001', '20125515-4', '2023-11-23'),
('1002', '19384291-6', '2023-11-16'),
('1004', '17582256-8', '2024-03-04');