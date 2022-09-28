-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler version: 0.9.4
-- PostgreSQL version: 13.0
-- Project Site: pgmodeler.io
-- Model Author: ---

-- Database creation must be performed outside a multi lined SQL file. 
-- These commands were put in this file only as a convenience.
-- 
-- object: new_database | type: DATABASE --
-- DROP DATABASE IF EXISTS new_database;
-- ddl-end --


-- object: public.school_class | type: TABLE --
-- DROP TABLE IF EXISTS public.school_class CASCADE;
CREATE TABLE public.school_class (
	id serial NOT NULL,
	alias text NOT NULL,
	age smallint NOT NULL,
	id_unity integer NOT NULL,
	CONSTRAINT school_class_pk PRIMARY KEY (id)
);

-- object: public.school_class_students | type: TABLE --
-- DROP TABLE IF EXISTS public.school_class_students CASCADE;
CREATE TABLE public.school_class_students (
	id_school_class integer NOT NULL,
	id_student integer NOT NULL

);

-- object: public.classroom | type: TABLE --
-- DROP TABLE IF EXISTS public.classroom CASCADE;
CREATE TABLE public.classroom (
	id serial NOT NULL,
	id_school_class integer NOT NULL,
	id_subject integer NOT NULL,
	id_teacher integer NOT NULL,
	CONSTRAINT classroom_pk PRIMARY KEY (id)
);

-- object: public.attendance | type: TABLE --
-- DROP TABLE IF EXISTS public.attendance CASCADE;
CREATE TABLE public.attendance (
	id_classroom integer NOT NULL,
	day timestamp NOT NULL,
	frequency json NOT NULL,
	CONSTRAINT attendance_pk PRIMARY KEY (id_classroom)
);

-- object: public.gradles | type: TABLE --
-- DROP TABLE IF EXISTS public.gradles CASCADE;
CREATE TABLE public.gradles (
	id_classroom integer NOT NULL,
	gradles json NOT NULL
);


