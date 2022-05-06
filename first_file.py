import pandas as pd
import shutil


class fileRead:
    def main():

        try:
            fileRead.File = open("./Reader.txt","r")
           

            data = fileRead.File.read()
            print(data)

            
            #######  captialization 

            print("capitlize the data..")
            print(data.title())
            print("capitalize is complate...")

            ####• Write data provided by transformer into another output file in a different directory


            with open("Reader.txt", "r") as input:
                
                with open("writefile.txt", "w") as output:
                    for line in input:
                         diff_dict = output.write(line)
                         print(diff_dict)

                         shutil.copy("E:\First_part\writefile.txt","G:\dict_file")
                         
                        

            
            
        except Exception as e:
            print("exception is", e)

        finally:
            if fileRead.File!=None:
                fileRead.File.close()

           
        return
           
fileRead.main()
            
