#STEFANO CALCATERRA - 405769
#HOMEWORK2 - EXERCISE 5

############################################### FUNZIONE GRID ###############################################

#funzione GRID
from pyplasm import *
import scipy
from  scipy import*
#from lar import *  
					
def larExtrude(model,pattern):
    V,FV = model
    d = len(FV[0])
    offset = len(V)
    m = len(pattern)
    outcells = []
    for cell in FV:
        # create the indices of vertices in the cell "tube"
        tube = [v + k*offset for k in range(m+1) for v in cell]
        # take groups of d+1 elements, via shifting by one
        rangelimit = len(tube)-d
        cellTube = [tube[k:k+d+1] for k in range(rangelimit)]
        outcells += [scipy.reshape(cellTube,newshape=(m,d,d+1)).tolist()]
    outcells = AA(CAT)(TRANS(outcells))
    outcells = [group for k,group in enumerate(outcells) if pattern[k]>0 ]
    coords = list(cumsum([0]+(AA(ABS)(pattern))))
    outVerts = VERTEXTRUDE((V,coords))
    newModel = outVerts, CAT(outcells)
    return newModel


def VERTEXTRUDE((V,coords)):
    """
        Utility function to generate the output model vertices in a multiple extrusion of a LAR model.
        V is a list of d-vertices (each given as a list of d coordinates).
        coords is a list of absolute translation parameters to be applied to V in order
        to generate the output vertices.
        
        Return a new list of (d+1)-vertices.
    """
    return CAT(AA(COMP([AA(AR),DISTR]))(DISTL([V,coords])))

# Questa funzione mi permette di ottenere un dominio simpliciale(triangolare)
def GRID (args):
    model= ([[]],[[0]])
    for k,step in enumerate(args):
        model = larExtrude(model,step*[1])
    V, cells = model
    verts = AA(list)(scipy.array(V)/AA(float)(args))
    return MKPOL([verts,AA(AA(lambda h:h+1))(cells),None])

############################################### PARTE ESERCIZIO 5 ###############################################

Dom1D = INTERVALS(1)(24)
dom1 = GRID([20,20])
dom2 = MAP([S2,S1])(dom1)
Bezier = BEZIER(S1) 

########################## cofano interno ########################## 

#superficie bilineare generata da punti
controlpoints_cofano=[[[1.75,-2,4.5],[1.25,0,4.5],[1.75,2,4.5]],
				[[3,-3,5],[3,0,6],[3,3,5]],
				[[6,-4,6.5],[6,0,7],[6,4,6.5]],
				[[10,-5,6.5],[8.5,0,6.5],[10,5,6.5]]]

mapping_cofano=BEZIERSURFACE(controlpoints_cofano)
cofano_interno = MAP(mapping_cofano)(dom1)
cofano_interno_scalato = SCALE([1,2,3])([0.33,0.33,0.33])(cofano_interno)
cofano_interno_traslato = T([1,3])([-16.5,0])(cofano_interno_scalato)

#VIEW(cofano_interno_scalato)



########################## specchietto ########################## 

#restituisce i valori inversi di x e y
def specchietto_inverso (controlpoints):
	array_new = []
	for array in controlpoints:
		array_points = []
		for points in array:			
			x = points[0]
			y = points[1]
			z = points[2]
			array_points.append((x,-y,z))
		array_new.append(array_points)
	#print array_new
	return array_new


#valori specchietto sinistra
SFu0 = [(0,2.5,6.75),(0.3,2.5,6.70),(0,2.5,6.5)]
SFu1 = [(0,1.55,7),(0.50,1.4,6.75),(0,1.3,6.5)]
SFu2 = [(0,1.5,7.25),(1,1.35,7),(0,1.25,6.75)]
SFu3 = [(0,1.25,8),(0.8,1,7.5),(0,0.75,6.5)]
SFu4 = [(0,1.2,7.75),(1.8,1,7.5),(0,0.75,6.75)]
SFu5 = [(0,0.5,7.5),(1,0.5,7.25),(0,0.5,6.75)]
SFu6 = [(0,0.05,7.5),(0,0.05,7.25),(0,0.05,7)]
SFu7 = [(0,0,7.25),(0,0,7.25),(0,0,7.1)]


