from sys import stdin
from collections import deque
import time

"""
en icpc live archive : time limit
casos de prueba: funciona con los casos de prueba y falla con un solo caso de udebug

autor: Juan Esteban Floyd Jimenez
codigo: 8943655

codigo de honor:
Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.

complejidades temporal = O(4^n * m^2)
complejidad espacial = O (4^n * m^2)

n = estados
m = size de la matriz

"""

class Estado:

    def __init__(self):

        self.n = 0          # tamaño 
        self.casilla = [ ]  # casillas
       
    def copiar( self ):

        """
        Entrada: recibe la instancia de la clase
        Descripcion: crea una copia de algun estado 
        Salida: retorna la copia del estado
        """

        # Crea un nuevo estado
        ans = Estado()
        
        #asigna valores y caracteristicas de un nuevo estado
        ans.n = int(self.n)
        ans.casilla = [ list(fila) for fila in self.casilla ]
       
        return ans

    def estado_vacio( self, n ):

        """
        Entrada: recibe la instancia de la clase y un size para el estado
        Descripcion: crea un estado donde todas las casillas son un valor nulo
        Salida: no tiene retorno, pero genera un estado donde todas las casillas tienen el valor nulo
        """

        # tamaño de casillas
        self.n = n*2 - 1

        #inicializa con valores nulos
        self.casilla = [ [ self.valor_nulo() for _ in range(n*2 - 1) ] for _ in range(n*2 - 1) ]

    def valor_nulo( self ):

        """
        Entrada: recibe la instancia de la clase 
        Descripcion: retorna "-" que significa que es una casilla donde se puede mover una canica con facilidad
        Salida: retorna "-" que significa que es una casilla donde se puede mover una canica con facilidad
        """

        #valor por defecto cuando una casilla esta disponible
        return '-'

    def valor_canica( self, num ):

        """
        Entrada: recibe la instancia de la clase y un numero 
        Descripcion: retorna "C#" que significa que es la canica asociada a un numero num, asi mismo para distinguir que canica 
        debe ir en que agujero
        Salida: retorna un string C concatenado con un numero num
        """

        #canica de la forma C#, donde # es el numero de la canica para asi mismo reconocer esta
        return "C"+str(num)

    def valor_pared( self ):

        """
        Entrada: recibe la instancia de la clase 
        Descripcion: retorna "#" que significa que es una casilla donde se encuentra una pared
        Salida: retorna "#" que significa que es una casilla donde se encuentra una pared

        """

        #pared se reconoce como "#"
        return "#"
    
    def valor_agujero( self, num ):

        """
        Entrada: recibe la instancia de la clase y un numero 
        Descripcion: retorna "A#" que significa que es un agujero asociada a un numero num, asi mismo para distinguir que canica 
        debe ir en que agujero
        Salida: retorna un string A concatenado con un numero num
        """

        #agujero de la forma A#, donde # es el numero de la canica para asi mismo reconocer esta
        return "A"+str(num)

    def crear_Estado( self, n, canicas, paredes ):

        """
        Entrada: recibe la instancia de la clase, un size para el tablero, una cantidad de coordenadas para las canicas y una cantidad de 
        coordenadas para las paredes 
        Descripcion: retorna un estado que consta de un tablero de size n, con una cierta cantidad de canicas, agujeros y paredes
        repartidas a lo largo del mapa
        Salida: un estado de size n*2 - 1, una cierta cantidad de canicas, de paredes, etc.
        """
        # Crea un estado por defecto
        self.estado_vacio( n )

        # obtiene las posiciones de las canicas
        for i in range( canicas ): 
            x, y = map(int, stdin.readline().strip().split())
            self.casilla[x*2][y*2] = self.valor_canica( i+1 )

        # obtiene posiciones de los agujeros
        for i in range( canicas ): 
            x, y = map(int, stdin.readline().strip().split())
            self.casilla[x*2][y*2] = self.valor_agujero( i+1 )

        # obtiene las posiciones de las paredes
        for _ in range( paredes ):
            x1, y1, x2, y2 = map(int, stdin.readline().strip().split())
            if (x1 == x2):
                self.casilla[x1+x2][y1 + y2] = self.valor_pared()
            else:
                self.casilla[x1 + x2][y1+y2] = self.valor_pared()
            
    def mover_izquierda( self ):
        """
        Entrada: recibe la instancia de la clase
        Descripcion: mueve todas las canicas hacia lo mas a la izquierda que se pueda, segun las reglas del juego
        Salida: si el movimiento es valido
        """
        ans, i = True, 0

        # Recorrer hasta la ultima posicion
        while ( i < self.n and ans ):
            
            # Inicializacion del iterador para columnas y el limite
            j, limite = 0, [ 0 ]

            while ( j < self.n and ans ):

                # Si tengo detras una pared, actualizar el limite
                if ( j-1 >= 0 and self.casilla[i][j-1] == self.valor_pared() ):
                    limite.append(j)

                elif ( self.casilla[i][j][0] == self.valor_canica(0)[0] ):

                    # Sino estoy situado en el limit
                    if ( j != limite[-1] ):
                        
                        # Si el limite esta apuntando a un agujero
                        if ( self.casilla[i][limite[-1]][0] == self.valor_agujero(0)[0] ):
                            
                            # Es el agujero para la canica sobre la que estoy situado
                            ans = ans and self.valor_agujero(int(self.casilla[i][j][1:])) == self.casilla[i][limite[-1]]

                            if ( ans ): 

                                # En caso tal de que si inserto la canica en dicha posicion y elimino el agujero y la canica
                                self.casilla[i][j], self.casilla[i][limite[-1]] = self.valor_nulo(), self.valor_nulo()
                                limite.pop()
                        else:

                            #si no es, entonces se mueve y actualiza una posicio adelante 
                            self.casilla[i][j], self.casilla[i][limite[-1]] = self.valor_nulo(), self.casilla[i][j]
                            limite.append(limite[-1] + 2) #cambia el limite
                    else:

                        #si estoy situado en el limite, actualizo el limite
                        limite.append(limite[-1] + 2)

                #si en  la casilla hay un agujero, cambia el limite       
                elif ( self.casilla[i][j][0] == self.valor_agujero(0)[0] ):
                    #actualiza el limite
                    limite.append(j)

                j += 2
            i += 2

        return ans

    def mover_derecha( self ):

        """
        Entrada: recibe la instancia de la clase
        Descripcion: mueve todas las canicas hacia lo mas a la derecha que se pueda, segun las reglas del juego
        Salida: si el movimiento es valido
        """

        ans, i = True, self.n-1

        # Recorrer hasta la ultima posicion
        while ( i > -1 and ans ):

             # Inicializacion del iterador para columnas y el limite
            j, limite = self.n-1, [ self.n-1 ]

            while ( j > -1 and ans ):

                # Si tengo detras una pared, actualizar el limit
                if ( j + 1 < self.n and self.casilla[i][j+1] == self.valor_pared() ):
                    limite.append(j)

                elif ( self.casilla[i][j][0] == self.valor_canica(0)[0] ):

                    # Sino estoy situado en el limit
                    if ( j != limite[-1] ):

                        # Si el limite esta apuntando a un agujero
                        if ( self.casilla[i][limite[-1]][0] == self.valor_agujero(0)[0] ):
                            # Es el agujero para la canica sobre la que estoy situado
                            ans = ans and self.valor_agujero(int(self.casilla[i][j][1:])) == self.casilla[i][limite[-1]]

                            if ( ans ): 

                                # En caso tal de que si inserto la canica en dicha posicion y elimino el agujero y la canica
                                self.casilla[i][j], self.casilla[i][limite[-1]] = self.valor_nulo(), self.valor_nulo()
                                limite.pop()
                        else:

                            #si no es, entonces se mueve y actualiza una posicio adelante 
                            self.casilla[i][j], self.casilla[i][limite[-1]] = self.valor_nulo(), self.casilla[i][j]
                            limite.append(limite[-1] - 2)
                    else:
                        #si estoy situado en el limite, actualizo el limite
                        limite.append(limite[-1] - 2)
                
                #si en  la casilla hay un agujero, cambia el limite  
                elif ( self.casilla[i][j][0] == self.valor_agujero(0)[0] ):

                    #actualiza el limite
                    limite.append(j)

                j -= 2
            i -= 2
        return ans

    def mover_arriba( self ):

        """
        Entrada: recibe la instancia de la clase
        Descripcion: mueve todas las canicas hacia lo mas hacia arriba que se pueda, segun las reglas del juego
        Salida: si el movimiento es valido
        """

        ans, i = True, 0

        # Recorrer hasta la ultima posicion
        while ( i < self.n and ans ):
            # Inicializacion del iterador para filas y el limite
            j, limite = 0, [ 0 ]

            while ( j < self.n and ans ):

                # Si tengo detras una pared, actualizar el limit
                if ( j-1 >= 0 and self.casilla[j-1][i] == self.valor_pared() ):
                    limite.append(j)

                elif ( self.casilla[j][i][0] == self.valor_canica(0)[0] ):
                    
                    # Sino estoy situado en el limit
                    if ( j != limite[-1] ):

                        # Si el limite esta apuntando a un agujero
                        if ( self.casilla[limite[-1]][i][0] == self.valor_agujero(0)[0] ):

                            # Es el agujero para la canica sobre la que estoy situado
                            ans = ans and self.valor_agujero(int(self.casilla[j][i][1:])) == self.casilla[limite[-1]][i]

                            if ( ans ): 

                                # En caso tal de que si inserto la canica en dicha posicion y elimino el agujero y la canica
                                self.casilla[j][i], self.casilla[limite[-1]][i] = self.valor_nulo(), self.valor_nulo()
                                limite.pop()
                        else:
                             #si no es, entonces se mueve y actualiza una posicio adelante 
                            self.casilla[j][i], self.casilla[limite[-1]][i] = self.valor_nulo(), self.casilla[j][i]
                            limite.append(limite[-1] + 2)
                    else:
                        #si estoy situado en el limite, actualizo el limite
                        limite.append(limite[-1] + 2)

                #si en  la casilla hay un agujero, cambia el limite 
                elif ( self.casilla[j][i][0] == self.valor_agujero(0)[0] ):

                    #actualiza el limite
                    limite.append(j)

                j += 2
            i += 2
        return ans
                        
    def mover_abajo( self ):

        """
        Entrada: recibe la instancia de la clase
        Descripcion: mueve todas las canicas hacia lo mas hacia abajo que se pueda, segun las reglas del juego
        Salida: si el movimiento es valido
        """

        ans, i = True, self.n-1

        # Recorrer hasta la ultima posicion
        while ( i > -1 and ans ):

            # Inicializacion del iterador para filas y el limite
            j, limite = self.n-1, [ self.n-1 ]

            while ( j > -1 and ans ):
                
                # Si tengo detras una pared, actualizar el limit
                if ( j + 1 < self.n and self.casilla[j+1][i] == self.valor_pared() ):
                    limite.append(j)

                elif ( self.casilla[j][i][0] == self.valor_canica(0)[0] ):

                    # Sino estoy situado en el limit
                    if ( j != limite[-1] ):

                        # Si el limite esta apuntando a un agujero
                        if ( self.casilla[limite[-1]][i][0] == self.valor_agujero(0)[0] ):

                            # Es el agujero para la canica sobre la que estoy situado
                            ans = ans and self.valor_agujero(int(self.casilla[j][i][1:])) == self.casilla[limite[-1]][i]

                            if ( ans ): 
                                
                                # En caso tal de que si inserto la canica en dicha posicion y elimino el agujero y la canica
                                self.casilla[j][i], self.casilla[limite[-1]][i] = self.valor_nulo(), self.valor_nulo()
                                limite.pop()
                        else:
                            #si no es, entonces se mueve y actualiza una posicion adelante
                            self.casilla[j][i], self.casilla[limite[-1]][i] = self.valor_nulo(), self.casilla[j][i]
                            limite.append(limite[-1] - 2)
                    else:

                        #si estoy situado en el limite, actualizo el limite
                        limite.append(limite[-1] - 2)

                #si en  la casilla hay un agujero, cambia el limite       
                elif ( self.casilla[j][i][0] == self.valor_agujero(0)[0] ):
                    #actualiza el limite
                    limite.append(j)

                j -= 2
            i -= 2
        return ans


    def mostrar( self ):

        """
        Entrada: recibe la instancia de la clase
        Descripcion: imprime un estado en especifico
        Salida: el estado segun el momento en el que se ejecute
        """

        # mostrar algun estado
        for fila in self.casilla: print('\t'.join(fila))
        print('')


