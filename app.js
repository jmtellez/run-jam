const express = require('express');
const app = express();
const port = 3000;
const accounts = require('./utils/accounts');
const dotenv = require('dotenv').config()

app.get('/', function(req,res){
    res.send("done");
});

app.get('/getaccounts',accounts.accounts);
app.get('/getAccountsTwo', accounts.accountsTwo);

module.exports = app.listen(port, function(){
    console.log(`Listening on port ${port}`);
    console.log(process.env.FULLNAME);
})