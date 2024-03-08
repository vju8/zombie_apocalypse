from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np



class Zombie_apocalypse:
    
    """
        Class designed to modell a zombie apocalypse. The mathematical 
        modelling used here is based on the Munz et al. 2009, which tackle 
        the problem by having 3 main players (human, zombie, dead) and 
        creating a system of first order ODEs (Ordinary Differential Equations)
        and analyzing the changes over specified time intervals and given 
        parameters. The main time unit is kept as days here.

        The complexity of the system of first order ODEs can be reduced and 
        be given as:
        
        dS/dt = P - BSZ - dS dZ/dt = BSZ + GR - ASZ dR/dt = dS + ASZ - GR
        
        
        
        Following notations were used:        
            S - the number of humans
            Z - the number of zombies
            R - the number of deceased (both humans and zombies)
            
            P - human birth rate (per day)
            d - natural death probability (human dies from anything but zombie)
            B - infection probability (human becomes a zombie)
            G - transition probability (deseased human is resurrected into a zombie)
            A - zombie kill probability (human kills zombie)
    
            S0 - initial number of humans
            Z0 - initial number of zombies
            R0 - initial number of deceased (both humans and zombies)
            Zc - percentage of zombie in human population (for calculation of Z0)
            Rc - percentage of deceased in human population (for calculation of R0)
    
    """
    
    d = 0.0077    
    B = 0.0095   
    G = 0.0005    
    A = 0.005     
    
    def __init__(self, scenario_title, S0 = 1000, Zc = None, Rc = None, P = None, nr_sim_days = 10):
        
        """
           Constructor method to initialize all the beginning attribute 
           variables of the class. 
        """
        
        self.S0 = S0                   
        
        if Zc is None:
            self.Z0 = 0             
        else:
            self.Z0 = Zc * self.S0
        
        if Rc is None:    
            self.R0 = 0               
        else:    
            self.R0 = Rc * self.S0
            
        if P is None:
            self.P = 0                 
        else:
            self.P = P   
        
        self.y0 = [self.S0, self.Z0, self.R0]         
        self.scenario_title = scenario_title
        self.timeline = np.linspace(0, nr_sim_days, 1000)         
        self.nr_sim_days = nr_sim_days
        

    def diff_eq_solver(self, y, t):
        """
            Function responsible for solving the system of first order ODEs
            given by given by: dy/dt = f(y, t), where y is characterized by
            the variables S, Z, R.

        Parameters
        ----------
        y : list
            List of variables S, Z, R for which the first order ODEs must be 
            solved.
        t : numpy.ndarray
            Array representing the timeline and the points in time for which 
            the first order ODEs must be solved.

        Returns
        -------
        list
            Return a list with all the values of the S, Z and R variables 
            change over the specified timeline t.

        """
        
        # solve the system dy/dt = f(y, t)
        Si = y[0]
        Zi = y[1]
        Ri = y[2]
         
        # the model equations (see Munz et al. 2009)
        self.f0 = self.P - self.B*Si*Zi - self.d*Si
        self.f1 = self.B*Si*Zi + self.G*Ri - self.A*Si*Zi
        self.f2 = self.d*Si + self.A*Si*Zi - self.G*Ri 
        return [self.f0, self.f1, self.f2]
    
    
    def scenario_builder(self):
        # solve the system of differential equations
        soln = odeint(self.diff_eq_solver, self.y0, self.timeline)
        self.S = soln[:, 0]
        self.Z = soln[:, 1]
        self.R = soln[:, 2]
    
    
    def plotter(self):
        """
            Function responsible for plotting the results of the zombie 
            apocalypse modelling.

        Returns
        -------
        None.

        """
        plt.ion()
        plt.rcParams['figure.figsize'] = 12, 6
        
        # plot results
        plt.figure()
        plt.plot(self.timeline, self.S, label='Humans')
        plt.plot(self.timeline, self.Z, label='Zombies')
        plt.xlabel('Days from outbreak', fontsize = 14, labelpad = 10)
        plt.ylabel('Population', fontsize = 14, labelpad = 10)
        plt.title(self.scenario_title, fontsize = 16, fontweight = "bold", pad = 10)
        plt.xticks(np.arange(self.nr_sim_days))
        plt.grid(visible = True, axis = "both")
        plt.legend(loc=0)
        plt.savefig(f"{self.scenario_title}.png", bbox_inches='tight', dpi = 200)
        plt.show()
    
    
    
if __name__ == "__main__":
    # SCENARIO 1
    scenario_1 = Zombie_apocalypse(scenario_title = "Zombie Apocalypse - No initial population deceased - no new births")
    scenario_1.scenario_builder()           
    scenario_1.plotter()
    
    # SCENARIO 2
    Rc = 0.015
    scenario_2 = Zombie_apocalypse(Rc = Rc,             
                                   scenario_title = f"Zombie Apocalypse - {Rc * 100}% of initial population deceased - no new births.")
    scenario_2.scenario_builder()           
    scenario_2.plotter()
    
    # SCENARIO 3
    Rc = 0.02
    P = 30
    scenario_3 = Zombie_apocalypse(Rc = Rc,            
                                   P = P,
                                   scenario_title = f"Zombie Apocalypse - {Rc * 100}% of initial population deceased - {P} new daily births")
    scenario_3.scenario_builder()           
    scenario_3.plotter()