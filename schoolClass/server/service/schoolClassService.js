const schoolClassData = require('../data/schoolClassData');

exports.getSchoolsClass = function () {
  return schoolClassData.getSchoolsClass();
}

exports.getSchoolClass = function (id) {
	return schoolClassData.getSchoolClass(id);
};

exports.saveSchoolClass = function (schoolClass) {
	return schoolClassData.saveSchoolClass(schoolClass);
};

exports.deleteSchoolClass = function (id) {
	return schoolClassData.deleteSchoolClass(id);
};

exports.updateSchoolClass = function (id, schoolClass) {
	return schoolClassData.updateSchoolClass(id, schoolClass);
};