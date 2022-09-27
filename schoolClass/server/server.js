const express = require('express');
const app = express();

app.use(express.json());
app.use('/', require('./route/schoolClassRoute'))

app.listen(3000);