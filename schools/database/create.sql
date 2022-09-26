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

-- object: public.school | type: TABLE --
-- DROP TABLE IF EXISTS public.school CASCADE;
CREATE TABLE public.school (
	id serial NOT NULL,
	name text NOT NULL,
	CONSTRAINT school_pk PRIMARY KEY (id)
);
-- ddl-end --
ALTER TABLE public.school OWNER TO postgres;
-- ddl-end --


