CREATE DATABASE IF NOT EXISTS kkidb;
use kkidb;

SET FOREIGN_KEY_CHECKS=0;

create table if not exists db_cat(
    id int primary key,
    reg_nr varchar(30),
    name varchar(50) not null,
    gender bool not null,
    birth date not null,
    registered date,
    dam int,
    sire int,
    foreign key(dam) references db_parents(id),
    foreign key(sire) references db_parents(id),
    comments varchar(50),
    type varchar(3)
);

create table if not exists db_ghost_cat(
    id int primary key,
    reg_nr varchar(30),
    name varchar(50),
    birth date not null,
    ems varchar(20),
    microchip varchar(30),
    dam int,
    sire int,
    foreign key(dam) references db_parents(id),
    foreign key(sire) references db_parents(id)
);

create table if not exists db_parents(
    id int primary key,
    is_ghost boolean not null,
    cat int,
    ghost int,
    foreign key(cat) references db_cat(id),
    foreign key(ghost) references db_ghost_cat(id)
);

create table if not exists db_cat_owners(
    id int primary key,
    cat int,
    owner int,
    foreign key(cat) references db_cat(id),
    foreign key(owner) references db_people(id),
    regdate date
);

create table if not exists db_people(
    id int primary key,
    name varchar(50) not null,
    id_num varchar(30) not null,
    address varchar(40),
    postal char(3),
    phone char(10),
    email varchar(30),
    member_id int,
    comment varchar(144)
);

create table if not exists db_imp_cat(
    id int primary key,
    cat_id int,
    foreign key(cat_id) references db_cat(id),
    org_country char(3),
    org_organization varchar(10),
    org_reg_nr varchar(20),
    attachment blob
);


create table if not exists db_cat_EMS(
    id int primary key,
    cat_id int,
    ems_id int,
    foreign key(cat_id) references db_cat(id),
    foreign key(ems_id) references db_EMS(id),
    reg_date date not null
);

create table if not exists db_EMS(
    id int primary key,
    breed varchar(40),
    ems_key varchar(20)
);

create table if not exists db_neutered(
    id int primary key,
    cat int not null,
    date date not null,
    foreign key(cat) references db_cat(id)
);

create table if not exists db_microchip(
    id int primary key,
    cat int not null,
    microchip_nr varchar(30) not null
);

create table if not exists db_group(
    id int primary key,
    breed varchar(50),
    ems varchar(50),
    groupp varchar(50)
);

create table if not exists db_category(
    id int primary key,
    breed varchar(50),
    category varchar(50)
);