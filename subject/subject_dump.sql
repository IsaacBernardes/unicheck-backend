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
CREATE DATABASE new_database;
-- ddl-end --


-- object: public.subject | type: TABLE --
-- DROP TABLE IF EXISTS public.subject CASCADE;
CREATE TABLE public.subject (
	id serial NOT NULL,
	name text NOT NULL,
	id_subject_type integer NOT NULL,
	id_school integer NOT NULL,
	CONSTRAINT subject_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.subject OWNER TO postgres;
-- ddl-end --

-- object: public.subject_type | type: TABLE --
-- DROP TABLE IF EXISTS public.subject_type CASCADE;
CREATE TABLE public.subject_type (
	id serial NOT NULL,
	name text NOT NULL,
	CONSTRAINT subject_type_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.subject_type OWNER TO postgres;
-- ddl-end --

INSERT INTO public.subject_type (id, name) VALUES (E'1', E'EXATAS');
-- ddl-end --
INSERT INTO public.subject_type (id, name) VALUES (E'2', E'HUMANAS');
-- ddl-end --
INSERT INTO public.subject_type (id, name) VALUES (E'3', E'SAÚDE');
-- ddl-end --

-- object: subject_type_fk | type: CONSTRAINT --
-- ALTER TABLE public.subject DROP CONSTRAINT IF EXISTS subject_type_fk CASCADE;
ALTER TABLE public.subject ADD CONSTRAINT subject_type_fk FOREIGN KEY (id_subject_type)
REFERENCES public.subject_type (id) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --


