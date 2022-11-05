#!/usr/bin/env python

'''
APOPT Online Solver for Mixed Integer Nonlinear Programming
 Reads output from AMPL, Pyomo, or other NL File Writers. Similar to other 
 solvers, this script reads the model (NL) file and produces a solution (sol) file.
 It sends the NL file to a remote server, computes a solution (remotely), and 
 retrieves a solution (sol) file through an internet connection. It communicates
 with the server https://byu.apopt.com that is hosting the APOPT solver. Contact
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
'''

# Import
import os
import sys
import string
from contextlib import closing

# Get Python version
ver = sys.version_info[0]
print('Version: '+str(ver))
if ver==2:  # Python 2
    import urllib    
else:       # Python 3+
    import urllib.request, urllib.parse, urllib.error
    import socket

def aps(server,app,aline):
    '''Send a request to the server \n \
       server = address of server \n \
       app      = application name \n \
       aline  = line to send to server \n'''
    try:
        # Web-server URL address
        url_base = server.strip() + '/online/apopt.php'
        app = app.lower()
        app.replace(" ","")
        if ver==2:  # Python 2
            params = urllib.urlencode({'p':app,'a':aline})
            f = urllib.urlopen(url_base,params)
            response = f.read()
        else:       # Python 3+
            params = urllib.parse.urlencode({'p':app,'a':aline})
            en_params = params.encode()
            f = urllib.request.urlopen(url_base,en_params)
            en_response = f.read()
            response = en_response.decode()
    except:
        response = 'Failed to connect to server'
    return response

def nl_load(server,app,filename):
    '''Load NL model file \n \
       server   = address of server \n \
       app      = application name \n \
       filename = NL file name'''
    # Load NL File
    f = open(filename,'r')
    aline = f.read()
    f.close()
    app = app.lower()
    app.replace(" ","")
    response = aps(server,app,' '+aline)
    y = 'Loaded NL file'
    return y

def aps_ip(server):
    '''Get current IP address \n \
       server   = address of server'''
    # get ip address for web-address lookup
    url_base = server.strip() + '/ip.php'
    if ver==2:   # Python 2
        f = urllib.urlopen(url_base)
        ip = string.strip(f.read())
    else:        # Python 3+
        f = urllib.request.urlopen(url_base)
        fip = f.read()
        ip = fip.decode().strip()
    return ip

def aps_sol(server,app,stub):
    '''Retrieve solution results\n \
       server   = address of server \n \
       app      = application name '''
    # Retrieve IP address
    ip = aps_ip(server)
    # Web-server URL address
    app = app.lower()
    app.replace(" ","")
    url = server.strip() + '/online/' + ip + '_' + app + '/' + ip + '_' + app + '.sol'

    if ver==2:  # Python 2
        f = urllib.urlopen(url)
    else:       # Python 3+
        f = urllib.request.urlopen(url)

    # Send request to web-server
    solution = f.read()    # Write the file

    # Write the file
    sol_file = stub + '.sol'
    fh = open(sol_file,'w')

    # possible problem here if file isn't able to open
    if ver==2:
        fh.write(solution.replace('\r',''))
    else:
        en_solution = solution.decode().replace('\r','')
        fh.write(en_solution)
    fh.close()        

    # Return message
    y = 'Successfully returned sol file'
    return y

def aps_option(server,app,name,value):
    '''Load APOPT option \n \
       server   = address of server \n \
       app      = application name \n \
       name     = option \n \
       value    = numeric value of option '''
    aline = 'option %s %f' %(name,value)
    app = app.lower()
    app.replace(" ","")
    response = aps(server,app,aline)
    return response

#print('Number of arguments:', len(sys.argv))
#print('Argument list:', str(sys.argv))

stub = ''
retrieve_solution = True 
for i in range(1,len(sys.argv)):
    arg = sys.argv[i]
    if (arg[0]=='-'):
        if (arg[1]=='?'):
            print('APOPT Online Solver')
            print('Usage:')
            print('  -?   : Show possible flags and options')
            print('  -s   : Return solution (sol) file')
            print('  -AMPL: Return solution (sol) file')
            print('  -test: Test installation')
            print('')
            print('Default option values are listed below')
            print('  minlp_maximum_iterations = 10000')
            print('  minlp_max_iter_with_int_sol = 500')
            print('  minlp_as_nlp = 0')
            print('  minlp_branch_method = 3')
            print('  minlp_gap_tol = 1.0e-2')
            print('  minlp_integer_tol = 1.0e-2')
            print('  minlp_integer_max = 2.0e9')
            print('  minlp_integer_leaves = 1')
            print('  minlp_print_level = 1')
            print('  nlp_maximum_iterations = 500')
            print('  objective_convergence_tolerance = 1.0e-6')
            print('  constraint_convergence_tolerance = 1.0e-6')
            print('Note: Adjust solver options in apopt.py')
        elif (arg[1].lower()=='t'):
            # write example nl file
            stub = 'test'
            nl_file = stub + '.nl'
            fh = open(nl_file,'w')
            fh.write('g3 0 1 0\n')
            fh.write(' 1 1 1 0 0\n')
            fh.write(' 1 1\n')
            fh.write(' 0 0\n')
            fh.write(' 1 1 1\n')
            fh.write(' 0 0 0 1\n')
            fh.write(' 0 0 0 0 0\n')
            fh.write(' 1 1\n')
            fh.write(' 0 0\n')
            fh.write(' 0 0 0 0 0\n')
            fh.write('C0\n')
            fh.write('o16\n')
            fh.write('o5\n')
            fh.write('v0\n')
            fh.write('n2\n')
            fh.write('O0 0\n')
            fh.write('o5\n')
            fh.write('v0\n')
            fh.write('n2\n')
            fh.write('x1\n')
            fh.write('0 0.5\n')
            fh.write('r\n')
            fh.write('1 -1\n')
            fh.write('b\n')
            fh.write('3\n')
            fh.write('k0\n')
            fh.write('J0 1\n')
            fh.write('0 1\n')
            fh.write('G0 1\n')
            fh.write('0 0\n')
            fh.close()
        elif ((arg[1].lower()=='a') or (arg[1].lower()=='s')):
            retrieve_solution = True
    else:
        stub = os.path.splitext(arg)[0]

if (len(stub)>=1):
    # server and application name
    # can use https if needed
    s = 'http://byu.apopt.com'
    a = ''.join(e for e in stub if e.isalnum())

    # clear prior application
    aps(s,a,'clear all')

    # load nl file
    nl_load(s,a,stub+'.nl')

    # adjustable solver options
    aps_option(s,a,'minlp_maximum_iterations',10000)
    aps_option(s,a,'minlp_max_iter_with_int_sol',500)
    aps_option(s,a,'minlp_as_nlp',1) # only NLP is currently working
    aps_option(s,a,'minlp_branch_method',3)
    aps_option(s,a,'minlp_gap_tol',1.0e-2)
    aps_option(s,a,'minlp_integer_tol',1.0e-2)
    aps_option(s,a,'minlp_integer_max',2.0e9)
    aps_option(s,a,'minlp_integer_leaves',1)
    aps_option(s,a,'minlp_print_level',1)
    aps_option(s,a,'nlp_maximum_iterations',500)
    aps_option(s,a,'objective_convergence_tolerance',1.0e-6)
    aps_option(s,a,'constraint_convergence_tolerance',1.0e-6)

    # solve
    output = aps(s,a,'solve')
    print(output)

    # retrieve solution (sol) file
    if retrieve_solution:
        aps_sol(s,a,stub)

    # clear solution folder
    output = aps(s,a,'clear all')