SRu0 = [(0,2.5,6.75),(0,2.5,6.70),(0,2.5,6.5)]
SRu1 = [(0,1.55,7),(0,1.4,6.75),(0,1.3,6.5)]
SRu2 = [(0,1.5,7.25),(0,1.35,7),(0,1.25,6.75)]
SRu3 = [(0,1.25,8),(0,1,7.5),(0,0.75,6.5)]
SRu4 = [(0,1.2,7.75),(0,1,7.5),(0,0.75,6.75)]
SRu5 = [(0,0.5,7.5),(0,0.5,7.25),(0,0.5,6.75)]
SRu6 = [(0,0.05,7.5),(0,0.05,7.25),(0,0.05,7)]
SRu7 = [(0,0,7.25),(0,0,7.25),(0,0,7.1)]

csfu0 = MAP(Bezier(SFu0))(dom1)
csfu1 = MAP(Bezier(SFu1))(dom1)
csfu2 = MAP(Bezier(SFu2))(dom1)
csfu3 = MAP(Bezier(SFu3))(dom1)
csfu4 = MAP(Bezier(SFu4))(dom1)
csfu5 = MAP(Bezier(SFu5))(dom1)
csfu6 = MAP(Bezier(SFu6))(dom1)
csfu7 = MAP(Bezier(SFu7))(dom1)


controlpoints_specchietto_sx_front = [SFu0,SFu1,SFu2,SFu3,SFu4,SFu5,SFu6,SFu7]
controlpoints_specchietto_sx_rear= [SRu0,SRu1,SRu2,SRu3,SRu4,SRu5,SRu6,SRu7]

controlpoints_specchietto_dx_front = specchietto_inverso([SFu0,SFu1,SFu2,SFu3,SFu4,SFu5,SFu6,SFu7])
controlpoints_specchietto_dx_rear = specchietto_inverso([SRu0,SRu1,SRu2,SRu3,SRu4,SRu5,SRu6,SRu7])
#print controlpoints_specchietto_dx_front

#linee_controllo = COLOR([1,0,0])(STRUCT([csfu0,csfu1,csfu2,csfu3,csfu4,csfu5,csfu6,csfu7]))

#######
mapping_specchietto_sx_front=BEZIERSURFACE(controlpoints_specchietto_sx_front)
mapping_specchietto_sx_rear=BEZIERSURFACE(controlpoints_specchietto_sx_rear)

mapping_specchietto_dx_front=BEZIERSURFACE(controlpoints_specchietto_dx_front)
mapping_specchietto_dx_rear=BEZIERSURFACE(controlpoints_specchietto_dx_rear)

#######
specchietto_sx_front = MAP(mapping_specchietto_sx_front)(dom1)
specchietto_sx_rear = MAP(mapping_specchietto_sx_rear)(dom1)

specchietto_dx_front = MAP(mapping_specchietto_dx_front)(dom2)
specchietto_dx_rear = MAP(mapping_specchietto_dx_rear)(dom2)

######

specchietto_sx = STRUCT([COLOR([0,1,1])(specchietto_sx_rear), specchietto_sx_front])
specchietto_sx_scalato = SCALE([1,2,3])([0.33,0.33,0.33])(specchietto_sx)
specchietto_sx_ruotato = R([1,2])(PI)(specchietto_sx_scalato)

specchietto_dx = STRUCT([COLOR([0,1,1])(specchietto_dx_rear), specchietto_dx_front])
specchietto_dx_scalato = SCALE([1,2,3])([0.33,0.33,0.33])(specchietto_dx)
specchietto_dx_ruotato = R([1,2])(PI)(specchietto_dx_scalato)

######

specchietto_sx = T([2,3])([8,0.2])(specchietto_sx_ruotato)
specchietto_dx = T([2,3])([-8,0.2])(specchietto_dx_ruotato)

specchietti = STRUCT([specchietto_sx,specchietto_dx])

#VIEW(STRUCT([specchietti,vista_complessiva]))



############################################### PARTE ESERCIZIO 4 ###############################################

Dom1D = INTERVALS(1)(24)
dom1 = GRID([20,20])
dom2 = MAP([S2,S1])(dom1)
Bezier = BEZIER(S1)

####################### volante ######################

volante_alpha = Bezier([[1.1,0,0],[1.2,0,0.6],[1.5,0,0],[1.2,0,-0.6],[1.1,0,0]])
volante_beta = BEZIER(S2)([[2.75,0,0],[2.75,3.67,0],[-2.75,3.67,0],[-2.75,0,0]])

surface1 = MAP(PROFILEPRODSURFACE([volante_alpha,volante_beta]))(dom1)
surface1_scaled = SCALE([1,2,3])([0.4,0.4,0.4])(surface1)

manico = COLOR(BLACK)(STRUCT(NN(2)([surface1_scaled,R([1,2])(PI)])))

#VIEW(v1)

