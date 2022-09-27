const database = require('../infra/database');

exports.getSchoolsClass = function () {
  return database.query('SELECT * FROM public.school_class');
};

exports.getSchoolClass = function (id) {
	return database.oneOrNone('select * from public.school_class where id = $1', [id]);
};

exports.saveSchoolClass = function (schoolClass) {
	return database.one('insert into public.school_class (id, alias, age, id_unity) values ($1, $2, $3, $4) returning *', [schoolClass.id, schoolClass.alias, schoolClass.age, schoolClass.id_unity]);
};

exports.updateSchoolClass = function (id, schoolClass) {
	return database.none('update public.school_class set alias = $2, age = $3, id_unity = $4 where id = $1', [id, schoolClass.alias, schoolClass.age, schoolClass.id_unity]);
};

exports.deleteSchoolClass = function (id) {
	return database.none('delete from public.school_class where id = $1', [id]);
};

