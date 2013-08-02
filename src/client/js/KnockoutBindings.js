var _self = this;
var o_arr = ko.observableArray([]);

var url = "http://localhost:5000/rest/records";
//var url = "http://localhost:5000/rest/record/0";

$.getJSON(url).done(function(data) {
    // Now use this data to update your view models,
    // and Knockout will update your UI automatically
    console.log("Successfully pulled json.");
    _self.o_arr(data)
}).fail(function(jqxhr) {
    console.log("Request Failed. Status: " + jqxhr.status + " Text: " + jqxhr.statusText);
    // response looks to be empty on failures
    //console.log(jqxhr.response);
    //console.log(jqxhr.responseText);
});

ko.applyBindings({'data': _self.o_arr}); // This makes Knockout get to work
