const express = require('express');
const app = express();
const port = 3000;
const accounts = require('./utils/accounts');
const spotify = require('./utils/spotify');
//const lastfm = require('./utils/lastfm');
const axios = require('axios');
const { json } = require('express/lib/response');
if (process.env.NODE_ENV !== 'production') {
    require('dotenv').config();
}

app.get('/', function(req,res){
    res.send({"status":"healthy"});
});

app.get('/getaccounts',accounts.accounts);
app.get('/getAccountsTwo', accounts.accountsTwo);
app.get('/lastfm', accounts.lastfm);
app.get('/getPlaylistsList', async function(req,res){
    spotify.getPlaylistsList(req,res);
});
//app.get('/lastfm',lastfm.getTopTracks);

module.exports = app.listen(port, function(){
    console.log(`Listening on port ${port}`);
    // console.log(process.env.FULLNAME);
})