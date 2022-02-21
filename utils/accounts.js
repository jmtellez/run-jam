const express = require('express');
const res = require('express/lib/response');
const app = express();
const port = 3000;
const lastfmapi = require('./lastfm');

function accounts(req, res){
    res.send("accounts information");
}
function accountsTwo(req, res){
    res.send("this is second accounts");
}
async function lastfm(req, res){
    let tracks = await lastfmapi.getTopTracks();
    res.setHeader('Content-Type', 'application/json');
    res.send(JSON.stringify(tracks));
    //res.json(tracks);
}
// module.exports = function accounts(req, res){
//     res.send("accounts information");
// }
module.exports = {
    accounts,
    accountsTwo,
    lastfm
}