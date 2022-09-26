const express = require('express');
const router = express.Router();
const schoolsService = require('../service/schoolService');

router.get('/schools', async function (req, res) {
  const schools = await schoolsService.getSchools();
  res.json(schools);
});

router.post('/schools', async function (req, res) {
  const school = req.body;
  const newSchool = await schoolsService.saveSchool(school);
  res.json(newSchool);
});

router.put('/schools/:id', async function (req, res) {
  const school = req.body;
	await schoolsService.updateSchool(req.params.id, school);
	res.end();
});

router.delete('/schools/:id', async function (req, res) {
  await schoolsService.deleteSchool(req.params.id);
	res.end();
});

module.exports = router;