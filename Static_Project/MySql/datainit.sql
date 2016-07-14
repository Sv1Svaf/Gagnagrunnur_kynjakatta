drop database if exists kkidb;
CREATE DATABASE IF NOT EXISTS kkidb;
use kkidb;

SET FOREIGN_KEY_CHECKS=0;

create table if not exists catdb_cat(
    id int AUTO_INCREMENT not null primary key,
    reg_nr varchar(30),
    name varchar(50) not null,
    gender bool not null,
    birth date,
    registered date,
    dam_id int,
    sire_id int,
    foreign key(dam_id) references catdb_parents(id),
    foreign key(sire_id) references catdb_parents(id),
    comments varchar(50),
    type varchar(3)
);

create table if not exists catdb_ghost_cat(
    id int AUTO_INCREMENT not null primary key,
    reg_nr varchar(30),
    name varchar(50),
    birth date,
    ems varchar(20),
    microchip varchar(30),
    dam_id int,
    sire_id int,
    foreign key(dam_id) references catdb_parents(id),
    foreign key(sire_id) references catdb_parents(id)
);

create table if not exists catdb_parents(
    id int AUTO_INCREMENT primary key,
    is_ghost boolean not null,
    cat_id int,
    ghost_id int,
    foreign key(cat_id) references catdb_cat(id),
    foreign key(ghost_id) references catdb_ghost_cat(id)
);

create table if not exists catdb_cat_owners(
    id int AUTO_INCREMENT NOT NULL primary key,
    cat_id int,
    owner_id int,
    foreign key(cat_id) references catdb_cat(id),
    foreign key(owner_id) references catdb_people(id),
    regdate date
);

create table if not exists catdb_people(
    id int AUTO_INCREMENT NOT NULL primary key,
    name varchar(50) not null,
    id_num varchar(30) not null,
    address varchar(40),
    postal char(3),
    phone char(10),
    email varchar(30),
    member_id int,
    comment varchar(144)
);

create table if not exists catdb_imp_cat(
    id int AUTO_INCREMENT NOT NULL primary key,
    cat_id int,
    foreign key(cat_id) references catdb_cat(id),
    org_country char(3),
    org_organization varchar(10),
    org_reg_nr varchar(20),
    attachment blob
);


create table if not exists catdb_cat_EMS(
    id int AUTO_INCREMENT NOT NULL primary key,
    cat_id int,
    ems_id int,
    foreign key(cat_id) references catdb_cat(id),
    foreign key(ems_id) references catdb_EMS(id),
    reg_date date not null
);

create table if not exists catdb_EMS(
    id int AUTO_INCREMENT NOT NULL primary key,
    breed varchar(40),
    ems_key varchar(20)
);

create table if not exists catdb_neutered(
    id int AUTO_INCREMENT NOT NULL primary key,
    cat int not null,
    date date not null,
    foreign key(cat) references catdb_cat(id)
);

create table if not exists catdb_microchip(
    id int AUTO_INCREMENT NOT NULL primary key,
    cat int not null,
    microchip_nr varchar(30) not null
);

create table if not exists catdb_group(
    id int AUTO_INCREMENT NOT NULL primary key,
    breed varchar(50),
    ems varchar(50),
    groupp varchar(50)
);

create table if not exists catdb_category(
    id int AUTO_INCREMENT NOT NULL primary key,
    breed varchar(50),
    category varchar(50)
);