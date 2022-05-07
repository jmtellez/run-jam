const { default: axios } = require('axios');
const { header } = require('express/lib/response');
const res = require('express/lib/response');

async function getPlaylistsList(req, res){
    let playlists;
    let config = {
        headers: {'Authorization': 'Bearer BQDJFFomUeFtM5oGdyuJgeOuqVnNpnikBJf4wfx1K-AX3DcVfSDwjDy5LQ-PNhDLdXi0QGveiXt9wiXNtBcWKpVNBCGJ49wGGaciWP_3iTUVTFcjehxacOxLEpOupSlGmoOtXeI-ax0q8QJhIJddsIVoa_GN2O7a3mIOq35wvj8EdMxTkTQ6MVOBqWVGNZaPJCBB5ONirnnxT5V81XL5Hbkj4jiTPObP8S6JIPcCdfD2KAWbSULB9WOJoNmC-2H07WS2Ovy2Cyolr7nANk99'},
        params: {'limit':1}
    } 
    await axios.get('https://api.spotify.com/v1/users/spotify/playlists', config).then((response)=>{
        playlists = response.data;
    })
    .catch((error)=>{
        console.log(error);
    })
    res.send(playlists);
}

module.exports = {
    getPlaylistsList
}