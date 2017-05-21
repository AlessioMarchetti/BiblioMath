create table authors(
    id integer primary key autoincrement not null,
    name text unique
);

create table categories(
    id integer primary key autoincrement,
    name text unique,
    id_parent int
);

insert into categories (id, name, id_parent) values (0,"root",0);

create table books(
    id integer primary key,
    title text not null
);

create table comments(
    id integer primary key autoincrement,
    id_book ref unique,
    comm text,
    aut text
);

create table aut_ref(
    id_book integer,
    id_aut integer,
    primary key (id_book, id_aut)
);

create table cat_ref(
    id_book integer,
    id_cat integer,
    primary key (id_book, id_cat)
);