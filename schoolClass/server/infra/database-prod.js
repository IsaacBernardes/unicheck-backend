const pgp = require('pg-promise')();
const db = pgp({
  user: 'admin',
  password: 'admin',
  host: 'school_classes_database',
  port: 5435,
  database: 'school_classes_database'
});

module.exports = db;