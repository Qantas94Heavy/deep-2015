'use strict';

var $header = $('#header');
var $results = $('#results');

$header.on('click', 'button', function (e) {
  $results.children('div').load('/poem', 'type=' +  $(e.currentTarget).text());
});
