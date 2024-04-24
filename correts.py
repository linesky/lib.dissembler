import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os
global sself
def prints(txts:str):
    global sself
    sself.text_area.insert(tk.END,txts )
    
def srun(data):
	os.system(data)
		
def scommand(data):
	srun(data)

def slines1(argvs):
     lst1=[]
     f1=open("/tmp/out.txt","r")
     f2=open("/tmp/out.asm","w")
     txt=f1.read()
     f1.close()
     txt=txt.replace("\r","\n")
     txt=txt.replace("\n\n","\n")
     
     txtx=txt.split("\n")
     txt=None
     inss1=None
     inss2=None
     inss3=None
     inss=None
     inss1=None
     inss2=None
     inss3=None
     inss=None
     ina=None
     inaa=None
     inaaa=None
     txx=""
     xtxt1=""
     for n in txtx:
         inss=n.find(">:")
         if inss>-1:
             n=n.replace(">","")
             inss1=n.find("<")
             if inss1>-1:
                 inss1+=1
                 n=n[inss1:]
                 f2.write("\n")
                 f2.write(n+"\n")
         else:
             inss1=n.find(":")
             
             if inss1>-1:
              	inss1+=1
              	n=n[inss1:]

              	xtxt=n.split("	")
              	n1=0
              	if len(xtxt)>2:
              	    xtxt1=xtxt[2]
              	ina=xtxt1.find("jne ")
              	if ina<0:
              	    ina=xtxt1.find("je ")
              	if ina<0:
              	    ina=xtxt1.find("jnz ")
              	if ina<0:
              	    ina=xtxt1.find("jz ")
              	if ina<0:
              	    ina=xtxt1.find("jng ")  
              	if ina<0:
              	    ina=xtxt1.find("jg ") 
              	if ina<0:
              	    ina=xtxt1.find("jpo ")
              	if ina<0:
              	    ina=xtxt1.find("jo ") 
              	if ina<0:
              	    ina=xtxt1.find("je ")
              	if ina<0:
              	    ina=xtxt1.find("jpo ")
              	if ina<0:
              	    ina=xtxt1.find("jne ")
              	if ina<0:
              	    ina=xtxt1.find("jpo ")
              	if ina<0:
              	    ina=xtxt1.find("jb ") 
              	if ina<0:
              	    ina=xtxt1.find("jnb ") 
              	if ina<0:
              	    ina=xtxt1.find("jl ")
              	if ina<0:
              	    ina=xtxt1.find("jle ")
              	if ina<0:
              	    ina=xtxt1.find("jnl ")
              	if ina<0:
              	    ina=xtxt1.find("jg ")
              	if ina<0:
              	    ina=xtxt1.find("jg ")
              	if ina<0:
              	    ina=xtxt1.find("jng ")
              	if ina<0:
              	    ina=xtxt1.find("jc ")
              	if ina<0:
              	    ina=xtxt1.find("jb ")
              	if ina>-1:
              	    inaa=xtxt1.find("0x")
              	    if inaa>-1:
              	        txx=xtxt1
              	        inaaa=xtxt1.find("0x")
              	        if inaaa<0:
              	            inaaa=len(xtxt1)
              	        txx=txx[inaa:]
              	        txx=txx.strip()
              	        txx=txx.replace("<","")
              	        txx=txx.replace(">","")
              	        lst1=lst1+[txx]             	
              	if len(xtxt)>1:
              	    f2.write("        ")
              	    for nnn in xtxt:
              	        if n1>1:
              	            inss2=nnn.find(" <")
              	            if inss2>-1:
              	                inss3=nnn.find("   ")
              	                nnn=nnn[:inss3]+nnn[inss2:]
              	                nnn=nnn.replace("<","")
              	                nnn=nnn.replace(">","")
              	            f2.write(nnn+" ")		
              	        n1+=1
              	    f2.write("\n")
     f2.close()
     scommand("echo  ------------------------------ > /tmp/outs.txt ")       	
     for mmm in lst1:
         print(mmm)
         scommand("objdump -M intel -D -b binary --start-address=$1 -mi386 -Maddr32,data32 /tmp/out.bin >> /tmp/outs.txt".replace("$1",mmm))
     
	
