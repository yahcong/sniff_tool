#!/usr/bin/env python2

def writerequest(servername,method,src_ip,dst_ip,src_port,dst_port,path,body,headers):
    filename = servername+'.txt'
    with open(filename,"a") as f:
        f.write('************receive request *************\n')
        f.write('method: '+str(method)+'\n')
        f.write('src_ip: '+str(src_ip)+'\n')
        f.write('dst_ip: '+str(dst_ip)+'\n')
        f.write('src_port: '+str(src_port)+'\n')
        f.write('dst_port: '+str(dst_port)+'\n')
        f.write('path: '+str(path)+'\n')
        f.write('body:\n'+str(body)+'\n')
        f.write('headers:\n'+str(headers)+'\n')
        f.write('*****************end***************\n')

def writeresponsn(servername,src_ip,dst_ip,src_port,dst_port,headers,responsedata):
    filename = servername+'.txt'
    with open(filename,"a") as f:
        f.write('************response data ************\n')
        f.write('src_ip: '+str(src_ip)+'\n')
        f.write('dst_ip: '+str(dst_ip)+'\n')
        f.write('src_port: '+str(src_port)+'\n')
        f.write('dst_port: '+str(dst_port)+'\n')
        f.write('headers:\n'+str(headers)+'\n')
        f.write('response data:\n'+str(responsedata)+'\n')
        f.write('*****************end***************\n')
