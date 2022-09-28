-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler version: 0.9.4
-- PostgreSQL version: 13.0
-- Project Site: pgmodeler.io
-- Model Author: Isaac Joas Bernardes de Lima

-- Database creation must be performed outside a multi lined SQL file. 
-- These commands were put in this file only as a convenience.
-- 
-- object: new_database | type: DATABASE --
-- DROP DATABASE IF EXISTS new_database;
-- CREATE DATABASE new_database;
-- ddl-end --


-- object: public.unity | type: TABLE --
-- DROP TABLE IF EXISTS public.unity CASCADE;
CREATE TABLE public.unity (
	id serial NOT NULL,
	name text NOT NULL,
	address text NOT NULL,
	id_school integer NOT NULL,
	CONSTRAINT unity_pk PRIMARY KEY (id)
);
-- ddl-end --

-- object: public.occupation | type: TABLE --
-- DROP TABLE IF EXISTS public.occupation CASCADE;
CREATE TABLE public.occupation (
	id serial NOT NULL,
	alias text NOT NULL,
	CONSTRAINT occupation_pk PRIMARY KEY (id)
);
-- ddl-end --

INSERT INTO public.occupation (id, alias) VALUES (E'1', E'GESTOR');
-- ddl-end --
INSERT INTO public.occupation (id, alias) VALUES (E'2', E'PROFESSOR');
-- ddl-end --
INSERT INTO public.occupation (id, alias) VALUES (E'3', E'ESTUDANTE');
-- ddl-end --

-- object: public.unity_users | type: TABLE --
-- DROP TABLE IF EXISTS public.unity_users CASCADE;
CREATE TABLE public.unity_users (
	id_user text NOT NULL,
	accepted boolean DEFAULT false,
	id_unity integer NOT NULL,
	id_occupation integer NOT NULL

);
-- ddl-end --

-- object: unity_fk | type: CONSTRAINT --
-- ALTER TABLE public.unity_users DROP CONSTRAINT IF EXISTS unity_fk CASCADE;
ALTER TABLE public.unity_users ADD CONSTRAINT unity_fk FOREIGN KEY (id_unity)
REFERENCES public.unity (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE;
-- ddl-end --

-- object: occupation_fk | type: CONSTRAINT --
-- ALTER TABLE public.unity_users DROP CONSTRAINT IF EXISTS occupation_fk CASCADE;
ALTER TABLE public.unity_users ADD CONSTRAINT occupation_fk FOREIGN KEY (id_occupation)
REFERENCES public.occupation (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE;
-- ddl-end --


