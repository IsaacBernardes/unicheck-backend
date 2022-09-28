const httpProxy = require('express-http-proxy');
const express = require('express');
const app = express();
var logger = require('morgan');

app.use(logger('dev'));

function selectProxyHost(req) {
    if (req.path.startsWith('/schools'))
        return 'schools_service/schools';
    else if (req.path.startsWith('/schoolClass'))
        return 'schoolClass_service/schoolClass';
    else if (req.path.startsWith('/subjects'))
        return 'subjects_service/subjects';
    else if (req.path.startsWith('/unities'))
        return 'unities_service/unities';
    else if (req.path.startsWith('/users'))
        return 'users_service/users';
    else   
        return 'schools_service/schools';
}

app.use((req, res, next) => {
    httpProxy(selectProxyHost(req))(req, res, next);
});

app.listen(10000, () => {
    console.log('API Gateway running!');
});