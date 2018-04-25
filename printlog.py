#!/usr/bin/env python2

def printrequest(servername,method,src_ip,dst_ip,src_port,dst_port,path,body,headers):
    print '***********receive request *****************'
    print 'server:'+str(servername)
    print 'method: '+str(method)
    print 'src_ip: '+str(src_ip)
    print 'dst_ip: '+str(dst_ip)
    print 'src_port: '+str(src_port)
    print 'dst_port: '+str(dst_port)
    print 'path: '+str(path)
    print 'body:\n'+str(body)
    print 'headers:\n'+str(headers)
    print '***********end*******************************'

def printresponsn(servername,src_ip,dst_ip,src_port,dst_port,headers,responsedata):
    print '***********response data*****************'
    print 'server:'+str(servername)
    print 'src_ip: '+str(src_ip)
    print 'dst_ip: '+str(dst_ip)
    print 'src_port: '+str(src_port)
    print 'dst_port: '+str(dst_port)
    print 'headers:\n'+str(headers)
    print 'response data:\n'+str(responsedata)
    print '***********end*******************************'

