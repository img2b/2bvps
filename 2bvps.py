#! /usr/bin/env python
#coding=utf-8
import sys
import ConfigParser 
 
conf = ConfigParser.ConfigParser()  
if(conf.read("2bvps.cfg")==0):
    print 'config file is missing'
    sys.exit()  
#定义服务类
class service:  
    name = ''  
    script=[]
    depends=[]
    #定义私有属性,私有属性在类外部无法直接进行访问  
    __weight = 0  
    #定义构造方法  
    def __init__(self,sections):  
        self.name = sections
        self.script= conf.get(sections,'script')
        self.depends=conf.get(sections,'depends')
        
         
    def speak(self):  
        print("service:%s"%(self.name))  
        print("script:%s"%(self.script)) 
        print("depends:%s"%(self.depends)) 

  
#serv = service('vpn')  
#serv.speak()
#脚本入口
conf = ConfigParser.ConfigParser()  
if(conf.read("2bvps.cfg")==0):
    print 'config file is missing'
    sys.exit()  

if len(sys.argv) < 2:  
    print 'No action specified.'  
    sys.exit()  
  
if sys.argv[1].startswith('-') and sys.argv[2]:  
    option = sys.argv[1][1:]  
    # 取 sys.argv[1] but without the first two characters，这里去掉“--”  
    if option == 'i' or option =='install':
        print 'install:'+sys.argv[2]
        serv = service(sys.argv[2])
        serv.speak()

    elif option == 'help':  
        print '''''\ 
This program prints files to the standard output. 
Any number of files can be specified. 
Options include: 
  --version : Prints the version number 
  --help    : Display this help'''  
    else:  
        print 'Unknown option.'  
    sys.exit()  
else:  
    for filename in sys.argv[1:]:  
        sys.exit()  