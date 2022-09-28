const pgp = require('pg-promise')();
const db = pgp({
  user: 'admin',
  password: 'admin',
  host: 'subjects_database',
  port: 5436,
  database: 'subjects_database'
});

module.exports = db;