#Stefano Calcaterra - Homework1

############## EXERCISE 5 ################

#ramp
depth = 2.66
raiser = 25./13
step2D = MKPOL([[[0,0],[0,1.4+raiser],[depth,raiser],[depth,1.4+raiser]],[[1,3,2],[2,3,4]], None])
step3D = MAP([S1,S3,S2])(PROD([step2D,Q(12)]))
ramp = STRUCT(NN(13)([step3D,T([1,3])([depth,raiser])]))

ramp0 = T([1,2,3])([1.5+15+3+6+10.5, 1.5+60+3,-raiser+0.5])(ramp)
ramp1 = T([1,2,3])([1.5+6+2+4+7.5, 1.5+60+3,-raiser+0.5+25])(ramp)
ramp2 = T([1,2,3])([1.5+6+2+4+7.5+(2.66*13)+14, 1.5+60+3,-raiser+0.5+25+25])(ramp)

ramps = STRUCT([ramp0, ramp1, ramp2])

building = STRUCT([pillars0, pillars1, pillars2, pillars3, floor0, floor1, floor2, floor3, floor4, north, east, south, west, windows, ramps])
VIEW(building)