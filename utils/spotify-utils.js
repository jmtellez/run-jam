import request from 'postman-request';

const token = '<OAUTH-TOKEN>'

export const search = ({ query, type, market = 'US', limit = 1, offset = 0 }, callback) => {
    const searchURI = `https://api.spotify.com/v1/search?q=${query}&type=${type}&market=${market}&limit=${limit}&offset=${offset}`;

    request({
        url: searchURI,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        json: true
    }, (err, { body } = {}) => {
        if (err) {
            callback("Unable to connect to spotify services", undefined);
        } else if (body.error) {
            callback(body.error, undefined);
        } else {
            callback(undefined, {
                track: body.tracks.items[0].name,
                trackId: body.tracks.items[0].id,
                artist: body.tracks.items[0].artists[0].name,
                artistId: body.tracks.items[0].artists[0].id,
            });
        }
    })
}