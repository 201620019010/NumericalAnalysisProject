export const parameters =[
    
    {
        "Index":0,
        "key":"incrementalSearch",
        "parameters":{
            "f":"function",
            "x0":"number",
            "deltaX":"number",
            "n":"number"
        },
        "Helps":[
            "Input Example-------------------",
            "f=math.log((math.sin(x)**2)+1)-(1/2)",
            "x0=-3",
            "delta=0.5",
            "n=100",
            "--------------------------------",
            "In order for this method to be applied f(X) function must be real and continued",
            "When picking deltax remeber to be really careful, if delta is too big the method wont find a root, and if its too short the emthod will become slow",
            "remember that x0 must exist in the function , try using the grapher to verify that x0 exists"
        ]
    },
    {
        "Index":1,
        "key":"bisection",
        "parameters":{
            "f":"function",
            "a":"number",
            "b":"number",
            "tol":"number",
            "n":"number"
        },
        "Helps":[
            "Input Example-------------------",
            "f=math.log((math.sin(x)**2)+1)-(1/2)",
            "a=-3",
            "b=0.5",
            "n=100",
            "tol=1e-7",
            "--------------------------------",
            "Remember that both a and b must exist in the function",
            "If there is more than one root  in the intevral [A,B] this method will give us an aproximation to the first root that it finds"
        ]
    },
    {
        "Index":2,
        "key":"falsePosition",
        "parameters":{
            "f":"function",
            "a":"number",
            "b":"number",
            "tol":"number",
            "n":"number"
        },
        "Helps":[
            "Input Example-------------------",
            "f=math.log((math.sin(x)**2)+1)-(1/2)",
            "a=-3",
            "b=0.5",
            "n=100",
            "tol=1e-7",
            "--------------------------------",
            "Remember that both a and b must exist in the function",
            "If there is more than one root  in the intevral [A,B] this method will give us an aproximation to the first root that it finds"
        ]
    },
    {
        "Index":3,
        "key":"newton",
        "parameters":{
            "f":"function",
            "f1":"function",
            "x0":"number",
            "tol":"number",
            "n":"number"
        },
        "Helps":[
            "Input Example-------------------",
            "f=math.log((math.sin(x)**2)+1)-(1/2)",
            "f1=2*(((math.sin(x)**2)+1)**-1)*math.sin(x)*math.cos(x)",
            "x0=0.5",
            "n=100",
            "tol=1e-7",
            "--------------------------------",
            "Both f(x0) and f1(x0) must exist , try using the grapher to verify that it exists"
        ]
    },
    {
        "Index":4,
        "key":"staticPoint",
        "parameters":{
            "f1":"function",
            "g":"function",
            "x0":"number",
            "tol":"number",
            "n":"number"
        },
        "Helps":[
            "Input Example-------------------",
            "f=math.log((math.sin(x)**2))+1-x",
            "g=math.log((math.sin(x)**2)+1)-(1/2)",
            "x0=0.5",
            "n=100",
            "tol=1e-7",
            "--------------------------------",
            "This method from a f(x)=0 equation generates a X=g(x) equation that searches for the solution ",
            "You must be really careful when picking X=g(x) because depending on this the method will be faster or slower",
            "f(x0) and g(x0) must exist , use the grapher to verify their existance"
        ]
    },
    {
        "Index":5,
        "key":"secant",
        "parameters":{
            "f":"function",
            "x0":"number",
            "x1":"number",
            "tol":"number",
            "n":"number"
        },
        "Helps":[
            "Input Example-------------------",
            "f=math.log((math.sin(x)**2)+1)-(1/2)",
            "x0=0",
            "x1=1",
            "n=100",
            "tol=1e-7",
            "--------------------------------",
            "Both f(x1) and g(x1) must exist , try using the grapher to verify that it exists"
        ]
    },
    {
        "Index":6,
        "key":"multipleRoots",
        "parameters":{
            "h":"function",
            "dh1":"function",
            "dh2":"function",
            "x0":"number",
            "tol":"number",
            "n":"number"
        },
        "Help":[
            "Input Example-------------------",
            "h=(math.e**x)-x-1",
            "dh1=(math.e**x)-1",
            "dh2=(math.e**x)",
            "x0=1",
            "tol=1e-7",
            "n=100",
            "--------------------------------",
            "One of the conditions to make sure this method convergers is that f'(x) must be different from 0",
            "When running the method if f´(xn) closes on 0 ,the method begins to slow  and there is a possible multiple root ",
            
        ]
    },
    {
        "Index":7,
        "key":"gaussianElimination",
        "parameters":{
            "A":"matrix",
            "b":"matrix"
        },
        "Helps":[
            "Input Example-------------------",
            "a=[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]",
            "b=[1],[1],[1],[1]",
            "--------------------------------",
            "Remember if there is a zero in the diagonal the method will fail",
            "Rember tha A and b must have the same number of rows",
            "The determinant of the matrix cant be zero"
        ]
    },

    {
        "Index":8,
        "key":"totalPivoting",
        "parameters":{
            "A":"matrix",
            "b":"matrix"
        },
        "Helps":[
            "Input Example-------------------",
            "a=[[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]]",
            "b=[1,1,1,1]",
            "--------------------------------",
            "Remember if there is a zero in the submatrix diagonal the method will fail",
            "Rember tha A and b must have the same number of rows"
        ]
    },
    {
        "Index":9,
        "key":"parcialPivoting",
        "parameters":{
            "A":"matrix",
            "b":"matrix"
        },
        "Helps":[
            "Input Example-------------------",
            "a=[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]",
            "b=[1],[1],[1],[1]",
            "--------------------------------",
            "Remember if there is a zero in the subamatrix diagonal the method will fail",
            "Rember tha A and b must have the same number of rows"
        ]
    },
    {
        "Index":10,
        "key":"LUsimple",
        "parameters":{
            "A":"matrix",
            "b":"matrix"
        },
        "Helps":[
            "Input Example-------------------",
            "a=[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]",
            "b=[1],[1],[1],[1]",
            "--------------------------------",
            "Remember if there is a zero in the diagonal the method will fail",
            "Rember tha A and b must have the same number of rows",
        ]
    },
    {
        "Index":11,
        "key":"LUparcial",
        "parameters":{
            "A":"matrix",
            "b":"matrix"
        },
        "Helps":[
            "Input Example-------------------",
            "a=[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]",
            "b=[1],[1],[1],[1]",
            "--------------------------------",
            "Remember if there is a zero in the diagonal the method will fail",
            "Rember tha A and b must have the same number of rows",
        ]
    },
    {
        "Index":12,
        "key":"crout",
        "parameters":{
            "A":"matrix",
            "b":"matrix"
        },
        "Helps":[
            "Input Example-------------------",
            "a=[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]",
            "b=[1],[1],[1],[1]",
            "--------------------------------",
            "Remember if there is a zero in the diagonal of L or U the method will fail",
            "Rember tha A and b must have the same number of rows",
            "This Method is finite, it will apply a formula to find the anwer"
        ]
    },
    {
        "Index":13,
        "key":"doolittle",
        "parameters":{
            "A":"matrix",
            "b":"matrix"
        },
        "Helps":[
            "Input Example-------------------",
            "a=[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]",
            "b=[1],[1],[1],[1]",
            "--------------------------------",
            "Remember if there is a zero in the diagonal of L or U the method will fail",
            "Rember tha A and b must have the same number of rows",
            "This Method is finite, it will apply a formula to find the anwer"
        ]
    },
    
    {
        "Index":14,
        "key":"cholesky",
        "parameters":{
            "A":"matrix",
            "b":"matrix"
        },
        "Helps":[
            "Input Example-------------------",
            "a=[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]",
            "b=[1],[1],[1],[1]",
            "--------------------------------",
            "Remember if there is a zero in the diagonal of L or U the method will fail",
            "Rember tha A and b must have the same number of rows",
            "This Method is finite, it will apply a formula to find the anwer",
            "Method will not work if it has to find the square root of a negative number"
        ]
    },

    {
        "Index":15,
        "key":"jacobi",
        "parameters":{
            "A":"matrix",
            "b":"matrix",
            "x0":"number",
            "tol":"number",
            "n":"number"
        },
        "Helps":[
            "Input Example-------------------",
            "a=[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]",
            "b=[1,1,1,1]",
            "x0=[0,0,0,0]",
            "tol=1e-7",
            "n=100",
            "--------------------------------",
            "A must be invertible therefore elements in the diagonal cant be zero",
            "Rember tha A and b must have the same number of rows",
            "If the Spectral radius of T is <1 the method converges",
            "A diagonally dominant matrix means that for each row ,the sum of the elements beside the diagonal must be less than the diagonal",
            "If  A is strictly diagonally dominant de method converges",
            
        ]
    },
    {
        "Index":16,
        "key":"gauss-seidel",
        "parameters":{
            "A":"matrix",
            "b":"matrix",
            "x0":"number",
            "tol":"number",
            "n":"number"
        },
        "Helps":[
            "Input Example-------------------",
            "a=[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]",
            "b=[1,1,1,1]",
            "x0=[0,0,0,0]",
            "tol=1e-7",
            "n=100",
            "--------------------------------",
            "Remember if there is a zero in the diagonal the method will fail",
            "Rember tha A and b must have the same number of rows",
            "If the Spectral radius of T is <1 the method converges",
            "A diagonally dominant matrix means that for each row ,the sum of the elements beside the diagonal must be less than the diagonal",
            "If  A is strictly diagonally dominant de method converges",
            
        ]
    },
    {
        "Index":17,
        "key":"sor",
        "parameters":{
            "A":"matrix",
            "b":"matrix",
            "x0":"number",
            "w":"number",
            "tol":"number",
            "n":"number"
        },
        "Helps":[
            "Input Example-------------------",
            "a=[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]",
            "b=[1,1,1,1]",
            "x0=[0,0,0,0]",
            "w=0.5",
            "tol=1e-7",
            "n=100",
            "--------------------------------",
            "Remember if there is a zero in the diagonal the method will fail",
            "Rember tha A and b must have the same number of rows",
            "If the Spectral radius of T is <1 the method converges",
            "A diagonally dominant matrix means that for each row ,the sum of the elements beside the diagonal must be less than the diagonal",
            "If  A is strictly diagonally dominant de method converges",
            "W must between 0 and 2  if w=1 gauss seidel , if 0<w<1 then the sub-relaxation method is used,if 1<w<2 then over-relaxation method is used",
            "The spectral radius must be less than 1 for the method to work"
        ]
    },

    {
        "Index":18,
        "key":"vandermonde",
        "parameters":{
            "x":"table",
            "y":"table",
        },
        "Helps":[
            "Input Example-------------------",
            "x=[0.5,1,3,5]",
            "y= [-5.04],[-1.47],[-1.69],[10.89]",
            "--------------------------------",
            "Remember that you need to input the same number of x and y elements",
            "This method uses gaussian elimination to find the polinome,",
            "This is the worst of the interpolating methods , it is the most inexact , but it is fast and easy"
        ]
    },

    {
        "Index":19,
        "key":"newtonInterpolation",
        "parameters":{
            "x":"table",
            "y":"table",
        },
        "Helps":[
            "Input Example-------------------",
            "x=[-1,0,3,4]",
            "y=[15.5,3,8,1]",
            "--------------------------------",
            "Remember that you need to input the same number of x and y elements",
            "This method uses the differences table"

        ]
    },
    {
        "Index":20,
        "key":"lagrange",
        "parameters":{
            "x":"table",
            "y":"table",
        },
        "Helps":[
            "Input Example-------------------",
            "x=[-1,0,3,4]",
            "y=[15.5,3,8,1]",
            "--------------------------------",
            "Remember that you need to input the same number of x and y elements",
        ]
    },
    {
        "Index":21,
        "key":"spline1",
        "parameters":{
            "x":"table",
            "y":"table",
        },
        "Helps":[
            "Input Example-------------------",
            "x=[-1,0,3,4]",
            "y=[15.5,3,8,1]",
            "--------------------------------",
            "Remember that you need to input the same number of x and y elements",
            "this method gives a lineal interpolating polinome"
        ]
        
    },
    {
        "Index":22,
        "key":"spline2",
        "parameters":{
            "x":"table",
            "y":"table",
        },
        "Helps":[
            "Input Example-------------------",
            "x=[-1,0,3,4]",
            "y=[15.5,3,8,1]",
            "--------------------------------",
            "Remember that you need to input the same number of x and y elements",
            "This method gives out a cuadratic polinome"
        ]
    },
    {
        "Index":23,
        "key":"spline3",
        "parameters":{
            "x":"table",
            "y":"table",
        },
        "Helps":[
            "Input Example-------------------",
            "x=[-1,0,3,4]",
            "y=[15.5,3,8,1]",
            "--------------------------------",
            "Remember that you need to input the same number of x and y elements",
            "This method gives out a cubic interpolating polinome"
        ]
    },

    {
        "Index":24,
        "key":"Grapher",
        "parameters":{
            "f":"function",
            "a":"lower interval",
            "b":"upper interval"
        },
        "Helps":[
            "Input Example-------------------",
            "f=math.log((math.sin(x)**2)+1)-(1/2)",
            "a=-3",
            "b=0.5",
            "--------------------------------",
        ]

    },
    {
        "Index":25,
        "key":"functionEvaluator",
        "parameters":{
            "f":"function",
            "a":"lower interval",
            "b":"upper interval"
        },
        "Helps":[
            "Input Example-------------------",
            "f=math.log((math.sin(x)**2)+1)-(1/2)",
            "a=-3",
            "b=0.5",
            "--------------------------------",
        ]


    },


    
  
    
        
    
]