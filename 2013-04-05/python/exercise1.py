#Stefano Calcaterra - Homework1

############## EXERCISE 1 ################

#cerchio pieno (con opzione di domini alph a e raggio)
def arc (alpha, r, R) : 
	#dom2D = INTERVALS([[0,alpha],[r,R]])([36,1])
	dom2D = PROD([INTERVALS(alpha)(36), DIFFERENCE([INTERVALS(R)(1),INTERVALS(r)(1)])])
	def mapping (v) : 
		a = v[0]
		r = v[1]
		return [r*COS(a), r*SIN(a)]		
	model = MAP(mapping)(dom2D)
	return model

column_round3D = PROD([arc(2*PI, 0, 1.5),Q(23.6)])

#pillars floor0
column_round0_1 = STRUCT(NN(5)([column_round3D,T([1])([1.5 + 30 +1.5])]))
column_round0_2 = T([2])([1.5 + 60 + 1.5])(column_round3D)
column_round0_tot = STRUCT([column_round0_1, column_round0_2])

column_square0_tot = INSR(PROD)(AA(QUOTE)([[-1.5,-15,3,-12,3,-30,3,-30,3],[-1.5,-60,3],[23.6]]))

pillars0 = STRUCT([column_round0_tot, column_square0_tot])

#pillars floor1
column_round1_1 = T([1,2])([1.5+30+3+30+3+30+1.5,1.5+60+1.5])(column_round3D)
column_square1_1 = INSR(PROD)(AA(QUOTE)([[3,-30,3,-30,3,-30,-3,-30,3],[3,-60,3],[23.6]]))
column_square1_2 = INSR(PROD)(AA(QUOTE)([[-3,-30,-3,-30,-3,-30,3],[3],[23.6]]))
column_square1_3 = INSR(PROD)(AA(QUOTE)([[-3,-6,2],[-3,-60,2],[23.6]]))
column_square1_tot = STRUCT([column_square1_1, column_square1_2, column_square1_3])

pillars1 = T([3])([23.6 + 1.4])(STRUCT([column_round1_1, T([1,2])([-1.5,-1.5])(column_square1_tot)]))

#pillars floor2
column_square2_1 =  INSR(PROD)(AA(QUOTE)([[3,-30,3,-96,3],[3],[23.6]]))
column_square2_2 =  INSR(PROD)(AA(QUOTE)([[3,-30,3,-30,3,-30,3,-30,3],[-3,-60,3],[23.6]]))
column_square2_tot = STRUCT([column_square2_1, column_square2_2])

pillars2 = T([1,2,3])([-1.5,-1.5,23.6+1.4+23.6+1.4])(column_square2_tot)

#pillars floor3
column_square3_1 = INSR(PROD)(AA(QUOTE)([[-66,3,-63,3],[3],[23.6]]))
column_square3_2 = INSR(PROD)(AA(QUOTE)([[2,-31,2],[-64,2],[23.6]]))
column_square3_3 = INSR(PROD)(AA(QUOTE)([[-2,-31,-2,-31,3,-30,3,-30,3],[-3,-60,3],[23.6]]))
column_square3_4 = INSR(PROD)(AA(QUOTE)([[-132,3],[-3,-60,-3,-12,3],[23.6]]))
column_square3_tot = STRUCT([column_square3_1, column_square3_2, column_square3_3, column_square3_4])

pillars3 = T([1,2,3])([-1.5,-1.5,23.6+1.4+23.6+1.4+23.6+1.4])(column_square3_tot)

building = STRUCT([pillars0, pillars1, pillars2, pillars3])
VIEW(building)