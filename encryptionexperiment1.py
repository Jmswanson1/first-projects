#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 11:27:09 2019

@author: joshuaswanson
"""

abcsnm ={'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13,
         'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25, '~':26,
         ',':27,'.':28,'?':29,'!':30,"'":31,'(':32,')':33,'#':34,';':35, ':':36, '[':37, ']':38, '&':39, '+':40,
         '-':41, '@':42, '$':43, '%':44, '^':45, '*':46, '_':47, '"':48, '{':49, '}':50, '<':51, '>':52, r'/':53,
         '=':54, '\n':55, '0':56, '1':57, '2':58, '3':59, '4':60,'5':61, '6':62, '7':63, '8':64, '9':65}



def get_key(val): 
    for key, value in abcsnm.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"


def f(message):

    message = message.replace(' ', '~').lower()
    messagelist = list(message)
    step1 = [abcsnm[k] for k in messagelist]
    temp1 = list(range(0,len(messagelist)))
    step2 = [[step1[k],k+1] for k in temp1]
    temp2 = [[(step2[k][0]+step2[k][1])%66, step2[k][1]] for k in list(range(0,len(step2)))]
    temp3 = [temp2[k][0] for k in list(range(len(temp2)))]
    temp4 = [get_key(temp3[k]) for k in list(range(len(temp3)))]
    i=1
    result = temp4[0]
    while i != len(temp4):
        result = result + temp4[i]
        i+=1
    realresult = ''.join(result)
    return realresult

def encrypt(message):
    j = len(message)
    i = 1
    temp = f(message)
    while i !=j:
        temp = f(temp)
        i+=1
    return temp



def decrypt(message):
    message = message.replace(' ', '~')
    msl = list(message)
    temp1 = list(range(0,len(msl)))
    j = len(msl)
    
    new = [(abcsnm[msl[k]]-(k+1)*j)%66 for k in temp1]

    result = [get_key(k) for k in new]  
    realresult = ''.join(result).replace('~', ' ')   
    return realresult

def startencrypt():
    
    
    again = True
    while again == True:
        
        message = input('Please enter a message to encrypt ')
        print(encrypt(message))
        
        checksout = False
        
        while checksout == False:
            again = input('Again? (y/n) ' )
            if again == 'y':
                again = True
                checksout = True
                print('Here we go again!')
            if again == 'n':
                again = False
                checksout = True
                print('Then I suppose we are done')
            else:
                print('That was not a valid responce, please try again.')

#cipher = encrypt(message)
#print(cipher)
#print(decrypt(cipher))

def startdec():
    again = True
    while again == True:
        the_message = input('Please enter a message to decrypt ')
        print(decrypt(the_message))
        checksout = False
        while checksout == False:
            again = input('Again? (y/n) ')
            if again == 'y':
                again = True
                checksout = True
                print('Here we go again!')
            elif again == 'n':
                again = False
                checksout = True
                print('Then I suppose we are done here')
            else:
                print('That was not a valid response, please try again.')


def initiate():
    check = False
    while check == False:
        direction = input('Do you want to encrypt or decrypt a message? (encrypt/decrypt) ')
        if direction == 'encrypt':
            check == True
            startencrypt()
            break
        if direction == 'decrypt':
            check == True
            startdec()
            break
        else:
            print('That was not the word encrypt or decrypt, please try again.')
    print('Goodbye')
        
        
    

initiate()