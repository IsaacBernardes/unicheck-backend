const schoolsData = require('../data/schoolsData');

exports.getSchools = function () {
  return schoolsData.getSchools();
}

exports.getSchool = function (id) {
	return schoolsData.getSchool(id);
};

exports.saveSchool = function (school) {
	return schoolsData.saveSchool(school);
};

exports.deleteSchool = function (id) {
	return schoolsData.deleteSchool(id);
};

exports.updateSchool = function (id, school) {
	return schoolsData.updateSchool(id, school);
};