#Stefano Calcaterra - Homework1

############## EXERCISE 2 ################

#plan floor0
plan0_1 = INSR(PROD)(AA(QUOTE)([[-1.5,-15,86],[-1.5,-24,53],[1.4]]))
plan0_2 = INSR(PROD)(AA(QUOTE)([[-1.5,-15,15],[-1.5,-19,5],[1.4]]))

plan0_3 = PROD([arc(PI, 0, 7.5),Q(1.4)])
plan0_3_1 = R([1,2])(PI)(plan0_3)
plan0_3_2 = T([1,2])([1.5+15+3+4.5,1.5+19])(plan0_3_1)

plan0_4 = PROD([arc(PI, 0, 16),Q(1.4)])
plan0_4_1 = R([1,2])(-PI/2)(plan0_4)
plan0_4_2 = T([1,2])([1.5+15+86+13,1.5+24+21+16])(plan0_4_1)

plan0_5 = INSR(PROD)(AA(QUOTE)([[-1.5,-15,-86,13],[-1.5,-24,-21,32],[1.4]]))


floor0 = T([3])([-1.4])(STRUCT([plan0_1, plan0_2, plan0_3_2, plan0_4_2, plan0_5]))
#building = STRUCT([plan0_tot])

#plan floor1
plan1_1 = INSR(PROD)(AA(QUOTE)([[3,30,3],[81],[1.4]]))
plan1_1_1 = T([1,2])([-1.5,-1.5])(plan1_1)

plan1_2 = INSR(PROD)(AA(QUOTE)([[-3,-30,-3,30,3,3],[3,60,3],[1.4]]))
plan1_2_1 = T([1,2])([-1.5,-1.5])(plan1_2)

plan1_3 = INSR(PROD)(AA(QUOTE)([[-3,-30,-3,-30,-3,-3,27,3,30,3],[81],[1.4]]))
plan1_3_1 = T([1,2])([-1.5,-1.5])(plan1_3)

plan1_4 = INSR(PROD)(AA(QUOTE)([[-3,-30,-3,30,3,3],[-3,-60,-3,-12,3],[1.4]]))
plan1_4_1 = T([1,2])([-1.5,-1.5])(plan1_4)

plan1_5 = INSR(PROD)(AA(QUOTE)([[14],[14],[1.4]]))
plan1_5_1 = T([1,2])([-1.5-14,1.5+60+1.5])(plan1_5)

floor1 = T([3])([23.6])(STRUCT([plan1_1_1, plan1_2_1,plan1_3_1, plan1_4_1, plan1_5_1]))

#plan floor2
plan2_1 = INSR(PROD)(AA(QUOTE)([[-3,-30,-3,-33,63,3],[81],[1.4]]))
plan2_1_1 = T([1,2])([-1.5,-1.5])(plan2_1)

plan2_2 = INSR(PROD)(AA(QUOTE)([[-3,-30,-3,-21,14],[-3,-60,-3,15],[1.4]]))
plan2_2_1 = T([1,2])([-1.5,-1.5])(plan2_2)

plan2_3 = MKPOL([[[1.5+30+3+30, -1.5],[1.5+30+3+18, 1.5+60+3],[1.5+30+3+30+3, 1.5+60+3],[1.5+30+3+33, -1.5]],[[1,2,3,4]],None])
plan2_3_1 = PROD([plan2_3,Q(1.4)])

plan2_4 = INSR(PROD)(AA(QUOTE)([[3,30,3,33],[3,-60,3],[1.4]]))
plan2_4_1 = T([1,2])([-1.5,-1.5])(plan2_4)

floor2 = T([3])([23.6+1.4+23.6])(STRUCT([plan2_1_1, plan2_2_1, plan2_3_1, plan2_4_1]))

#plan floor3
plan3_1 = INSR(PROD)(AA(QUOTE)([[66,3],[81],[1.4]]))
plan3_1_1 = T([1,2])([-1.5,-1.5])(plan3_1)

plan3_2 = INSR(PROD)(AA(QUOTE)([[-66,-3,63,3],[3,60,3],[1.4]]))
plan3_2_1 = T([1,2])([-1.5,-1.5])(plan3_2)

plan3_3 = INSR(PROD)(AA(QUOTE)([[-66,-3,-30,-3,-3,27,3],[-3,-60,-3,12,3],[1.4]]))
plan3_3_1 = T([1,2])([-1.5,-1.5])(plan3_3)

plan3_4 = INSR(PROD)(AA(QUOTE)([[-66,-3,30,3,3],[-3,-60,-3,-12,3],[1.4]]))
plan3_4_1 = T([1,2])([-1.5,-1.5])(plan3_4)

floor3 = T([3])([23.6+1.4+23.6+1.4+23.6])(STRUCT([plan3_1_1, plan3_2_1, plan3_3_1, plan3_4_1]))

#plan floor4
plan4_1 = INSR(PROD)(AA(QUOTE)([[66],[-64,2,15],[1.4]]))
plan4_1_1 = T([1,2])([-1.5,-1.5])(plan4_1)

plan4_2 = INSR(PROD)(AA(QUOTE)([[-66,69],[81],[1.4]]))
plan4_2_1 = T([1,2])([-1.5,-1.5])(plan4_2)

floor4 = T([3])([23.6+1.4+23.6+1.4+23.6+1.4+23.6])(STRUCT([plan4_1_1, plan4_2_1]))

building = STRUCT([pillars0, pillars1, pillars2, pillars3, floor0, floor1, floor2, floor3, floor4])
VIEW(building)