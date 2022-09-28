const httpProxy = require('express-http-proxy');
const express = require('express');
const app = express();
var logger = require('morgan');

app.use(logger('dev'));

function selectProxyHost(req) {
    if (req.path.startsWith('/schools'))
        return 'host.docker.internal:9003' + req.path;
    else if (req.path.startsWith('/schoolClass'))
        return 'host.docker.internal:9004' + req.path;
    else if (req.path.startsWith('/subjects'))
        return 'host.docker.internal:9005' + req.path;
    else if (req.path.startsWith('/unities'))
        return 'host.docker.internal:9001' + req.path;
    else if (req.path.startsWith('/invites'))
        return 'host.docker.internal:9001' + req.path;
    else if (req.path.startsWith('/users'))
        return 'host.docker.internal:9002' + req.path;
    else   
        return 'host.docker.internal:9003/schools';
}

app.use((req, res, next) => {
    httpProxy(selectProxyHost(req))(req, res, next);
});

app.listen(10000, () => {
    console.log('API Gateway running!');
});