from __future__ import print_function
import pdb
import Pyro4
import threading



class Pig(object):

    def __init__(self, location, pig_id, hit_flag = False):
        self.location=location
        self.pig_id = pig_id
        self.hit_flag = hit_flag
        self.pyroname = Pyro4.Proxy("PYRONAME:"+str(pig_id)+".example")
        
    def send_message(self):
        print("sending message")
        self.pyroname.confirm_message()
        
        
    
    '''  
    def bird_approaching(location,hopcount):
        
    
    def take_shelter(pigID):
    
    def status(pigID):
    def status_all():
    
    def was_hit(pigID ,trueFlag):
    '''

@Pyro4.expose
       
class Pig_Server(Pig):
    def __init__(self):
        Pig.__init__(self, location, pig_id, hit_flag = False)
        
    
    def confirm_message(self):
        print("message received from {0}".format(self.pig_id))

def main():
    Pyro4.Daemon.serveSimple(
            {
                Pig_Server: "0.example"
            },
            ns = False)

if __name__=="__main__":
    main()    