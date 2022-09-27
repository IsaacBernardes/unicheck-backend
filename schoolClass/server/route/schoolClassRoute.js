const express = require('express');
const router = express.Router();
const schoolClassService = require('../service/schoolClassService');

router.get('/schoolClass', async function (req, res) {
  const schoolClass = await schoolClassService.getSchoolsClass();
  res.json(schoolClass);
});

router.post('/schoolClass', async function (req, res) {
  const schoolClass = req.body;
  const newSchoolClass = await schoolClassService.saveSchoolClass(schoolClass);
  res.json(newSchoolClass);
});

router.put('/schoolClass/:id', async function (req, res) {
  const schoolClass = req.body;
	await schoolClassService.updateSchoolClass(req.params.id, schoolClass);
	res.end();
});

router.delete('/schoolClass/:id', async function (req, res) {
  await schoolClassService.deleteSchoolClass(req.params.id);
	res.end();
});

module.exports = router;