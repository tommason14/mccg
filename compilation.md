# PSI4 compilation

Simple binary install. Can install from source, but why go to the hassle?

https://admiring-tesla-08529a.netlify.com/installs/v131/

# Gamess compilation

Gamess requires compilation from source, with readme files given to guide you along the way. 
Steps are as follows:
- download the source from ![here](https://www.msg.chem.iastate.edu/GAMESS/download/register/)
- if compiling for use on multiple compute nodes, ensure that the required mpi libraries are installed or that the required modules are loaded
- follow the steps at machines/readme.unix
- run ./config to set variables for the GAMESS compilation procedure
- compile any source code relating to distribution of information across nodes (DDI or distributed data interface)
- compile all source code
- link to code to an executable



# LAMMPS install

- On MacOS machines, can use Homebrew: `brew install lammps`
- On Windows, pre-compiled installers available ![here](http://packages.lammps.org/windows.html)
- On Linux, pre-built executables are available through various package managers, ie. for Ubuntu distros: `apt-get install lammps-daily` 
