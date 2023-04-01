%Frida Rangel
%A01651385
%Comprobación por Matlab de solución de sistema de ecuaciones:
clear all
close all
clc


A =[0.25 0.15 0.00;0.45 0.50 0.75;0.30 0.35 0.25];
B = [1.5;5;3];

X = A\B 