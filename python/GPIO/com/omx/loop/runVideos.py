'''
Created on Jun 21, 2017

@author: 390607
'''
import os
import time
import subprocess
#os.system("date")
#print(os.getcwd())


# define the Vehicle class
class RunVideos:
    path = 'D:\\IDM'
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
    
    def executeVideosFiles(self):
        

        #subprocess.call(['ls', '-ltr'])

                
        while True:
            print("Starting Over from path %s \n\n" %self.path )
            listing = os.listdir(self.path)
            for infile in listing:
                print ("current file is: " + infile)
                try:
                    if "Agilent" in infile:
                        time.sleep(10)
                        print("File contains succeed")                        
                    else:
                        time.sleep(10)
                        print("Files not contain agilent")
                except ValueError:
                    print("Oops!  That was no valid number.Try again...")
                except IOError:
                    print('An error occured trying to read the file.')
                except:
                    print('An error occured.')    
# your code goes here
car1 = RunVideos()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00
print(car1.description())


videos = RunVideos()
try:
    videos.executeVideosFiles();
except KeyboardInterrupt:
    print('You cancelled the operation.\n\n\n')


    
    

    




    