import express from 'express';
import { search } from '../utils/spotify-utils.js';

const app = express();

app.get('/search', (req, res) => {
    search(req.query, (err, body = {}) => {
        if (err) {
            res.send(err);
        } else {
            res.send(body);
        }
    });

})

app.listen(3000, () => {
    console.log("Server listening on port 3000!");
})
