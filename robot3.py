from sys import stdin
from heapq import heappop, heappush
from math import *

"""
author: Juan Esteban Floyd Jimenez

student code: 8943655 

Honor Code:
As a member of the academic community of the Pontificia Universidad Javeriana Cali I commit myself to 
to follow the highest standards of academic integrity.

temporal complexity O(n + m * log(n)) = for using dijkstra's algorithm
space complexity O(n * m) = by the matrices used
"""

class BumpyRobot:
    '''
    this class is in charge of representing all the information on the grid of each test case.

    this class stores the grid with all the necessary constants, alpha, beta, gamma, delta, start position, 
    target position, plus all the allowed movements (transverse, i.e. up, down, left and right), finally, 
    it also stores information about the E amount of energy for each test case.
    
    attributes:
        a1: floating-point constant alpha1 for using the energy consumption function.
        a2: floating-point constant alpha2 for using the energy consumption function.
        y: integer constant gamma for using the energy consumption function.
        B1:floating-point constant beta1 for using the time consumption function.
        B2: floating-point constant alpha2 for using the time consumption function.
        delta: integer constant delta for using the time consumption function.
        start: tuple (i (integer),j (integer)) where represents initial position (initial position of the bumpy robot).
        target: tuple (i (integer),j (integer)) where represents target position (position to be reached by the bumpy robot).
        E: Amount E of energy for each test case, which is an integer.
        grid: grid that stores information about the heights, it is an matrix of integers.
        MOVEMENTS: tuple (i (integer),j (integer)) where represents all the allowed movements (transverse, i.e. up, down, left and right).
    '''

    def __init__(self, **kargs):
        
        # Store the constants
        self.a1 = kargs['a1']
        self.a2 = kargs['a2']
        self.y = int(kargs['y'])
        self.B1 = kargs['B1']
        self.B2 = kargs['B2']
        self.delta = int(kargs['delta'])

        # Store the start and target position
        self.start = (kargs['rs'] - 1, kargs['cs'] - 1)
        self.target = (kargs['rt'] - 1, kargs['ct'] - 1)

        # Store the energy value and the Bumpy Robot Grid
        self.E = kargs['E']
        self.grid = kargs['grid']

        # Movements
        self.MOVEMENTS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def energy(self, u, v):
        '''
        this is the energy consumption function.
        args:
            u: position in which the bumpy robot is at that time.
            v: position to which the bumpy robot will move.
        return:
            ans: amount of energy required to move from u to v.
        '''
        ans = None
        
        # Create the h1 and h2 variables to be consecuent with the function notation
        h1, h2  = self.grid[u[0]][u[1]], self.grid[v[0]][v[1]]

        # Conditions of the energy funtion
        if (h1 > h2): ans = (ceil( self.a1*(h1 - h2) ) + self.y)
        elif (h1 == h2): ans = self.y
        else: ans = ( ceil( self.a2*(h2 - h1)) + self.y )

        return ans

    def time(self, u, v):
        '''
        this is the time consumption function.
        args:
            u: position in which the bumpy robot is at that time.
            v: position to which the bumpy robot will move.
        return:
            ans: amount of time required to move from u to v.
        '''
        ans = None

        # Create the h1 and h2 variables to be consecuent with the function notation
        h1, h2  = self.grid[u[0]][u[1]], self.grid[v[0]][v[1]]

        # Conditions of the time funtion
        if (h1 > h2): ans = ( ceil( self.B1*(h1 - h2)) + self.delta )
        elif (h1 == h2): ans = self.delta
        else: ans = ( ceil( self.B2*(h2 - h1)) + self.delta )

        return ans

    def valid_movement(self, pos, mov):
        '''
        this function is to check if a transaction to be executed is valid. 
        The movement is valid if it is crosswise (i.e., up, down, left, right) 
        and if the movement does not go out of the grid. 
        args:
            pos: position in which it is currently located.
            mov: movement to be executed.
        return:
            ans: new position if the move to be executed was valid.
        '''
        ans = None

        # Check if movement not generate a position out of range
        if (pos[0] + mov[0] >= 0 and pos[0] + mov[0] < len(self.grid)):
            if (pos[1] + mov[1] >= 0 and pos[1] + mov[1] < len(self.grid[0])):
                ans = [ pos[0] + mov[0], pos[1] + mov[1] ]
        return ans

