//Stefano Calcaterra - Homework1

/************* EXERCISE 2 *************/

//plan floor0
var plan0_1 = SIMPLEX_GRID([[-1.5,-15,86],[-1.5,-24,53],[1.4]])
var plan0_2 = SIMPLEX_GRID([[-1.5,-15,15],[-1.5,-19,5],[1.4]])

var plan0_3 =  EXTRUDE([1.4])(arc(PI, 0, 7.5))
var plan0_3_1 = R([0,1])(PI)(plan0_3)
var plan0_3_2 = T([0,1])([1.5+15+3+4.5,1.5+19])(plan0_3_1)

var plan0_4 = EXTRUDE([1.4])(arc(PI, 0, 16))
var plan0_4_1 = R([0,1])(-PI/2)(plan0_4)
var plan0_4_2 = T([0,1])([1.5+15+86+13,1.5+24+21+16])(plan0_4_1)

var plan0_5 = SIMPLEX_GRID([[-1.5,-15,-86,13],[-1.5,-24,-21,32],[1.4]])

var floor0 = T([2])([-1.4])(STRUCT([plan0_1, plan0_2, plan0_3_2, plan0_4_2, plan0_5]))

//plan floor1
var plan1_1 = SIMPLEX_GRID([[3,30,3],[81],[1.4]])
var plan1_1_1 = T([0,1])([-1.5,-1.5])(plan1_1)

var plan1_2 = SIMPLEX_GRID([[-3,-30,-3,30,3,3],[3,60,3],[1.4]])
var plan1_2_1 = T([0,1])([-1.5,-1.5])(plan1_2)

var plan1_3 = SIMPLEX_GRID([[-3,-30,-3,-30,-3,-3,27,3,30,3],[81],[1.4]])
var plan1_3_1 = T([0,1])([-1.5,-1.5])(plan1_3)

var plan1_4 = SIMPLEX_GRID([[-3,-30,-3,30,3,3],[-3,-60,-3,-12,3],[1.4]])
var plan1_4_1 = T([0,1])([-1.5,-1.5])(plan1_4)

var plan1_5 = SIMPLEX_GRID([[14],[14],[1.4]])
var plan1_5_1 = T([0,1])([-1.5-14,1.5+60+1.5])(plan1_5)

var floor1 = T([2])([23.6])(STRUCT([plan1_1_1, plan1_2_1,plan1_3_1, plan1_4_1, plan1_5_1]))

//plan floor2
var plan2_1 = SIMPLEX_GRID([[-3,-30,-3,-33,63,3],[81],[1.4]])
var plan2_1_1 = T([0,1])([-1.5,-1.5])(plan2_1)

var plan2_2 = SIMPLEX_GRID([[-3,-30,-3,-21,14],[-3,-60,-3,15],[1.4]])
var plan2_2_1 = T([0,1])([-1.5,-1.5])(plan2_2)

var points = [[1.5+30+3+30, -1.5],[1.5+30+3+18, 1.5+60+3],[1.5+30+3+30+3, 1.5+60+3],[1.5+30+3+33, -1.5]]
var plan2_3 = SIMPLICIAL_COMPLEX(points)([[0,1,2],[0,2,3]])
var plan2_3_1 =  EXTRUDE([1.4])(plan2_3)

var plan2_4 = SIMPLEX_GRID([[3,30,3,33],[3,-60,3],[1.4]])
var plan2_4_1 = T([0,1])([-1.5,-1.5])(plan2_4)

var floor2 = T([2])([23.6+1.4+23.6])(STRUCT([plan2_1_1, plan2_2_1, plan2_3_1, plan2_4_1]))

//plan floor3
var plan3_1 = SIMPLEX_GRID([[66,3],[81],[1.4]])
var plan3_1_1 = T([0,1])([-1.5,-1.5])(plan3_1)

var plan3_2 = SIMPLEX_GRID([[-66,-3,63,3],[3,60,3],[1.4]])
var plan3_2_1 = T([0,1])([-1.5,-1.5])(plan3_2)

var plan3_3 = SIMPLEX_GRID([[-66,-3,-30,-3,-3,27,3],[-3,-60,-3,12,3],[1.4]])
var plan3_3_1 = T([0,1])([-1.5,-1.5])(plan3_3)

var plan3_4 = SIMPLEX_GRID([[-66,-3,30,3,3],[-3,-60,-3,-12,3],[1.4]])
var plan3_4_1 = T([0,1])([-1.5,-1.5])(plan3_4)

var floor3 = T([2])([23.6+1.4+23.6+1.4+23.6])(STRUCT([plan3_1_1, plan3_2_1, plan3_3_1, plan3_4_1]))

//plan floor4
var plan4_1 = SIMPLEX_GRID([[66],[-64,2,15],[1.4]])
var plan4_1_1 = T([0,1])([-1.5,-1.5])(plan4_1)

var plan4_2 = SIMPLEX_GRID([[-66,69],[81],[1.4]])
var plan4_2_1 = T([0,1])([-1.5,-1.5])(plan4_2)

var floor4 = T([2])([23.6+1.4+23.6+1.4+23.6+1.4+23.6])(STRUCT([plan4_1_1, plan4_2_1]))

var building = STRUCT([pillars0, pillars1, pillars2, pillars3, floor0, floor1, floor2, floor3, floor4])

DRAW(building);