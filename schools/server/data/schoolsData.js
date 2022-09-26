const database = require('../infra/database');

exports.getSchools = function () {
  return database.query('select * from public.school');
};

exports.getSchool = function (id) {
	return database.oneOrNone('select * from public.school where id = $1', [id]);
};

exports.saveSchool = function (school) {
	return database.one('insert into public.school (id, name) values ($1, $2) returning *', [school.id, school.name]);
};

exports.updateSchool = function (id, school) {
	return database.none('update public.school set name = $1 where id = $2', [school.name, id]);
};

exports.deleteSchool = function (id) {
	return database.none('delete from public.school where id = $1', [id]);
};

