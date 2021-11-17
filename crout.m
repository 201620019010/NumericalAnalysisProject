%Este programa halla la soluci�n al sistema Ax=b y la factorizaci�n LU de A
%usando el m�todo de Crout

%Entradas: 
%A, matrix invertible
%b, vector constante

%Salidas
%x, soluci�n
%L, matriz L de la factorizaci�n
%U, matriz U de la factorizaci�n

%Creado por: Samir Posada
%�ltima actualizaci�n: 16/07/2020

function [x,L,U]=C13_Crout(A,b)

%Inicializaci�n
n=size(A,1);
L=eye(n); 
U=eye(n);

result=[]
result=append(["STAGE 0----------------------------"])
result=append(A))
%Factorizaci�n
for i=1:n-1
    disp(['Stage: ',num2str(i),'--------------------'])
    for j=i:n
        L(j,i)=A(j,i)-dot(L(j,1:i-1),U(1:i-1,i)');
        
    end
    disp(L)
    for j=i+1:n
        U(i,j)=(A(i,j)-dot(L(i,1:i-1),U(1:i-1,j)'))/L(i,i);
    end

    disp(U)
end
L(n,n)=A(n,n)-dot(L(n,1:n-1),U(1:n-1,n)');

%Entrega de resultados
z=sustprgr([L b]);
x=sustregr([U z]); 
result=result       
end