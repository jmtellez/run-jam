const express = require('express');
const app = express();
const port = 3000;
const accounts = require('./utils/accounts');

app.get('/', function(req,res){
    res.send("done");
});

app.get('/getaccounts',accounts);

module.exports = app.listen(port, function(){
    console.log(`Listening on port ${port}`);
})