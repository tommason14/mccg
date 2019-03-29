# mccg
Repository for the Monash computational chemistry group

# automating workflows
## [qcp](https://github.com/tommason14/qcp)- Quantum Chemical Processor
Automate processes such as 
- creating input and job files
- recursive parsing of log files
- recursive submission of jobs, deletion of queued jobs
- Finding bond distances of xyz files

Currently installed on Raijin, Magnus, Monarch, Massive and Stampede. Implemented for GAMESS, PSI4 and Gaussian calculations

## generation of LAMMPS input files
Scripts to generate a LAMMPS input file, along with a data file containing the appropriate force field parameters, given an xyz file with numbered atoms.

## view_hessian_calculation.ipynb
Takes a GAMESS log file as an input and produces an infrared spectra along with a molecule viewer to view all the vibrational modes of files generated using the FMO approach.

## gamess_to_molden.py
Parse GAMESS log files for use with [molden](http://cheminf.cmbi.ru.nl/molden/), allowing for easy viewing of geometries, convergence, frequencies and vibrational modes generated using the FMO approach (also works with non-FMO).