#corpo volante
Cv0 = [[-1.37,0,0],[0,0.5,0],[1.37,0,0]]
Cv1 = [[-1.37,-0.25,0],[0,0.5,0],[1.37,-0.25,0]]
Cv2 = [[-0.3,-0.2,0],[0,0,0],[0.3,-0.2,0]]
Cv3 = [[-0.3,-0.25,0],[0,-0.2,0],[0.3,-0.25,0]]
Cv4 = [[-0.3,-0.3,0],[0,-0.2,0],[0.3,-0.3,0]]
Cv5 = [[-0.2,-0.6,0],[0,-0.5,0],[0.2,-0.6,0]]
Cv6 = [[-0.2,-0.6,0],[0,-0.5,0],[0.2,-0.6,0]]
Cv7 = [[-0.1,-0.9,0],[0,-0.8,0],[0.1,-0.9,0]]
Cv8 = [[-0.1,-1.37,0],[0,-1.36,0],[0.1,-1.37,0]]

cv0 = MAP(Bezier(Cv0))(dom1)
cv1 = MAP(Bezier(Cv1))(dom1)
cv2 = MAP(Bezier(Cv2))(dom1)
cv3 = MAP(Bezier(Cv3))(dom1)
cv4 = MAP(Bezier(Cv4))(dom1)
cv5 = MAP(Bezier(Cv5))(dom1)
cv6 = MAP(Bezier(Cv6))(dom1)
cv7 = MAP(Bezier(Cv7))(dom1)
cv8 = MAP(Bezier(Cv8))(dom1)

#VIEW(STRUCT([v1,cv0,cv1,cv2,cv3,cv4,cv5,cv6,cv7,cv8]))

controlpoints_volante = [Cv0,Cv1,Cv2,Cv3,Cv4,Cv5,Cv6,Cv7,Cv8]

mapping_volante=BEZIERSURFACE(controlpoints_volante)
surface2 = MAP(mapping_volante)(dom1)
surface2_scaled = SCALE([1,2,3])([0.33,0.33,0.33])(surface2)
#VIEW(STRUCT([v1, surface2_scaled]))

surface2_offset = OFFSET([0,0,0.05])(surface2_scaled)
corpo = surface2_offset
#VIEW(STRUCT([T(3)(-0.025)(surface2_offset),v1]))

#pomello
pomello_alpha = Bezier([[0,0,0.25],[0.5,0,0.3],[1,0,0]])
pomello_beta = BEZIER(S2)([[1,0,0],[1,1.5,0],[-1,1.5,0],[-1,0,0]])

p1 = MAP(pomello_alpha)(dom1)
p2 = MAP(pomello_beta)(dom1)

#VIEW(STRUCT([p1,p2]))

surface3 = MAP(PROFILEPRODSURFACE([pomello_alpha,pomello_beta]))(dom1)
surface3_scaled = SCALE([1,2,3])([0.25,0.25,0.25])(surface3)

pomello_tot = STRUCT(NN(2)([surface3_scaled,R([1,2])(PI)]))
pomello = COLOR(GRAY)(T([2,3])([-0.1,0.05])(pomello_tot))
#VIEW(pomello) 

volante = STRUCT([manico, corpo, pomello])
#VIEW(volante)

volante_r1 = R([1,2])(PI/2)(volante)
volante_r2 = R([1,3])(-PI/3)(volante_r1)
volante_t = T([1,2,3])([-3,-2.5,6])(volante_r2)



############################################### PARTE ESERCIZIO 3 ###############################################

Dom1D = INTERVALS(1)(24)
dom1 = GRID([20,20])
dom2 = MAP([S2,S1])(dom1)
Bezier = BEZIER(S1)

#cerchio pieno (con opzione di domini alph a e raggio)
def arc (alpha, r, R) : 

	dom2D = PROD([INTERVALS(alpha)(36), DIFFERENCE([INTERVALS(R)(1),INTERVALS(r)(1)])])
	def mapping (v) : 
		a = v[0]
		r = v[1]
		return [r*COS(a), r*SIN(a)]		
	model = MAP(mapping)(dom2D)
	return model


cerchione_esterno = PROD([arc(2*PI, 2.35, 2.45),Q(2.5)])

############### copertone ################
alpha = Bezier([[2.30,0,0],[2.65,0,0],[2.75,0,0.05],[2.75,0,2.4],[2.65,0,2.5],[2.30,0,2.5]])
beta = BEZIER(S2)([[2.75,0,0],[2.75,3.67,0],[-2.75,3.67,0],[-2.75,0,0]])

