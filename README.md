APOPT Solver

APOPT (for Advanced Process OPTimizer) is a software package for solving large-scale optimization problems of any of these forms:

* Linear programming (LP)
* Quadratic programming (QP)
* Quadratically constrained quadratic program (QCQP)
* Nonlinear programming (NLP)
* Mixed integer programming (MIP)
* Mixed integer linear programming (MILP)
* Mixed integer nonlinear programming (MINLP)

Applications of the APOPT include chemical reactors, friction stir welding, prevention of hydrate formation in deep-sea pipelines, 
computational biology, solid oxide fuel cells, and flight controls for Unmanned Aerial Vehicles (UAVs). APOPT is supported in
AMPL, [APMonitor](http://apmonitor.com), [Gekko](https://gekko.readthedocs.io/en/latest/), and Pyomo.

APOPT Online Solver for Mixed Integer Nonlinear Programming
 Reads output from AMPL, Pyomo, or other NL File Writers. Similar to other 
 solvers, this script reads the model (NL) file and produces a solution (sol) file.
 It sends the NL file to a remote server, computes a solution (remotely), and 
 retrieves a solution (sol) file through an internet connection. It communicates
 with the server http://byu.apopt.com that is hosting the APOPT solver. Contact
 support@apmonitor.com for support, especially if there is a feature request or a 
 concern about a problem solution.

Instructions for usage:
 1. Place apopt.py in an appropriate folder in the system path (e.g. Linux, /usr/bin/)
 2. Set appropriate permissions to make the script executable (e.g. chmod 775 apopt.py)
 3. In AMPL, Pyomo, or other NL file write, set solver option to apopt.py
 4. Test installation by running apopt.py -test
 5. Visit apopt.com for additional information and solver option help

Information on the APOPT solver with references can be found at the [Wikipedia article for APOPT](https://wikipedia.org/wiki/APOPT). Besides this Python client version, local executable versions of the solver are available in Linux and Windows.
