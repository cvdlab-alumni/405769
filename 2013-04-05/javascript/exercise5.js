//Stefano Calcaterra - Homework1

/************* EXERCISE 5 *************/

//ramp
var depth = 2.66;
var raiser = 25./13;
var step2D = SIMPLICIAL_COMPLEX([[0,0],[0,1.4+raiser],[depth,raiser],[depth,1.4+raiser]])([[0,2,1],[1,2,3]]);
var step3D = MAP([S0,S2,S1])(EXTRUDE([12])(step2D));
var ramp = STRUCT(REPLICA(13)([step3D,T([0,2])([depth,raiser])]));

var ramp0 = T([0,1,2])([1.5+15+3+6+10.5, 1.5+60+3,-raiser+0.5])(ramp)
var ramp1 = T([0,1,2])([1.5+6+2+4+7.5, 1.5+60+3,-raiser+0.5+25])(ramp)
var ramp2 = T([0,1,2])([1.5+6+2+4+7.5+(2.66*13)+14, 1.5+60+3,-raiser+0.5+25+25])(ramp)

var ramps = STRUCT([ramp0, ramp1, ramp2])

var building = STRUCT([pillars0, pillars1, pillars2, pillars3, floor0, floor1, floor2, floor3, floor4, north, east, south, west, windows, ramps])

DRAW(building);