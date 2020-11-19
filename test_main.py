import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_graph(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_y)==10, "you have plotted the wrong number of points in your graph" )
        filedata = np.loadtxt("md_results.txt")
        for i in range(len(this_y) ) :
            self.assertTrue( np.abs(filedata[i,0] - this_x[i])<1E-6, "the x-coordinates for the points in your graph are incorrect" )
            cv_val = filedata[i,3] - filedata[i,1]*filedata[i,1]
            cv_val = cv_val / (filedata[i,0]*filedata[i,0] )
            self.assertTrue( np.abs(cv_val - this_y[i])<1E-6, "the y-coordinates for the points in your graph are incorrect" )
