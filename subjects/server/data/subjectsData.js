const database = require('../infra/database');

exports.getSubjects = function () {
  return database.query('select * from public.subject');
};

exports.getSubject = function (id) {
	return database.oneOrNone('select * from public.subject where id = $1', [id]);
};

exports.saveSubject = function (subject) {
	return database.one('insert into public.subject (id, name, id_subject_type, id_school) values ($1, $2, $3, $4) returning *', [subject.id, subject.name, subject.type, subject.school]);
};

exports.updateSubject = function (id, subject) {
	return database.none('update public.subject set name = $2, id_subject_type = $3, id_school = $4 where id = $1', [id, subject.name, subject.type, subject.school]);
};

exports.deleteSubject = function (id) {
	return database.none('delete from public.subject where id = $1', [id]);
};
