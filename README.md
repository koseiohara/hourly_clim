# hourly_clim

This program is to compute climatological mean field.  
The temporal resolution of the output data is the same as that of the input data.  


## Namelist
nml/execmode.nml, nml/files.nml, nml/grid.nml, nml/recinfo.nml, and nml/tinfo.nml are needed to execute the src.

### execmode.nml
Namelist to set parameters 'mode'.  
"DEBUG", "BOTH", and "COMPUTE" are available for this parameter.  
If "DEBUG", climatological mean is not computed and output is only record list in output/Debugger.txt  
If "COMPUTE", only climatological mean is outputed and output/Debugger.txt is not generated.  
If "BOTH", both of files are generated.

### files.nml
Namelist to set parameters 'input_fname' and 'output_fname'.  
'input_fname' is the name to read and 'output_fname' is to write.  
Their file formats are single-precision binary files withot header.

### grid.nml
Namelist to set parameters 'nx', 'ny', and 'nz'.  
They are the grid sizes for input and output data.

### recinfo.nml
Namelist to set parameters 'varnum' and 'input_initialRecord'.  
'varnum' is the number of parameters in the input file.  
See the control file of input file to check VARS.  
'input_initialRecord' is the first record to read.  
If you want to read the n-th variable in control file, input_initialRecord=n.

### tinfo.nml
Namelist to set parameters 'datayear_ini', 'climyear_ini', 'climyear_fin', and 'hourstep'.  
For example, if you read a file that have 1900/01/01-2000/12/31 and
you want to compute the climatological mean from 1930/01/01-1980/12/31, 
datayear_ini=1900, climyear_ini=1930, climyear_fin=1980.  
If the data is 6 hourly, hourstep=6.
