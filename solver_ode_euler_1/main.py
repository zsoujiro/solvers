import tkinter;
import gui_root;

def main()->int:
    root=tkinter.Tk();
    root.title(gui_root.win.title);
    root.geometry("640x480");
    win_root=gui_root.win(root);
    
    root.mainloop();
    return 0;
    
if(__name__=="__main__"):
    if(main()==0):
        print("Program terminated successfuly.");