surface = MAP(PROFILEPRODSURFACE([alpha,beta]))(dom1)
surface_scaled = SCALE([1,2])([0.38,0.38])(surface)
copertone = STRUCT(NN(2)([surface_scaled,R([1,2])(PI)]))

#VIEW(STRUCT([COLOR([0,0,0])(copertone),cerchione_esterno]))

################# raggio ################
c0 = [[0.5,0.3,0],[1.2,0.14,0.45],[1.25,0.15,0.5],[1.30,0.14,0.45],[2.35,0.10,0]]
c1 = [[0.5,-0.3,0],[1.2,-0.14,0.45],[1.25,-0.15,0.5],[1.30,-0.14,0.45],[2.35,-0.10,0]]

s0 = MAP(Bezier(c0))(dom1)
s1 = MAP(Bezier(c1))(dom1)

#VIEW(STRUCT([s0,s1]))

C0 = Bezier(c0)
C1 = Bezier(c1)

raggio_1 = MAP(BEZIER(S2)([C0,C1]))(GRID([20,20]))
#VIEW(raggio_1)

raggio_2 = OFFSET([0,0,0.1])(raggio_1)
#VIEW(raggio_2)

raggi = STRUCT(NN(6)([raggio_2,R([1,2])(PI/3)]))
#VIEW(raggi)

perno1 = PROD([arc(2*PI, 0, 0.59),Q(0.1)])
perno2 = PROD([arc(2*PI, 0, 0.3),Q(0.15)])
perno_tot = T(3)(2.2)(STRUCT([perno1,COLOR([1,1,0])(perno2)]))

################################

cerchione = STRUCT([cerchione_esterno,T(3)(2.2)(raggi),perno_tot])
#VIEW(cerchione)

################################

ruota = SCALE([1,2,3])([0.8,0.8,0.8])(STRUCT([COLOR([0,0,0])(copertone), cerchione]))
ruota_ruotata = R([2,3])(PI/2)(ruota)
ruota_traslata = T([1,2,3])([-8.5,-5,2])(ruota_ruotata)

ruote_sinistra = STRUCT(NN(2)([ruota_traslata,T(1)(19+0.75+0.5)]))
ruote_destra = R([2,3])(PI)(T(3)(-2-2)(ruote_sinistra)) 

ruote_tot = STRUCT([ruote_sinistra,ruote_destra])
#VIEW(STRUCT([ruote_tot, vista_complessiva]))



############################################### PARTE ESERCIZIO 2 ###############################################

Dom1D = INTERVALS(1)(24)
Bezier = BEZIER(S1) 

#laterale
Lu0 = [(0,0,3.5),(0.25,0,1.5)]
Lu1 = [(0.25,0,1.5),(3,0,0.75),(5.75,0,1)]
Lu2 = [(5.75,0,1),(5.75,0,5.25),(11.25,0,5.25),(11.25,0,1)]
Lu3 = [(11.25,0,1),(25.75,0,1)]
Lu4 = [(25.75,0,1),(25.75,0,5.5),(31.75,0,5.5),(31.75,0,1.25)]
Lu5 = [(31.75,0,1.25),(34,0,1.5),(34,0,4),(35,0,5)]
Lu6 = [(35,0,5),(34.5,0,5.5),(34.25,0,6.75)]
Lu7 = [(34.25,0,6.75),(34.25,0,7.75)]
Lu8 = [(34.25,0,7.75),(33,0,6.5),(29,0,7),(24,0,9),(19,0,12.5),(14,0,8.5),(9.5,0,6.5)]
Lu9 = [(9.5,0,6.5),(5,0,6.5),(0,0,3.5)]

clu0 = MAP(Bezier(Lu0))(Dom1D)
clu1 = MAP(Bezier(Lu1))(Dom1D)
clu2 = MAP(Bezier(Lu2))(Dom1D)
clu3 = MAP(Bezier(Lu3))(Dom1D)
clu4 = MAP(Bezier(Lu4))(Dom1D)
clu5 = MAP(Bezier(Lu5))(Dom1D)
clu6 = MAP(Bezier(Lu6))(Dom1D)
clu7 = MAP(Bezier(Lu7))(Dom1D)
clu8 = MAP(Bezier(Lu8))(Dom1D)
clu9 = MAP(Bezier(Lu9))(Dom1D)

laterale = STRUCT([clu0,clu1,clu2,clu3,clu4,clu5,clu6,clu7,clu8,clu9])
#VIEW(laterale)

#frontale

