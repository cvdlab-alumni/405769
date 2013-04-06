#Stefano Calcaterra - Homework1

############## EXERCISE 3 ################

#North
north0_1 = INSR(PROD)(AA(QUOTE)([[12],[23.6],[3]]))
north0_2 = INSR(PROD)(AA(QUOTE)([[21],[-20,3.6],[3]]))
north0_3 = STRUCT([north0_1, north0_2])
north0_4 = R([1,2])(PI/2)(north0_3)
north0_5 = R([1,3])(-PI/2)(north0_4)
north0_6 = T([1,2])([1.5+30+3+30+3+30,1.5+24])(north0_5)

north0_7 = INSR(PROD)(AA(QUOTE)([[16,3],[23.6],[3]]))
north0_8 = R([2,3])(-PI/2)(north0_7)
north0_9 = STRUCT(NN(2)([north0_8,T([2])([29])]))
north0_10 = T([1,2,3])([1.5+30+3+30+3+30, 1.5+24+21,23.6])(north0_9)

north0_round1 = PROD([arc(PI, 13, 16),Q(23.6)])
north0_round2 = R([1,2])(-PI/2)(north0_round1)
north0_round3 = T([1,2])([1.5+15+86+13,1.5+24+21+16])(north0_round2)

north1_1 = INSR(PROD)(AA(QUOTE)([[3,-60,12,-3,3],[25],[3]]))
north1_2 = INSR(PROD)(AA(QUOTE)([[-3,60],[12.5,-8,4.5],[3]]))
north1_3 = INSR(PROD)(AA(QUOTE)([[-3,-60,-12,3],[3],[3]]))

north_high_border = INSR(PROD)(AA(QUOTE)([[81],[-23.6,-25,-25,-25,3],[3]]))
north_high_border2 = R([1,2])(PI/2)(north_high_border)
north_high_border3 = R([1,3])(-PI/2)(north_high_border2)
north_high_border4 = T([1,2])([1.5+30+3+30+3+30+3+30, -1.5])(north_high_border3)

north1_4 = STRUCT([north1_1, north1_2, north1_3]) 
north1_5 = R([1,2])(PI/2)(north1_4)
north1_6 = R([1,3])(-PI/2)(north1_5)
north123 = T([1,2,3])([1.5+30+3+30+3+30+3+30,-1.5,23.6])(STRUCT(NN(3)([north1_6,T([3])([25])])))

north = STRUCT([north0_6, north0_10, north0_round3, north123, north_high_border4])

#East
east0_1 = INSR(PROD)(AA(QUOTE)([[-1.5,-15,-12,3,3,30],[25],[3]]))
east0_2 = INSR(PROD)(AA(QUOTE)([[-1.5,-15,-15,-3,-30,30,3],[12.5,-8,3.1],[3]]))
east0_3 = R([2,3])(PI/2)(STRUCT([east0_1, east0_2]))
east0_4 = T([2])([1.5+3+24])(east0_3)

east1_1 = INSR(PROD)(AA(QUOTE)([[3,30,3,30,3,-30,3,30,3],[25],[3]]))
east1_2 = INSR(PROD)(AA(QUOTE)([[-3,-30,-3,-30,-3,30],[12.5,-8,4.5],[3]]))
east1_3 = R([2,3])(PI/2)(STRUCT([east1_1, east1_2]))
east12 = STRUCT(NN(2)([east1_3,T([3])([25])]))

east3_1 = INSR(PROD)(AA(QUOTE)([[3,30,3,30,-3,30],[12.5,-8,4.5,3],[3]]))
east3_2 = INSR(PROD)(AA(QUOTE)([[-3,-30,-3,-30,3,-30,3,30,3],[25,3],[3]]))
east3_3 = R([2,3])(PI/2)(STRUCT([east3_1, east3_2]))

east123 = T([1,2,3])([-1.5, 1.5, 23.6])(STRUCT([east12, T([3])([25+25])(east3_3)]))
east = STRUCT([east0_4, east123])

#South
south0_1 = INSR(PROD)(AA(QUOTE)([[-3,-12,-3,33,3],[13,-10,0.6],[3]]))
south0_2 = INSR(PROD)(AA(QUOTE)([[-3,-12,-3,-33,-3,5],[23.6],[3]]))
south0_3 = STRUCT(NN(2)([south0_2,T([3])([-12])]))
south0_4 = R([1,2])(-PI/2)(STRUCT([south0_1, south0_3]))
south0_5 = R([1,3])(PI/2)(south0_4)