def sline(argvs1,argvs2):
     lst1=[]
     scommand('objdump  -M intel -d -S --disassemble=$2 "$1" > /tmp/out.txt'.replace("$1",argvs1).replace("$2",argvs2))
     f1=open("/tmp/out.txt","r")
     txt=f1.read()
     f1.close()
     txt=txt.replace("\r","\n")
     txt=txt.replace("\n\n","\n")
     
     txtx=txt.split("\n")
     txt=None
     inss1=None
     inss2=None
     inss3=None
     inss=None
     ina=None
     inaa=None
     inaaa=None
     txx=""
     xtxt1=""
     f1=open("/tmp/out.asm","w")
     f1.write("[bits 32]\n")
     for n in txtx:
         inss=n.find(">:")
         if inss>-1:
             n=n.replace(">","")
             inss1=n.find("<")
             if inss1>-1:
                 inss1+=1
                 n=n[inss1:]
                 f1.write("\n")
                 f1.write(n+"\n")
         else:
             inss1=n.find(":")
             
             if inss1>-1:
              	inss1+=1
              	n=n[inss1:]
              	
                
              	xtxt=n.split("	")
              	if len(xtxt)>2:
              	    xtxt1=xtxt[2]
              	

              	n1=0     
              	if len(xtxt)>1:
              	    txtxx=xtxt[1].split(" ")
              	    if xtxt[1].find("e8 fc ff ff ff")>-1:
              	        txtxx=txtxx[1:]
              	    counts=0
              	    for tx in txtxx:
              	        if counts==0:
              	           if tx!="":
              	               f1.write("db 0x")
              	        else:
              	           if tx!="":           	        
              	               f1.write(",0x")
              	        if tx!="":  
              	            f1.write(tx)
              	        counts+=1
              	    f1.write("\n")
     f1.close()            	    
     scommand("nasm -f bin /tmp/out.asm -o /tmp/out.bin")
     scommand("objdump -M intel -D -b binary -mi386 -Maddr32,data32 /tmp/out.bin> out.txt")        	   
     slines1("")
     f1=open("/tmp/out.asm","r")
     readss=f1.read()
     f1.close()
     prints(readss)
     f1=open("/tmp/outs.txt","r")
     readss=f1.read()
     f1.close()
     prints(readss)

class BareboneBuilder:
    def __init__(self, root):
        global sself
        sself=self
        i:int=0
        self.root = root
        self.root.title("editor")

        
        
        self.menubar = tk.Menu(self.root)
        self.mainmenu = tk.Menu(self.menubar, tearoff=0)
        
        # Área de texto
        self.text_1 = tk.Text(self.root, height=1, width=80,bg='yellow')
        self.text_1.pack(pady=10)
        self.text_2 = tk.Text(self.root, height=1, width=80,bg='yellow')
        self.text_2.pack(pady=10)

        self.text_area = tk.Text(self.root, height=25, width=80,bg='yellow')
        self.text_area.pack(pady=10)

        # Botões
        self.b1=self.mainmenu.add_command( label="new file", command=self.build_kernel)
        

        self.b2=self.mainmenu.add_command( label="load file", command=self.run_kernel)
        

        self.b3=self.mainmenu.add_command( label="save file", command=self.copy_file)
        self.b12=self.mainmenu.add_command( label="replace", command=self.replaces)
        self.b6=self.mainmenu.add_command( label="exit", command=self.root.quit)
        self.b5=self.menubar.add_cascade(label="main", menu=self.mainmenu)
        
        self.b4=self.root.configure(menu=self.menubar,bg='yellow')
        self.text_1.insert(tk.END,"/lib/i386-linux-gnu/libc.a" )
        self.text_2.insert(tk.END,"_IO_fgets" )

    def build_kernel(self):
        
        self.text_area.delete(1.0, tk.END)
    def replaces(self):
        txts=self.text_area.get("1.0", "end-1c")
        txts=txts.replace(self.text_1.get("1.0", "end-1c"),self.text_2.get("1.0", "end-1c"))
        self.text_area.delete(1.0, tk.END)
        sline(self.text_1.get("1.0", "end-1c"),self.text_2.get("1.0", "end-1c"))
        
        
       
    def run_kernel(self):
        filename = tk.filedialog.askopenfilename(title="load file")
        self.text_area.delete(1.0, tk.END)
        self.text_1.delete(1.0, tk.END)
        self.text_1.insert(tk.END,filename )
        sline(self.text_1.get("1.0", "end-1c"),self.text_2.get("1.0", "end-1c"))



    def copy_file(self):
        
        heads=self.text_area.get("1.0", "end-1c")
        filename = tk.filedialog.asksaveasfilename(title="save file")
        f2=open(filename,"w")
        f2.write(heads)
        f2.close()



if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    
    root.mainloop()
