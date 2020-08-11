import tkinter;
import euler;
import cexprtk;

class win:
    title="Solver of ODE of order 1 using method of Euler"
    def __init__(self, parent):
        
        frm_root=tkinter.Frame(parent);
        frm_root.grid();
        
        self.h_var=tkinter.StringVar();
        lbl_h=tkinter.Label(frm_root, text="h=");
        lbl_h.grid(row=0, column=0);
        in_h=tkinter.Entry(frm_root, textvariable=self.h_var);
        in_h.grid(row=0, column=1);
        
        self.x0_var=tkinter.StringVar();
        lbl_x0=tkinter.Label(frm_root, text="x0=");
        lbl_x0.grid(row=1, column=0);
        in_x0=tkinter.Entry(frm_root, textvariable=self.x0_var);
        in_x0.grid(row=1, column=1);
        
        self.y0_var=tkinter.StringVar();
        lbl_y0=tkinter.Label(frm_root, text="y0=");
        lbl_y0.grid(row=2, column=0);
        in_y0=tkinter.Entry(frm_root, textvariable=self.y0_var);
        in_y0.grid(row=2, column=1);
        
        self.x_var=tkinter.StringVar();
        lbl_x=tkinter.Label(frm_root, text="x=");
        lbl_x.grid(row=3, column=0);
        in_x=tkinter.Entry(frm_root, textvariable=self.x_var);
        in_x.grid(row=3, column=1);
        
        self.f_var=tkinter.StringVar();
        lbl_f=tkinter.Label(frm_root, text="f(x, y)=");
        lbl_f.grid(row=4, column=0);
        in_f=tkinter.Entry(frm_root, textvariable=self.f_var);
        in_f.grid(row=4, column=1);
        
        self.y_var=tkinter.StringVar();
        lbl_y=tkinter.Label(frm_root, text="y=");
        lbl_y.grid(row=5, column=0);
        in_y=tkinter.Entry(frm_root, textvariable=self.y_var);
        in_y.grid(row=5, column=1);
        
        btn_calc=tkinter.Button(frm_root, text="Calculate");
        btn_calc["command"]=self.calc;
        btn_calc.grid(row=6, column=0);
        
        btn_reset=tkinter.Button(frm_root, text="Reset");
        btn_reset["command"]=self.reset;
        btn_reset.grid(row=6, column=1);
    
    def calc(self):
        h=float(self.h_var.get());
        x0=float(self.x0_var.get());
        y0=float(self.y0_var.get());
        x=float(self.x_var.get());
        f=str(self.f_var.get());
                
        y=euler.euler_solver_2(f, h, x0, y0, x);
        self.y_var.set(y);
        
    def reset(self):
        self.h_var.set("");
        self.x0_var.set("");
        self.y0_var.set("");
        self.x_var.set("");
        self.f_var.set("");
        self.y_var.set("");

def main()->int:
    return 0;
    
if(__name__=="__main__"):
    if(main()==0):
        print("Program terminated successfuly.");