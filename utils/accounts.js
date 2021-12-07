const express = require('express');
const app = express();
const port = 3000;

module.exports = function accounts(req, res){
    res.send("accounts information");
}