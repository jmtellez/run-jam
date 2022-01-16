const express = require('express');
const res = require('express/lib/response');
const app = express();
const port = 3000;

function accounts(req, res){
    res.send("accounts information");
}
function accountsTwo(req, res){
    res.send("this is second accounts");
}
// module.exports = function accounts(req, res){
//     res.send("accounts information");
// }
module.exports = {
    accounts,
    accountsTwo
}