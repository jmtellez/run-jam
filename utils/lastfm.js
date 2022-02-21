const express = require('express');
const axios = require('axios');
const res = require('express/lib/response');
if (process.env.NODE_ENV !== 'production') {
    require('dotenv').config();
}



function getTopTracks(){
    axios.get('http://ws.audioscrobbler.com/2.0/',{
        params:{
            method: 'chart.gettoptracks',
            api_key: process.env.LASTFMAPIKEY,
            format: 'json',
            limit: 100
        }
    }).then(function(response){
        // console.log(response.data.tracks.track[0]);
        console.log(response.data.tracks);
        // tracks = response.data.tracks;
        return response.data.tracks;
    }).catch(function(error){
        console.log(error);
    })
}

module.exports = {
    getTopTracks
}