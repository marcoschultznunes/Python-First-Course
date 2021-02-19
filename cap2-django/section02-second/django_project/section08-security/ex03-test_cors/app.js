const express = require('express')
let app = express()

const cors = require('cors')
const morgan = require('morgan')
app.use(morgan('dev'))
app.use(cors())

app.use((req, res, next) => {
    res.setHeader("Content-Security-Policy", "script-src 'self' 'unsafe-inline' https://apis.google.com");
    return next();
});

app.get('/', function(req, res){
    res.sendFile(__dirname + '/client/index.html');
});

module.exports = app
