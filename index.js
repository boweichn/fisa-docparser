const docparser = require("docparser-node");
const config = require("./config/config");

var client = new docparser.Client(config.key);

client
  .ping()
  .then(function() {
    console.log("authentication succeeded!");
  })
  .catch(function(err) {
    console.log("authentication failed!");
  });

client
  .getParsers()
  .then(function(parsers) {
    console.log(parsers);
    // => [{"id":"someparserid","label":"My Document Parser"}]
  })
  .catch(function(err) {
    console.log(err);
  });
client
  .getResultsByParser("uqinwtuacpxs", { format: "object" })
  .then(function(result) {
    console.log(result);
  })
  .catch(function(err) {
    console.log(err);
  });
