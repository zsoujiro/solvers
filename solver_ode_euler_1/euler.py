import math;
import cexprtk;

def euler_next(func, h: float, x0: float, y0: float)->float:
    retval=y0+h*func(x0, y0);
    return retval;

def euler_solver(func, h: float, x0: float, y0: float, x: float)->float:
    deltax=x-x0;
    n=int(deltax/h);
    retval=0;
    x=x0;
    y=y0;
    for i in range(n):
        retval=euler_next(func, h, x, y);
        y=retval;
        x=x+h;
    return retval;
    
def euler_solver_2(text: str, h: float, x0: float, y0: float, x: float)->float:
    deltax=x-x0;
    n=int(deltax/h);
    retval=0;
    st=cexprtk.Symbol_Table({"x": x0, "y": y0}, add_constants=True);
    expression=cexprtk.Expression(text, st);
    for i in range(n):
        retval=st.variables["y"]+h*expression();
        st.variables["y"]=retval;
        st.variables["x"]=st.variables["x"]+h;
    return retval;

def f(x: float, y: float):
    return x+y;

def main()->int:
    print("Welcome to the solver of ODE by Euler method.");
    h=float(input("h="));
    x_0=float(input("x_0="));
    y_0=float(input("y_0="));
    text=input("f(x, y)=");
    x=float(input("x="));
    y=euler_solver(f, h, x_0, y_0, x);
    print("y=", y);
    y=euler_solver_2(text, h, x_0, y_0, x);
    print("Using cexprtk y=", y);
    return 0;
    
if(__name__=="__main__"):
    if(main()==0):
        print("Program terminated successfuly.");