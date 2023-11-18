
/* Definir
            Tipo instrumento: Que DataType?
            Rut: Int or CharVar?
            DataType en Instrumento(Medidas)

*/

-- NUM telefono se cambia a VARCHAR (15)


CREATE TABLE Encargado (
    Rut VARCHAR(12) PRIMARY KEY,
    NombreDePila VARCHAR(50),
    Apellido1 VARCHAR(50),
    Apellido2 VARCHAR(50)
);

CREATE TABLE Estudiante (
    Rut VARCHAR(12) PRIMARY KEY,
    NombreDePila VARCHAR(50),
    Apellido1 VARCHAR(50),
    Apellido2 VARCHAR(50),
    Telefono INT,
    Carrera VARCHAR(50),
    CertificadoAR VARCHAR(50),
    Email VARCHAR(50)
);

CREATE TABLE Renueva (
    CodigoDelContrato INT REFERENCES ContratoDeComodato(CodigoContrato),
    RutEst VARCHAR(12) REFERENCES Estudiante(Rut),
    FechaRenovacion DATE
);

CREATE TABLE Oficializa (
    CodigoContrato INT REFERENCES ContratoDeComodato(CodigoContrato),
    RutProf VARCHAR(12) REFERENCES Profesor(Rut),
    RutEst VARCHAR(12) REFERENCES Estudiante(Rut),
    FechaOficializacion DATE
);

CREATE TABLE ContratoDeComodato (
    CodigoContrato INT PRIMARY KEY,
    CalleAlumno VARCHAR(50),
    NumCalleAlumno INT,
    ComunaAlumno VARCHAR(50),
    TelefonoAlumno INT,
    NombreDirector VARCHAR(50),
    RutDirector VARCHAR(12),
    FechaContrato DATE,
    FechaInicio DATE,
    FechaTermino DATE
);

CREATE TABLE Profesor (
    Rut VARCHAR(12) PRIMARY KEY,
    NombreDePila VARCHAR(50),
    Apellido1 VARCHAR(50),
    Apellido2 VARCHAR(50)
);

CREATE TABLE Ensena (
    RutEst VARCHAR(12) REFERENCES Estudiante(Rut),
    RutProf VARCHAR(12) REFERENCES Profesor(Rut)
);

CREATE TABLE Catedras (
    Catedra VARCHAR(50) PRIMARY KEY,
    RutEst VARCHAR(12) REFERENCES Estudiante(Rut),
    RutProf VARCHAR(12) REFERENCES Profesor(Rut)
);

CREATE TABLE Elige (
    RutEst VARCHAR(12) REFERENCES Estudiante(Rut),
    RutProf VARCHAR(12) REFERENCES Profesor(Rut),
    NumSerieInst VARCHAR(30) REFERENCES Instrumento(NumSerie),
    N_instrumentos INT
);

CREATE TABLE Solicita(
    RutEst VARCHAR(12) REFERENCES Estudiante(Rut),
    NumSerieInst VARCHAR(30) REFERENCES Instrumento(NumSerie),
    TipoPrestamo VARCHAR(20),
    FechaSolicitud DATE
);

CREATE TABLE Prestamo_Eventual(
    RutEst VARCHAR(12) REFERENCES Estudiante(Rut),
    RutEnc VARCHAR(12) REFERENCES Encargado(Rut),
    FechaInicio DATE,
    FechaTermino DATE
);

CREATE TABLE Gestiona(
    RutEnc VARCHAR(12) REFERENCES Encargado(Rut),
    RutEst VARCHAR(12) REFERENCES Estudiante(Rut),
    NumSerieInst VARCHAR(30) REFERENCES Instrumento(NumSerie),
    CodigoDelContrato INT REFERENCES ContratoDeComodato(CodigoContrato),
    FechaDevoInst DATE
);