Fu0 = [(0,8.5,9.75),(0,6,9.75),(0,4.25,9.25)]
Fu1 = [(0,4.25,9.25),(0,2.5,7.75)]
Fu2 = [(0,2.5,7.75),(0,1.75,8),(0,1.5,7.5)]
Fu3 = [(0,1.5,7.5),(0,1.25,7.75)]
Fu4 = [(0,1.25,7.75),(0,0,7.5)]
Fu5 = [(0,0,7.5),(0,0,7)]
Fu6 = [(0,0,7),(0,0.75,6.75),(0,1.25,6.75)]
Fu7 = [(0,1.25,6.75),(0,1.25,6.5)]
Fu8 = [(0,1.25,6.5),(0,0.75,6),(0,0.75,4),(0,1.5,1.75)]
Fu9 = [(0,1.5,1.75),(0,2.5,1.5),(0,3.5,1.5)]
Fu10 = [(0,3.5,1.5),(0,4,1),(0,4.5,1.25)]
Fu11 = [(0,4.5,1.25),(0,6.5,1.25)]
Fu12 = [(0,6.5,1.25),(0,7,1)]
Fu13 = [(0,7,1),(0,8.5,1)]

cfu0 = MAP(Bezier(Fu0))(Dom1D)
cfu1 = MAP(Bezier(Fu1))(Dom1D)
cfu2 = MAP(Bezier(Fu2))(Dom1D)
cfu3 = MAP(Bezier(Fu3))(Dom1D)
cfu4 = MAP(Bezier(Fu4))(Dom1D)
cfu5 = MAP(Bezier(Fu5))(Dom1D)
cfu6 = MAP(Bezier(Fu6))(Dom1D)
cfu7 = MAP(Bezier(Fu7))(Dom1D)
cfu8 = MAP(Bezier(Fu8))(Dom1D)
cfu9 = MAP(Bezier(Fu9))(Dom1D)
cfu10 = MAP(Bezier(Fu10))(Dom1D)
cfu11 = MAP(Bezier(Fu11))(Dom1D)
cfu12 = MAP(Bezier(Fu12))(Dom1D)
cfu13 = MAP(Bezier(Fu13))(Dom1D)

frontale_sx = STRUCT([cfu0,cfu1,cfu2,cfu3,cfu4,cfu5,cfu6,cfu7,cfu8,cfu9,cfu10,cfu11,cfu12,cfu13])
frontale_dx = R([1,2])(PI)(frontale_sx)

frontale = STRUCT([frontale_sx,T(2)(16)(frontale_dx)])
#VIEW(frontale)

#superiore
Su0 = [(0,7.5,0),(0,6,0),(1.5,1.5,0),(4,0.25,0),(6.75,-0.25,0)]
Su0_1 = [(6.75,-0.25,0),(7,0,0)]
Su1 = [(7,0,0),(13.5,0,0)]
Su2 = [(13.5,0,0),(14,-1,0),(14.5,-0.75,0)]
Su3 = [(14.5,-0.75,0),(14.25,-0.5,0),(14.25,0,0)]
Su4 = [(14.25,0,0),(27,0,0)]
Su5 = [(27,0,0),(27.5,-0.25,0)]
Su6 = [(27.5,-0.25,0),(32,-0.25,0)]
Su7 = [(32,-0.25,0),(33,0,0),(34.5,1.5,0),(35,6,0),(35,7.5,0)]

csu0 = MAP(Bezier(Su0))(Dom1D)
csu0_1 = MAP(Bezier(Su0_1))(Dom1D)
csu1 = MAP(Bezier(Su1))(Dom1D)
csu2 = MAP(Bezier(Su2))(Dom1D)
csu3 = MAP(Bezier(Su3))(Dom1D)
csu4 = MAP(Bezier(Su4))(Dom1D)
csu5 = MAP(Bezier(Su5))(Dom1D)
csu6 = MAP(Bezier(Su6))(Dom1D)
csu7 = MAP(Bezier(Su7))(Dom1D)

superiore_sx = STRUCT([csu0,csu0_1,csu1,csu2,csu3,csu4,csu5,csu6,csu7])
superiore_dx = R([2,3])(PI)(superiore_sx)

superiore = STRUCT([superiore_sx,T(2)(15)(superiore_dx)])
#VIEW(superiore)

vista_complessiva = STRUCT([T(1)(-17)(laterale), T(2)(-8)(frontale), T([1,2])([-17,-7.5])(superiore)])
#VIEW(vista_complessiva)



############################################### TOTALE ESERCIZIO 2 + 3 + 4 + 5 ###############################################

VIEW(STRUCT([vista_complessiva, ruote_tot, volante_t, COLOR([1,0,0])(cofano_interno_traslato), COLOR([1,0,0])(specchietti)]))