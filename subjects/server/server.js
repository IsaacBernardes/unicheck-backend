const express = require('express');
const app = express();

app.use(express.json());
app.use('/', require('./route/subjectsRoute'))

app.listen(3000);