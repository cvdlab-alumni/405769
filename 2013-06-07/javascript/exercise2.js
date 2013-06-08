// HOMEWORK 3
// Stefano Calcaterra, 405769

/////////////////// EXERCISE 1 ///////////////////

var domain = DOMAIN([[0, 40], [0, 40]])([12,12]);
var points = new Array();

var mapping = function (v) {

  var x = v[0];
  var y = v[1];
  var z = Math.random()*3;

  points.push([x,y,z]);

  return [x, y, z];

};

var valley = MAP(mapping)(domain);


/////////////////// EXERCISE 2 ///////////////////

var lake = COLOR([0,0,1])(CUBOID([15,27,0.7]));


/////////////////// TOTALE ///////////////////
var tot = STRUCT([valley, T([0,1])([20,10])(lake)]);
DRAW(tot);
