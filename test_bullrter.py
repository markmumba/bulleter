import unittest
import bullrter

# import tracemalloc

# tracemalloc.start()
class TestFiles(unittest.TestCase):
    
    def test_get_data(self):
        
        with open('safe.txt', 'r') as f:
            data=f.read()
            self.assertEqual(data,bullrter.read_file('safe.txt'))
            f.close()
    
    def test_convert_file(self):
        n=open('new.txt','w')
        f=open('safe.txt' ,'r')
        
        for x in f:
            output ="*" + x.title()
            n.write(output)
        f.close()    
        new=open('new.txt','r')
        self.assertTrue(output,new.read()) 
        
        new.close()   
        
            
# Snapshot= tracemalloc.take_snapshot()
# top_stats= Snapshot.statistics('lineno')    

# print("[Top 10 ]")
# for stat in top_stats[:10]:
#     print(stat)

if __name__=='__main__':
    unittest.main()
    