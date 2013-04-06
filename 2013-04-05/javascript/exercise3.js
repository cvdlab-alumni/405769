//Stefano Calcaterra - Homework1

/************* EXERCISE 3 *************/

//North
var north0_1 = SIMPLEX_GRID([[12],[23.6],[3]])
var north0_2 = SIMPLEX_GRID([[21],[-20,3.6],[3]])
var north0_3 = STRUCT([north0_1, north0_2])
var north0_4 = R([0,1])(PI/2)(north0_3)
var north0_5 = R([0,2])(PI/2)(north0_4)
var north0_6 = T([0,1])([1.5+30+3+30+3+30,1.5+24])(north0_5)

var north0_7 = SIMPLEX_GRID([[16,3],[23.6],[3]])
var north0_8 = R([1,2])(-PI/2)(north0_7)
var north0_9 = STRUCT(REPLICA(2)([north0_8,T([1])([29])]))
var north0_10 = T([0,1,2])([1.5+30+3+30+3+30, 1.5+24+21,23.6])(north0_9)

var north0_round1 = EXTRUDE([23.6])(arc(PI, 13, 16))
var north0_round2 = R([0,1])(-PI/2)(north0_round1)
var north0_round3 = T([0,1])([1.5+15+86+13,1.5+24+21+16])(north0_round2)

var north1_1 = SIMPLEX_GRID([[3,-60,12,-3,3],[25],[3]])
var north1_2 = SIMPLEX_GRID([[-3,60],[12.5,-8,4.5],[3]])
var north1_3 = SIMPLEX_GRID([[-3,-60,-12,3],[3],[3]])

var north_high_border = SIMPLEX_GRID([[81],[-23.6,-25,-25,-25,3],[3]])
var north_high_border2 = R([0,1])(PI/2)(north_high_border)
var north_high_border3 = R([0,2])(PI/2)(north_high_border2)
var north_high_border4 = T([0,1])([1.5+30+3+30+3+30+3+30, -1.5])(north_high_border3)

var north1_4 = STRUCT([north1_1, north1_2, north1_3]) 
var north1_5 = R([0,1])(PI/2)(north1_4)
var north1_6 = R([0,2])(PI/2)(north1_5)
var north123 = T([0,1,2])([1.5+30+3+30+3+30+3+30,-1.5,23.6])(STRUCT(REPLICA(3)([north1_6,T([2])([25])])))

var north = STRUCT([north0_6, north0_10, north0_round3, north123, north_high_border4])

//East
var east0_1 = SIMPLEX_GRID([[-1.5,-15,-12,3,3,30],[25],[3]])
var east0_2 = SIMPLEX_GRID([[-1.5,-15,-15,-3,-30,30,3],[12.5,-8,3.1],[3]])
var east0_3 = R([1,2])(PI/2)(STRUCT([east0_1, east0_2]))
var east0_4 = T([1])([1.5+3+24])(east0_3)

var east1_1 = SIMPLEX_GRID([[3,30,3,30,3,-30,3,30,3],[25],[3]])
var east1_2 = SIMPLEX_GRID([[-3,-30,-3,-30,-3,30],[12.5,-8,4.5],[3]])
var east1_3 = R([1,2])(PI/2)(STRUCT([east1_1, east1_2]))
var east12 = STRUCT(REPLICA(2)([east1_3,T([2])([25])]))

var east3_1 = SIMPLEX_GRID([[3,30,3,30,-3,30],[12.5,-8,4.5,3],[3]])
var east3_2 = SIMPLEX_GRID([[-3,-30,-3,-30,3,-30,3,30,3],[25,3],[3]])
var east3_3 = R([1,2])(PI/2)(STRUCT([east3_1, east3_2]))

var east123 = T([0,1,2])([-1.5, 1.5, 23.6])(STRUCT([east12, T([2])([25+25])(east3_3)]))
var east = STRUCT([east0_4, east123])

