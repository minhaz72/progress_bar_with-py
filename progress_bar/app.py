#progress bar with python : 
import sys 
import time 
def progress_bar_with_py(count, total, suffix='') : 
    barlength= 60 
    filledlength= int(round(barlength *  count / float(total)))
    percent= round(100.0 * count / float(total), 1 )
    bar=' * ' * filledlength + '-' * (barlength-filledlength)
    sys.stdout.write('[%s] %s%s ....... %s/r' % (bar, percent , '% ' , suffix))
    sys.stdout.flush()
    
if __name__=='__main__': 
    for i in range(10): 
        time.sleep(1)
        progress_bar_with_py(i,  10)
        