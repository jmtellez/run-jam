// require csvtojson
const csv = require("csvtojson/v2");

// Convert a csv file with csvtojson


//    function getParsedMusicObject(){
//     csv()
//     .fromFile('E:/Projects/run-jam/assets/regional-global-weekly-2022-01-13.csv')
//     .then(function(jsonArrayObj){ //when parse finished, result will be emitted here.
//       return jsonArrayObj
//      })
//    }
// csv()
//   .fromFile('E:/Projects/run-jam/assets/regional-global-weekly-2022-01-13.csv')
//   .then(function(jsonArrayObj){ //when parse finished, result will be emitted here.
//      console.log(jsonArrayObj[150]); 
//    })

// let musicObject = csv().fromFile('E:/Projects/run-jam/assets/regional-global-weekly-2022-01-13.csv').then(function(jsonArrayObj){
//     return jsonArrayObj;
// });
// console.log(musicObject);

// const jsonArray=await csv().fromFile('E:/Projects/run-jam/assets/regional-global-weekly-2022-01-13.csv');
// console.log(jsonArray[150]);

const jsonArray = csv()
.fromFile('E:/Projects/run-jam/assets/regional-global-weekly-2022-01-13.csv')
.then((jsonObj)=>{
	return jsonObj;
	/**
	 * [
	 * 	{a:"1", b:"2", c:"3"},
	 * 	{a:"4", b:"5". c:"6"}
	 * ]
	 */ 
})
console.log(jsonArray);