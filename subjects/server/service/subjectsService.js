const subjectsData = require('../data/subjectsData');

exports.getSubjects = function () {
  return subjectsData.getSubjects();
}

exports.getSubject = function (id) {
	return subjectsData.getSubject(id);
};

exports.saveSubject = function (subject) {
	return subjectsData.saveSubject(subject);
};

exports.deleteSubject = function (id) {
	return subjectsData.deleteSubject(id);
};

exports.updateSubject = function (id, subject) {
	return subjectsData.updateSubject(id, subject);
};