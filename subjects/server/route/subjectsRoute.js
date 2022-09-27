const express = require('express');
const router = express.Router();
const subjectsService = require('../service/subjectsService');

router.get('/subjects', async function (req, res) {
  const subjects = await subjectsService.getSubjects();
  res.json(subjects);
});

router.post('/subjects', async function (req, res) {
  const subject = req.body;
  const newSubject = await subjectsService.saveSubject(subject);
  res.json(newSubject);
});

router.put('/subjects/:id', async function (req, res) {
  const subject = req.body;
	await subjectsService.updateSubject(req.params.id, subject);
	res.end();
});

router.delete('/subjects/:id', async function (req, res) {
  await subjectsService.deleteSubject(req.params.id);
	res.end();
});

module.exports = router;