class Dijkstra:
    '''
    class executing dijkstra's algorithm.

    dijkstra's algorithm is used because it is a shortest path problem, 
    since it must get from the initial position to the target position 
    in the minimum amount of time possible without consuming more than the amount E of energy for each test case.
    
    attributes:
        INF: value representing infinity.
        BumpyRobot: information about the bumpy robot class for the test case being executed.
        Value: stores time values for some executed movement where there is a time or energy improvement.
        energy: stores energy values for some executed movement where there is a time or energy improvement
        result: Stores the smallest time value of some executed movement in which there is an improvement in time or energy.   
    '''
    def __init__(self, BumpyRobot):

        # Define the INF constant
        self.INF = float('inf')
        
        # Store the Bumpy Robot case
        self.BumpyRobot = BumpyRobot

        # Create value and visited arrays
        self.value = [ [ self.INF for _ in range(len(self.BumpyRobot.grid[0]))] for _ in range(len(self.BumpyRobot.grid)) ]
        self.energy = [ [ self.INF for _ in range(len(self.BumpyRobot.grid[0]))] for _ in range(len(self.BumpyRobot.grid)) ]
        self.result = [ [ self.INF for _ in range(len(self.BumpyRobot.grid[0]))] for _ in range(len(self.BumpyRobot.grid)) ]

        # Store the inititalize its value
        self.value[self.BumpyRobot.start[0]][self.BumpyRobot.start[1]] = 0
        self.result[self.BumpyRobot.start[0]][self.BumpyRobot.start[1]] = 0
        self.energy[self.BumpyRobot.start[0]][self.BumpyRobot.start[1]] = 0

    def calc(self, l):
        '''
        This function is Dijkstra's algorithm, where it is adapted to this specific problem. 
        That is, it calculates the shortest path from the starting position to all other nodes.
        args:
            l: initial position
        '''
        while (len(l)):

            # Get the cost and node
            time, energy, u = heappop(l)

            # Move to adjacent positions
            for mov in self.BumpyRobot.MOVEMENTS:

                # Check if the movements is valid
                v = self.BumpyRobot.valid_movement(u, mov)
                
                # When it is valid
                if (v is not None):

                    # Compute the energy to go for the v position
                    eEnergy = self.BumpyRobot.energy(u, v)

                    # Valid if the maximum energy has not been exceeded.
                    if (eEnergy + energy <= self.BumpyRobot.E):
                        
                        # Compute the time cost to go to v position
                        vtime = self.BumpyRobot.time(u, v)

                        # Check if exists a time or energy improvement
                        if ( time + vtime < self.value[v[0]][v[1]] or eEnergy + energy < self.energy[v[0]][v[1]] ):
                            
                            # Update the vale and energy with the local results, but in result store the best value
                            self.value[v[0]][v[1]] = time + vtime
                            self.result[v[0]][v[1]] = min(time + vtime, self.result[v[0]][v[1]])
                            self.energy[v[0]][v[1]] = eEnergy + energy

                            # Store in the heap queue
                            heappush(l, ( time + vtime, eEnergy + energy, v ))

def solve(**kargs):
    '''
    This function is in charge of calling the function that calculates the shortest paths 
    from an initial position to all the other positions, with all the information of the grid 
    of the case that is being executed at that moment.
    args:
        information about the grid on a specific test case.
    return:
        ans: Minimum time, to reach the target position if possible, otherwise the word 'failed'.
    ''' 
    ans = None

    # Create a dijkstra instance
    dijkstra = Dijkstra(BumpyRobot(
        a1=kargs['a1'], 
        a2=kargs['a2'],
        y=kargs['y'], 
        B1=kargs['B1'], 
        B2=kargs['B2'], 
        delta=kargs['delta'], 
        grid=kargs['grid'], 
        rs=kargs['rs'], 
        cs=kargs['cs'], 
        rt=kargs['rt'], 
        ct=kargs['ct'], 
        E=kargs['E']
    ))

    # Create the init heap queue and put to calc the dijkstra with it
    l = [(0, 0, [dijkstra.BumpyRobot.start[0], dijkstra.BumpyRobot.start[1]])]
    dijkstra.calc(l)

    # Get the value associated with the target position
    ans = dijkstra.result[dijkstra.BumpyRobot.target[0]][dijkstra.BumpyRobot.target[1]]

    # If value was not modified in the dijkstra algorith, assign the message 'failed' to ans variable
    if (ans == dijkstra.INF): 
        ans = 'failed'
    else: ans = int(ans)

    return ans

def main():
    '''
    Function in charge of reading data for each test case and displaying the answer, for this same test case.
    '''
    # Get the m and n value by each case
    m, n = map(int, stdin.readline().strip().split())

    while (m and n):

        # Get Bumpy Robot constants
        a1, a2, y = map(float, stdin.readline().strip().split())
        B1, B2, delta = map(float, stdin.readline().strip().split())

        # Create a Bumpy Robot Grid
        grid = [ list(map(int, stdin.readline().strip().split())) for _ in range(m) ]

        # Get the start and target positions
        rs, cs, rt, ct, E = map(int, stdin.readline().strip().split())

        # Show the answer for this case
        print( solve(a1=a1, a2=a2, y=y, B1=B1, B2=B2, delta=delta, grid=grid, rs=rs, cs=cs, rt=rt, ct=ct, E=E) )

        # Get the m and n value by each case
        m, n = map(int, stdin.readline().strip().split())

main()