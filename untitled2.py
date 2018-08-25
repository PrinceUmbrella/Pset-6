## -*- coding: utf-8 -*-
#"""
#Created on Tue Aug 14 12:36:10 2018
#
#@author: eleou
#"""
#
#import string
#def shiftFunc(shift):
#    alpha = string.ascii_lowercase
#    alpha_List = []
#    cap_alpha = []
#    for i in alpha:
#        alpha_List.append(i)
#        cap_alpha.append(i.upper())   
#    
#    
#    def Encryptt(listt, shift):
#        cut_list = listt[-(26-shift):] 
#        new_list = listt[:-(26-shift)]
#        combList = cut_list + new_list
#        return(combList)
#    
#    
#    beta_list = Encryptt(alpha_List,shift)  
#    delta_list = Encryptt(cap_alpha,shift)
#    #print(beta_list)
#    #print(delta_list)
#    #print(alpha_List)
#    shift_guide = dict(zip(alpha_List,beta_list))
#    shift_guide2 = dict(zip(cap_alpha,delta_list))
#    shift_guide.update(shift_guide2)
#    return(shift_guide)
#    
#    
#def applyFunc(shift = 1, message = "Hello, Hi"):
#    guide = shiftFunc(shift)
#    chiper_message = []
#    #add test case or error handling
#    for i in message:
#        if i in string.ascii_lowercase:
#            chiper_message.append(guide[i])
#        elif i in string.ascii_uppercase:
#            chiper_message.append(guide[i.lower()].upper())
#            
#        else:
#            chiper_message.append(i)
#            
#    encrypt_message = ''.join(chiper_message)
#    
#        
#    print(encrypt_message)
#  
##print(shiftFunc(24))
##shiftFunc(24)
#applyFunc(24,"we are taking 6.00.1x")
import ps6


