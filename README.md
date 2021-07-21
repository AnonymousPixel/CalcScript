# CalcScript
----
Calcscript is a python-based, simple algorithmic parser. Using Calcscript, it is possible to write simple algorithms with I/O functionality.

**NOTE:** *Each file must start with `LP INF` or `LP MAN`. `LP INF` Will infinitly loop the program until `END` is called (And confirmed), `LP MAN` will loop the file once.*
## Commands
- `-` title, will print only once, even in `LP INF`; `-Calculator`. Will only work if it is on the second line after `LP INF` or `LP MAN`.
- `STA/STB/STC` sets variable `A/B/C` to a certain value; `STA 18`
- `ISA/ISB/ISC` sets variable `A/B/C` using python's `input()` function; `ISB`
- `A++/B++/C++` adds one to `A/B/C`
- `A--/B--/C--` subtracts one from `A/B/C`
- `(A/B/C) (+,-,/,*,^) (A/B/C)` calculates using basic operators and stores result in first variable; `A+B` *Will add `A` and `B` and store the result in `A`.*
- `ASQ/BSQ/CSQ` Square-roots `A/B/C`; `SQA`
- `MIN (VA/VB/VC) (VA/VB/VC)` sets lowest value to first variable; `MIN VA VB`
- `MAX (VA/VB/VC) (VA/VB/VC)` sets highest value to first variable; `MAX VA VB`
- `MEN(VA/VB/VC) (VA/VB/VC)` sets mean value of two params  to first variable; `MEN VA VB`
- `CLR` clears screen
  
All other text will be printed as string, variables can be embedded like so: `>A`, `>B` or `>C`; `Sqrt of >B is: >C`

## Github
The CalcScript~~.py~~.exe file is the 'interperter' which will read the main.ccs file
