'use strict';

var $header = $('#header');
var $results = $('#results');

$header.on('click', 'button', function (e) {
  var type = $(e.currentTarget).text();
  if (type === 'Haiku') {
    alert('This requires the paid version of Poem Generator. Please pay using PayPal.');
    window.location.href = '/pro.html';
  }
  $results.children('div').load('/poem', 'type=' + type);
});
