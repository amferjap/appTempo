CREATE TABLE precipitaciones (
    clave_prec BIGINT AUTO_INCREMENT PRIMARY KEY,
    dia DATE,
    prob DECIMAL(5,2)
);

CREATE TABLE temperaturas (
    clave_t BIGINT AUTO_INCREMENT PRIMARY KEY,
    dia DATE,
    maxima DECIMAL(5,2)
);

CREATE TABLE humedades (
    clave_h BIGINT AUTO_INCREMENT PRIMARY KEY,
    dia DATE,
    maxima DECIMAL(5,2)
);

CREATE TABLE vientos (
    clave_v BIGINT AUTO_INCREMENT PRIMARY KEY,
    dia DATE,
    velocidad DECIMAL (5,2),
    gust DECIMAL (5,2),
    gradosº INT (3)
);

CREATE TABLE presion (
    clave_p BIGINT AUTO_INCREMENT PRIMARY KEY,
    dia DATE,
    absoluta DECIMAL (5,2),
    relativa DECIMAL (5,2)
);

CREATE TABLE solar (
    clave_u BIGINT AUTO_INCREMENT PRIMARY KEY,
    dia DATE,
    uvi DECIMAL (5,2)
);