//Stefano Calcaterra - Homework1

/************* EXERCISE 4 *************/

var window_north1_hor = SIMPLEX_GRID([[60],[0.5,-7,0.5],[3]])
var window_north1_ver = SIMPLEX_GRID([[0.5,-14,0.5,0.5,-14,0.5,0.5,-14,0.5,0.5,-14,0.5],[8],[3]])
var window_north1_glass = SIMPLEX_GRID([[-0.5,14,-0.5,-0.5,14,-0.5,-0.5,14,-0.5,-0.5,14,-0.5],[-0.5,7,-0.5],[3]])
var window_north1 = STRUCT([COLOR([0,0,0])(window_north1_hor), COLOR([0,0,0])(window_north1_ver), COLOR([171,205,239])(window_north1_glass)])

var window_north1_2 = R([0,1])(PI/2)(window_north1)
var window_north1_3 = R([0,2])(PI/2)(window_north1_2)
var window_north1_4 = T([0,1,2])([1.5+30+3+30+3+30+3+30,-1.5+3,23.6+12.5])(STRUCT(REPLICA(3)([window_north1_3,T([2])([25])])))

var window_east1_hor = SIMPLEX_GRID([[30],[0.5,-7,0.5],[3]])
var window_east1_ver = SIMPLEX_GRID([[0.5,-14,0.5,0.5,-14,0.5],[8],[3]])
var window_east1_glass = SIMPLEX_GRID([[-0.5,14,-0.5,-0.5,14,-0.5],[-0.5,7,-0.5],[3]])
var window_east1 = STRUCT([COLOR([0,0,0])(window_east1_hor), COLOR([0,0,0])(window_east1_ver), COLOR([171,205,239])(window_east1_glass)])

var window_east1_2 = R([1,2])(PI/2)(window_east1)
var window_east1_3 = T([0,1,2])([1.5+30+3+30+3,1.5,23.6+12.5])(STRUCT(REPLICA(3)([window_east1_2,T([2])([25])])))

var window_south1_hor = SIMPLEX_GRID([[60],[0.5,-9.25,0.5,0.5,-9.25,0.5],[3]])
var window_south1_ver = SIMPLEX_GRID([[0.5,-14,0.5,0.5,-14,0.5,0.5,-14,0.5,0.5,-14,0.5],[20.5],[3]])
var window_south1_glass = SIMPLEX_GRID([[-0.5,14,-0.5,-0.5,14,-0.5,-0.5,14,-0.5,-0.5,14,-0.5],[-0.5,9.25,-0.5,-0.5,9.25,-0.5],[3]])
var window_south1 = STRUCT([COLOR([0,0,0])(window_south1_hor), COLOR([0,0,0])(window_south1_ver), COLOR([171,205,239])(window_south1_glass)])

var window_south1_2 = R([0,1])(-PI/2)(window_south1)
var window_south1_3 = R([0,2])(-PI/2)(window_south1_2)
var window_south1_4 = T([0,1,2])([1.5,1.5+60,23.6+3])(STRUCT(REPLICA(2)([window_south1_3,T([2])([25])])))

var windows = STRUCT([window_north1_4, window_east1_3, window_south1_4])


var building = STRUCT([pillars0, pillars1, pillars2, pillars3, floor0, floor1, floor2, floor3, floor4, north, east, south, west, windows])

DRAW(window_south1_4);