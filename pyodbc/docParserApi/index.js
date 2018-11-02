const docparser = require("docparser-node");
const ObjectsToCsv = require("objects-to-csv");


var fs = require('fs');
var client = new docparser.Client(KEY);

// default impot file
const myFile = 'test.pdf'

// writes results to JSON
var writeResultJSON = (myResult) => {
  fs.writeFile("./test.json", JSON.stringify(myResult, null, 4), (err) => {
    if (err) {
        console.error(err);
        return;
    };
    console.log("File has been created");
  });
}

var writeResultCSV = (async(result) =>{
  let csv = new ObjectsToCsv(result);
 
  // Save to file:
  await csv.toDisk('./test.csv');
 
  // Return the CSV file as string:
  console.log(await csv.toString());
})

// test Auth
client
  .ping()
  .then(function() {
    console.log("authentication succeeded!");
  })
  .catch(function(err) {
    console.log("authentication failed!");
  });

// show all parsers
var grabPaser = () => {
  client
  .getParsers()
  .then(function(parsers) {
    console.log(parsers)
  })
  .catch(function(err) {
    console.log(err);
  });
}

// grab result by id
var returnResult = (id_sequence) => {
  client
  .getParsers()
  .then(function(result){
    client
    .getResultsByParser(result[id_sequence].id, { format: "object" })
    .then(function(result) {
      writeResultCSV(result);
    })
    .catch(function(err) {
      console.log(err);
    })
  })
  .catch(function(err) {
    console.log(err);
  });
}

// upload a document to docParser
var uploadDoc = (id_sequence) => {
  client
  .getParsers()
  .then(function(result){
    client
    .uploadFileByPath(result[id_sequence].id, myFile, {remote_id: 'test'})
    .then(function (result) {
      // => {"id":"document_id","file_size":198989,"quota_used":16,"quota_left":34,"quota_refill":"1970-01-01T00:00:00+00:00"}
      console.log(result)
    })
    .catch(function (err) {
      console.log(err)
    })
  })
  .catch(function(err) {
    console.log(err);
  });
}

var main = () => {
  returnResult(0);
}

main();
