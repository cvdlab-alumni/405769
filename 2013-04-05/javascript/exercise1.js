//Stefano Calcaterra - Homework1

/************* EXERCISE 1 *************/

//porzione di arco pieno
function arc (alpha, r, R) {

	var domain = DOMAIN([[0,alpha],[r,R]])([36,1]);
	
	var mapping = function (v) {
		var a = v[0];
		var r = v[1];

		return [r*COS(a), r*SIN(a)];
	}

	var model = MAP(mapping)(domain);
	return model;
} 

var column_round3D = EXTRUDE([23.6])(arc(2*PI, 0, 1.5))

//pillars floor0
var column_round0_1 = STRUCT(REPLICA(5)([column_round3D,T([0])([1.5 + 30 +1.5])]))
var column_round0_2 = T([1])([1.5 + 60 + 1.5])(column_round3D)
var column_round0_tot = STRUCT([column_round0_1, column_round0_2])

var column_square0_tot = SIMPLEX_GRID([[-1.5,-15,3,-12,3,-30,3,-30,3],[-1.5,-60,3],[23.6]])

var pillars0 = STRUCT([column_round0_tot, column_square0_tot])

//pillars floor1
var column_round1_1 = T([0,1])([1.5+30+3+30+3+30+1.5,1.5+60+1.5])(column_round3D)
var column_square1_1 = SIMPLEX_GRID([[3,-30,3,-30,3,-30,-3,-30,3],[3,-60,3],[23.6]])
var column_square1_2 = SIMPLEX_GRID([[-3,-30,-3,-30,-3,-30,3],[3],[23.6]])
var column_square1_3 = SIMPLEX_GRID([[-3,-6,2],[-3,-60,2],[23.6]])
var column_square1_tot = STRUCT([column_square1_1, column_square1_2, column_square1_3])

var pillars1 = T([2])([23.6 + 1.4])(STRUCT([column_round1_1, T([0,1])([-1.5,-1.5])(column_square1_tot)]))

//pillars floor2
var column_square2_1 =  SIMPLEX_GRID([[3,-30,3,-96,3],[3],[23.6]])
var column_square2_2 =  SIMPLEX_GRID([[3,-30,3,-30,3,-30,3,-30,3],[-3,-60,3],[23.6]])
var column_square2_tot = STRUCT([column_square2_1, column_square2_2])

var pillars2 = T([0,1,2])([-1.5,-1.5,23.6+1.4+23.6+1.4])(column_square2_tot)

//pillars floor3
var column_square3_1 = SIMPLEX_GRID([[-66,3,-63,3],[3],[23.6]])
var column_square3_2 = SIMPLEX_GRID([[2,-31,2],[-64,2],[23.6]])
var column_square3_3 = SIMPLEX_GRID([[-2,-31,-2,-31,3,-30,3,-30,3],[-3,-60,3],[23.6]])
var column_square3_4 = SIMPLEX_GRID([[-132,3],[-3,-60,-3,-12,3],[23.6]])
var column_square3_tot = STRUCT([column_square3_1, column_square3_2, column_square3_3, column_square3_4])

var pillars3 = T([0,1,2])([-1.5,-1.5,23.6+1.4+23.6+1.4+23.6+1.4])(column_square3_tot)

var building = STRUCT([pillars0, pillars1, pillars2, pillars3])

DRAW(building);