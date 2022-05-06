import pandas as pd
import shutil


class fileRead:
    def main():

        try:
            fileRead.File = open("./file.txt","r")
           

            data = fileRead.File.read()
            print(data)
            
            
            print(data.count("world"))
            
            count = data.lower()
            print(data.count("Hello"))

            coun = data.upper()
            print(data.count("hello"))
            
            with open("file.txt", "r") as input:
                
                with open("files.txt", "w") as output:
                    for line in input:
                         output.write(line)
                         

                        

            
            
        except Exception as e:
            print("exception is", e)

        finally:
            if fileRead.File!=None:
                fileRead.File.close()

           
        return
           
fileRead.main()
            
