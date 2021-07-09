# survival-of-the-squares          

## RULES        
Any live cell with fewer than two live neighbours dies, as if by underpopulation.           
Any live cell with two or three live neighbours lives on to the next generation.                   
Any live cell with more than three live neighbours dies, as if by overpopulation.                     
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.                          
These rules, which compare the behavior of the automaton to real life, can be condensed into the following:                 

Any live cell with two or three live neighbours survives.                               
Any dead cell with three live neighbours becomes a live cell.                                        
All other live cells die in the next generation. Similarly, all other dead cells stay dead.                                                  

let' get started!

## how to run it?
step 1: Run `git clone https://github.com/mishraabhi0123/survival-of-the-squares.git`        
step 2: Create a Python Virtual Environment (Optional) by running `python -m venv env`     
step 3: Activate the environment (only if step 2)
- `source env/bin/activate` for Linux            
- `.\env\Scripts\activate` for Windows           
       
step 4: Install dependencies by running `pip install -r requirements.txt`    
step 5: Run `squares.py` by `python squares.py`   
