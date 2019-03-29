# mccg
Repository for the Monash computational chemistry group

# automating workflows
## [qcp](github.com/tommason14/qcp)- Quantum Chemical Processor
Automate processes such as 
- creating input and job files
- recursive parsing of log files
- recursive submission of jobs 

Currently installed on Raijin, Magnus, Monarch, Massive and Stampede. Implemented for GAMESS, PSI4 and Gaussian calculations

## gamess_to_molden.py
Parse GAMESS log files for use with [molden](http://cheminf.cmbi.ru.nl/molden/), allowing for easy viewing of geometries and frequencies generated using the FMO approach.
