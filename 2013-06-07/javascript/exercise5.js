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

  var punti = new Array();

  if(x>25 && y<30) {
  	punti.push(x);
  	punti.push(y);
  	punti.push(0);
  } else {
  	punti.push(x);
  	punti.push(y);
  	punti.push(z);
  }

  return punti;

};

var valley = MAP(mapping)(domain);


/////////////////// EXERCISE 2 ///////////////////

var lake = COLOR([0,0,1])(CUBOID([15,27,0.7]));


/////////////////// EXERCISE 3 ///////////////////

var dom1D = INTERVALS(1)(32);
var dom2D = PROD1x1([INTERVALS(1)(16),INTERVALS(1)(16)]);

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

var coniferous = function (scala) {

	var Su0 = BEZIER(S0)([[0.75,0,0],[0,0,3]]);
	var curve0 = MAP(Su0)(dom1D);
	//DRAW(COLOR([0,0,1])(curve0));

	var Su1 = BEZIER(S1)([[1.5,0,0],[1.5,2,0],[-1.5,2,0],[-1.5,0,0]]);
	var Su1Draw = BEZIER(S0)([[1.5,0,0],[1.5,2,0],[-1.5,2,0],[-1.5,0,0]]);
	var curve1 = MAP(Su1Draw)(dom1D);
	//DRAW(COLOR([1,0,1])(curve1));

	var Su1Base = BEZIER(S0)([[1.1,0,0],[1.1,1.5,0],[-1.1,1.5,0],[-1.1,0,0]]);
	var Su1BaseMirror = BEZIER(S0)([[-1.1,0,0],[-1.1,-1.5,0],[1.1,-1.5,0],[1.1,0,0]]);

	var mezza_chioma = MAP(PROFILEPROD_SURFACE([Su0,Su1]))(dom2D);
	var chioma_sup = STRUCT(REPLICA(2)([mezza_chioma, R([0,1])(PI)]));

	var chioma_base = MAP(BEZIER(S1)([Su1Base,Su1BaseMirror]))(dom2D);

	var chioma = STRUCT([chioma_base, chioma_sup]);


	var tronco = EXTRUDE([1])(arc(2*PI, 0, 0.2));
	var tree = STRUCT([COLOR([1,0.6,0.4])(tronco), COLOR([0,1,0.3])(T([2])([1])(chioma))]);

	return S([0,1,2])([scala,scala,scala])(tree);

}


var popola_foresta = function () {

	for(i=0; i<points.length; i++) {

		var x = points[i][0];
		var y = points[i][1];
		var z = points[i][2];

		if(x < 25 && y < 20) {
			var con = T([0,1,2])([x, y, z])(coniferous(0.5*Math.random()));
			DRAW(con);
		}
	}
}


/////////////////// EXERCISE 4 ///////////////////

var human_settlement = function (x_buildings, y_buildings, coordinates) {

	var houses = new Array();

	var space_x = 0;
	var space_y = 0;

	var x = 1.5;
	var y = 1;

	for(i=0; i<x_buildings; i++) {

		for(k=0; k<y_buildings; k++) {		

			var house = T([0,1])([space_x, space_y])(CUBOID([x,y,2*Math.random()]));
			
			space_y = space_y + 1 + 2;
			

			houses.push(house);
			DRAW(T([0,1,2])([coordinates[0],coordinates[1],coordinates[2]])(house));
		}

		space_y = 0;
		space_x = space_x + x + 2;
	}

	return houses;
}


/////////////////// EXERCISE 5 ///////////////////

//ho modificato i valori dei palazzi, mettendo x e y fisse, in modo da poter fare le strade che altrimenti, avendo valori diversi per ogni palazzo, verrebbero sovrastate
var build_streets = function (x_buildings, y_buildings, coordinates) {

	var streets = new Array();

	var space_street = 1.5;

	var x = (1.5 + 2)* (x_buildings-1) + 1.5;
	var y = (1 + space_street) * (y_buildings-1) + 1 + 2;

	var space_x = 0;
	var space_y = 1.25;

	for(i=0; i<y_buildings; i++) {

		var street = T([0,1])([space_x, space_y])(CUBOID([x,space_street,0.1]));
		space_y = space_y + space_street + 1 + 0.5;
			
		streets.push(street);
		DRAW(COLOR([0,0,0])(T([0,1,2])([coordinates[0],coordinates[1],coordinates[2]])(street)));

	}

	var space_x = 1.75;
	var space_y = 0;


	for(k=0; k<x_buildings -1; k++) {

		var street = T([0,1])([space_x, space_y])(CUBOID([space_street,y,0.1]));
		space_x = space_x + 1.75 + space_street + 0.25;

		streets.push(street);
		DRAW(COLOR([0,0,0])(T([0,1,2])([coordinates[0],coordinates[1],coordinates[2]])(street)));
	}

	return streets;

}

/////////////////// TOTALE ///////////////////
var tot = STRUCT([valley, lake, popola_foresta(), human_settlement(3,4,[28,0,0]), human_settlement(2,4,[30,15,0]), build_streets(3,4,[28,0,0]), build_streets(2,4,[30,15,0]) ]);

DRAW(tot);
