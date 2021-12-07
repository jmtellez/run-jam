const chai = require('chai');
const chaiHTTP = require('chai-http');
const app = require('../app');
const should = chai.should();

chai.use(chaiHTTP);

describe('Request Index', function(){
    it('This should return 200 index for working',(done)=>{
        chai.request(app).get('/').end((err,resp)=>{
            resp.should.have.status(200);
            done();
        })
    })
})