//South
var south0_1 = SIMPLEX_GRID([[-3,-12,-3,33,3],[13,-10,0.6],[3]])
var south0_2 = SIMPLEX_GRID([[-3,-12,-3,-33,-3,5],[23.6],[3]])
var south0_3 = STRUCT(REPLICA(2)([south0_2,T([2])([-12])]))
var south0_4 = R([0,1])(-PI/2)(STRUCT([south0_1, south0_3]))
var south0_5 = R([0,2])(-PI/2)(south0_4)

var south0_round1 = EXTRUDE([23.6])(arc(PI, 4.5, 7.5))
var south0_round2 = R([0,1])(PI)(south0_round1)
var south0_round3 = T([0,1])([1.5+15+7.5, 1.5+19])(south0_round2)

var south0_tot = STRUCT([T([0,1])([1.5+3+15,3+12+3+1.5+60])(south0_5), south0_round3])

var south1_1 = SIMPLEX_GRID([[4,-11,3,-60,3],[25],[3]])
var south1_2 = SIMPLEX_GRID([[-4,11,-3,60],[3,-20.5,1.5],[3]])
var south1_3 = R([0,1])(-PI/2)(STRUCT([south1_1, south1_2]))
var south1_4 = R([0,2])(-PI/2)(south1_3)

var south2_1 = SIMPLEX_GRID([[3,12,3,-60,3],[25],[3]])
var south2_2 = SIMPLEX_GRID([[-3,-12,-3,60],[3,-20.5,1.5],[3]])
var south2_3 = R([0,1])(-PI/2)(STRUCT([south2_1, south2_2]))
var south2_4 = R([0,2])(-PI/2)(south2_3)

var south3_1 = SIMPLEX_GRID([[3,-13.5,1.5],[25,3],[3]])
var south3_2 = SIMPLEX_GRID([[-3,13.5,-1.5,63],[12.5,-8,4.5,3],[3]])
var south3_3 = R([0,1])(-PI/2)(STRUCT([south3_1, south3_2]))
var south3_4 = R([0,2])(-PI/2)(south3_3)

var south_balcony_1 = SIMPLEX_GRID([[14],[11],[1.5]])
var south_balcony_2 = R([0,1])(-PI/2)(south_balcony_1)
var south_balcony_3 = R([0,2])(-PI/2)(south_balcony_2)
var south_balcony_4 = T([0,1,2])([-1.5-12.5,1.5+60+1.5+14, 23.6+1])(south_balcony_3)

south = STRUCT([south0_tot, T([0,1,2])([1.5,81-1.5,23.6])(south1_4), T([0,1,2])([1.5,81-1.5,23.6+25])(south2_4), T([0,1,2])([1.5,81-1.5,23.6+25+25])(south3_4), south_balcony_4])

//West
var west0_1 = SIMPLEX_GRID([[14,-6,13,3,30,3,30],[23.6],[3]])
var west0_2 = SIMPLEX_GRID([[-14,6],[15.6,-6,2],[3]])
var west0_3 = R([0,1])(PI)(STRUCT([west0_1, west0_2]))
var west0_4 = R([1,2])(-PI/2)(west0_3)

var west1_1 = SIMPLEX_GRID([[135],[12.5,-8,4.5],[3]])
var west1_2 = SIMPLEX_GRID([[30,-30,75],[-12.5,8],[3]])
var west1_3 = R([0,1])(PI)(STRUCT([west1_1, west1_2]))
var west1_4 = R([1,2])(-PI/2)(west1_3)

var west23_1 = SIMPLEX_GRID([[135],[12.5,-8,4.5,25,3],[3]])
var west23_2 = SIMPLEX_GRID([[20,-2,6,-2,105],[-12.5,8],[3]])
var west23_3 = R([0,1])(PI)(STRUCT([west23_1, west23_2]))
var west23_4 = R([1,2])(-PI/2)(west23_3)


var west = STRUCT([T([0,1])([1.5+30+3+30+3+30,60+3+12+0.5])(west0_4), T([0,1,2])([-1.5+135, 60+3+12+1.5, 23.6])(west1_4), T([0,1,2])([-1.5+135, 60+3+12+1.5, 23.6+25])(west23_4) ])


var building = STRUCT([pillars0, pillars1, pillars2, pillars3, floor0, floor1, floor2, floor3, floor4, north, east, south, west])

DRAW(building);