create database stock;
create table stockDaliy (
id   INT NOT NULL AUTO_INCREMENT,
symbol  varchar(30),
code    varchar(30),
name   varchar(30),
trade   varchar(30) ,
pricechange   float,
changepercent  float,
buy     float,
sell    float,
settlement   float,
open  float,
high float,
low  float,
volume  bigint,
amount   bigint,
ticktime    varchar(30),
per      double,
per_d    double,
nta      double,
pb      double,
mktcap   bigint,
nmc      bigint   ,
turnoverratio   double,
gvi        double,
gvi_d        double,
createTime timestamp,
PRIMARY KEY (id)
)ENGINE=MyISAM DEFAULT CHARSET=utf8