south0_round1 = PROD([arc(PI, 4.5, 7.5),Q(23.6)])
south0_round2 = R([1,2])(PI)(south0_round1)
south0_round3 = T([1,2])([1.5+15+7.5, 1.5+19])(south0_round2)

south0_tot = STRUCT([T([1,2])([1.5+3+15,3+12+3+1.5+60])(south0_5), south0_round3])

south1_1 = INSR(PROD)(AA(QUOTE)([[4,-11,3,-60,3],[25],[3]]))
south1_2 = INSR(PROD)(AA(QUOTE)([[-4,11,-3,60],[3,-20.5,1.5],[3]]))
south1_3 = R([1,2])(-PI/2)(STRUCT([south1_1, south1_2]))
south1_4 = R([1,3])(PI/2)(south1_3)

south2_1 = INSR(PROD)(AA(QUOTE)([[3,12,3,-60,3],[25],[3]]))
south2_2 = INSR(PROD)(AA(QUOTE)([[-3,-12,-3,60],[3,-20.5,1.5],[3]]))
south2_3 = R([1,2])(-PI/2)(STRUCT([south2_1, south2_2]))
south2_4 = R([1,3])(PI/2)(south2_3)

south3_1 = INSR(PROD)(AA(QUOTE)([[3,-13.5,1.5],[25,3],[3]]))
south3_2 = INSR(PROD)(AA(QUOTE)([[-3,13.5,-1.5,63],[12.5,-8,4.5,3],[3]]))
south3_3 = R([1,2])(-PI/2)(STRUCT([south3_1, south3_2]))
south3_4 = R([1,3])(PI/2)(south3_3)

south_balcony_1 = INSR(PROD)(AA(QUOTE)([[14],[11],[1.5]]))
south_balcony_2 = R([1,2])(-PI/2)(south_balcony_1)
south_balcony_3 = R([1,3])(PI/2)(south_balcony_2)
south_balcony_4 = T([1,2,3])([-1.5-12.5,1.5+60+1.5+14, 23.6+1])(south_balcony_3)

south = STRUCT([south0_tot, T([1,2,3])([1.5,81-1.5,23.6])(south1_4), T([1,2,3])([1.5,81-1.5,23.6+25])(south2_4), T([1,2,3])([1.5,81-1.5,23.6+25+25])(south3_4), south_balcony_4])

#West
west0_1 = INSR(PROD)(AA(QUOTE)([[14,-6,13,3,30,3,30],[23.6],[3]]))
west0_2 = INSR(PROD)(AA(QUOTE)([[-14,6],[15.6,-6,2],[3]]))
west0_3 = R([1,2])(PI)(STRUCT([west0_1, west0_2]))
west0_4 = R([2,3])(-PI/2)(west0_3)

west1_1 = INSR(PROD)(AA(QUOTE)([[135],[12.5,-8,4.5],[3]]))
west1_2 = INSR(PROD)(AA(QUOTE)([[30,-30,75],[-12.5,8],[3]]))
west1_3 = R([1,2])(PI)(STRUCT([west1_1, west1_2]))
west1_4 = R([2,3])(-PI/2)(west1_3)

west23_1 = INSR(PROD)(AA(QUOTE)([[135],[12.5,-8,4.5,25,3],[3]]))
west23_2 = INSR(PROD)(AA(QUOTE)([[20,-2,6,-2,105],[-12.5,8],[3]]))
west23_3 = R([1,2])(PI)(STRUCT([west23_1, west23_2]))
west23_4 = R([2,3])(-PI/2)(west23_3)

west = STRUCT([T([1,2])([1.5+30+3+30+3+30,60+3+12+0.5])(west0_4), T([1,2,3])([-1.5+135, 60+3+12+1.5, 23.6])(west1_4), T([1,2,3])([-1.5+135, 60+3+12+1.5, 23.6+25])(west23_4) ])


building = STRUCT([pillars0, pillars1, pillars2, pillars3, floor0, floor1, floor2, floor3, floor4, north, east, south, west])
VIEW(building)