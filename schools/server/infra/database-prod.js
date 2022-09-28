const pgp = require('pg-promise')();
const db = pgp({
  user: 'admin',
  password: 'admin',
  host: 'schools_database',
  port: 5434,
  database: 'school_database'
});

module.exports = db;