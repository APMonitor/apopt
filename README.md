APOPT Solver

APOPT (for Advanced Process OPTimizer) is a software package for solving large-scale optimization problems of any of these forms:

Linear programming (LP)
Quadratic programming (QP)
Quadratically constrained quadratic program (QCQP)
Nonlinear programming (NLP)
Mixed integer programming (MIP)
Mixed integer linear programming (MILP)
Mixed integer nonlinear programming (MINLP)

Applications of the APOPT include chemical reactors, friction stir welding, prevention of hydrate formation in deep-sea pipelines, 
computational biology, solid oxide fuel cells, and flight controls for Unmanned Aerial Vehicles (UAVs). APOPT is supported in
AMPL, APMonitor, and Pyomo.

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

Information on the APOPT solver with references can be found at
 https://wikipedia.org/wiki/APOPT
Besides this Python client version, local executable versions of the solver are
 available in Linux and Windows.

---BSD License---

Copyright (c) 2016, Advanced Process Solutions, LLC
 All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list
of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or other
materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may
be used to endorse or promote products derived from this software without specific
prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
