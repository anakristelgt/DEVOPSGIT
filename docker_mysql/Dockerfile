FROM mysql:oracle

ENV MYSQL_ROOT_PASSWORD=toor
ENV MYSQL_DATABASE=fastapi 

COPY ./MOCK_DATA.sql /docker-entrypoint-initdb.d 
