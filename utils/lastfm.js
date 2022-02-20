const express = require('express');

if (process.env.NODE_ENV !== 'production') {
    require('dotenv').config();
}

function last(req,res){
    res.send("lastfm information")
}

function getTopTracks(req,res){
    res.send("process.env.FIRSTNAME")
}

module.exports = {
    getTopTracks
}