CREATE TABLE Fechas_de_prestamos(
    FechasPrestamo DATE PRIMARY KEY,
    RutEnc VARCHAR(12) REFERENCES Encargado(Rut),
    RutEst VARCHAR(12) REFERENCES Estudiante(Rut),
    CodigoContrato INT REFERENCES ContratoDeComodato(CodigoContrato)
);

CREATE TABLE Instrumento(
    NumSerie VARCHAR(30) PRIMARY KEY,
    NumInventario INT,
    Nombre VARCHAR(50),
    Marca VARCHAR(50),
    Medidas INT,
    Avaluo INT,
    Estado VARCHAR(50),
    Cantidad INT
);

/* ======================================================== */


-- ToDo: Actualizar Campos RUT TIPO


Estudiante: Rut
Encargado: Rut
Profesor: Rut
Renueva: RutEst
Oficializa: RutEst, RutProf
ContratoDeComodato: RutDirector
Ensena: RutEst, RutProf
Catedra: RutEst, RutProf
Elige: RutEst, RutProf
Solicita: RutEst
Prestamo_eventual: RutEst, RutProf
Gestiona: RutEnc, RutProf
Fechas_de_prestamos: RutEnc, RutProf

Solicita: TipoPrestamo



ALTER TABLE estudiante
ALTER COLUMN rut TYPE VARCHAR(12);


ALTER TABLE Encargado
ALTER COLUMN rut TYPE VARCHAR(12);


ALTER TABLE Profesor
ALTER COLUMN rut TYPE VARCHAR(12);


ALTER TABLE Renueva
ALTER COLUMN RutEst TYPE VARCHAR(12);


ALTER TABLE Oficializa
ALTER COLUMN RutEst TYPE VARCHAR(12),
ALTER COLUMN RutProf TYPE VARCHAR(12);


ALTER TABLE ContratoDeComodato
ALTER COLUMN RutDirector TYPE VARCHAR(12);

ALTER TABLE Ensena
ALTER COLUMN RutEst TYPE VARCHAR(12),
ALTER COLUMN RutProf TYPE VARCHAR(12);

ALTER TABLE Catedras
ALTER COLUMN RutEst TYPE VARCHAR(12),
ALTER COLUMN RutProf TYPE VARCHAR(12);


ALTER TABLE Elige
ALTER COLUMN RutEst TYPE VARCHAR(12),
ALTER COLUMN RutProf TYPE VARCHAR(12);

ALTER TABLE Solicita
ALTER COLUMN RutEst TYPE VARCHAR(12);

ALTER TABLE Prestamo_eventual
ALTER COLUMN RutEst TYPE VARCHAR(12),
ALTER COLUMN RutEnc TYPE VARCHAR(12);

ALTER TABLE Gestiona
ALTER COLUMN RutEnc TYPE VARCHAR(12),
ALTER COLUMN RutEst TYPE VARCHAR(12);

ALTER TABLE Fechas_de_prestamos
ALTER COLUMN RutEnc TYPE VARCHAR(12),
ALTER COLUMN RutEst TYPE VARCHAR(12);

ALTER TABLE Solicita
ALTER COLUMN TipoPrestamo TYPE VARCHAR(20);

ALTER TABLE estudiante
ALTER COLUMN rut TYPE VARCHAR(12);

ALTER TABLE Renueva
ALTER COLUMN RutEst TYPE VARCHAR(12);


UPDATE estudiante
SET rut = 20987,
    nombredepila = 'Sady',
    apellido1 = 'GUzman',
    apellido2 = 'Tapia',
    telefono = 12345,
    carrera = 'IngC',
    certificadoar = '0001',
    email = 'aa@bb.com';


CREATE TABLE test (
    Rut INT PRIMARY KEY
);

INSERT INTO test (Rut, Name) VALUES (123, 'John');

INSERT INTO test (Rut) VALUES (44);

INSERT INTO estudiante (Rut) VALUES (44);

INSERT INTO estudiante (Rut) VALUES (44-23.23);