class Juego:

    def __init__(self):
        
        self.inicial = Estado() # Estado inicial
        self.movimientos = [ 'izquierda', 'derecha', 'arriba', 'abajo' ]   #movimientos permitidos en el juego

    def objetivo( self, estado ):


        """
        Entrada: recibe la instancia de la clase y un estado especifico
        Descripcion: verifica si algun estado especifico es el estado objetivo (con el que puedo ganar)
        Salida: si es el estado objetivo o no
        """

        # iterador de filas por defecto
        ans, i = True, 0
        
        while ( i < estado.n and ans ):
            j = 0

            while ( j < estado.n and ans ):

                # si el estado es nulo 
                ans = ans and estado.casilla[i][j] == estado.valor_nulo()
                j += 2
            i += 2
            
        return ans

    def crear_juego( self, n, canicas, paredes ):
        """
        Entrada:recibe la instancia de la clase, un size para el tablero, una cantidad de coordenadas para las canicas y una cantidad de 
        coordenadas para las paredes
        Descripcion: crea un estado segun el size del tablero, el numero de canicas, agujeros y el numero de paredes
        Salida: no tiene retorno, pero inicial se vuelve un estado con las especificaciones que se pasaron por parametro
        """
        # crea el estado origen
        self.inicial.crear_Estado( n, canicas, paredes )

    def movimiento( self, estado, movimiento ):

        """
        Entrada: recibe la instancia de la clase, un estado  y un movimiento
        Descripcion: se ejecuta en el estado pasado por parametro, el movimiento pasado por parametro
        Salida: la validez del movimiento
        """

        #para cada uno de los movimientos, se llaman con su respectivo metodo

        validador = True
        if ( movimiento == 'izquierda' ): validador = estado.mover_izquierda()
        elif ( movimiento == 'derecha' ): validador = estado.mover_derecha()
        elif ( movimiento == 'arriba' ): validador = estado.mover_arriba()
        else: validador = estado.mover_abajo()

        return validador

    def bfs( self ):

        """
        Entrada: recibe la instancia de la clase
        Descripcion: ejecuta movimientos a un estado, estos mismos afectan el estado, se cuentan que movimientos se generaron 
        hasta llegar al estado objetivo, que es donde se gana el juego.
        Salida: la cantidad de movimientos ejecitados, si la varible es none, no se puede ganar el juego
        """
        ans, queue = None, deque()
        limite = 5000

        #cola que almacena el numero de movimientos, estado
        queue.append([[], self.inicial])

        while (len(queue) and limite):

            estado = queue.popleft()

            for movimiento in self.movimientos:
                
                #n= movimientos generados, hijo = copia del estado
                n, hijo = list(estado[0]), estado[1].copiar()

                #se agrega el movimiento generado
                n.append(movimiento)

                #res = movimiento aplicado al hijo, cambios segun el movimiento
                res = self.movimiento( hijo, movimiento )
                #hijo.mostrar()
                #time.sleep(3)
                #print(self.objetivo(hijo))

                #si todavia no es el estado objetivo
                if ( not self.objetivo(hijo) ):

                    if ( res ):

                        #temporal me almacena, los movimientos y el estado
                        tmp = [ n, hijo ]

                        #se agregan a la cola
                        queue.append( tmp )
                else:
                    #si es el objetivo queue se restablece y ans= obtiene la cantidad de movimientos
                    queue, ans = deque(), len(n)
                    break
                    
            limite -= 1

        return ans


    def correr( self ):

        """
        Entrada: recibe la instancia de la clase
        Descripcion: crea un estado, segun el size del tablero, una cierta cantidad de coordenadas de canicas y 
        una cantidad de coordenadas de paredes 
        Salida: si es posible ganar el juego en una n cantidad de movimientos o si es imposible ganarlo
        """

        n, canicas, paredes = map(int, stdin.readline().strip().split())
        caso = 1

        while ( n or canicas or paredes ):

            self.crear_juego( n, canicas, paredes )

            estado = self.inicial.copiar()
            ans = self.bfs()

            if ( ans != None ):
                #print(n,canicas,paredes)
                print("Case " + str(caso) + ": " + str(ans) + " moves\n")
            else:
                #print(n,canicas,paredes)
                print("Case " + str(caso) + ": " + "impossible\n")

            caso += 1
            n, canicas, paredes = map(int, stdin.readline().strip().split())


def main():

    juego = Juego()
    juego.correr()

main()

