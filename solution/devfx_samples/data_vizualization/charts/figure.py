import numpy as np
import devfx.math as math
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""     
def test():
    x = math.range(0.0, 8.0, 0.01)
    f1 = x**(0.5)
    f1_label='f(x)=x**(0.5)'
    f2_label='f(x)=x**(2.00)'
    f2 = x**(2.00)
     
    #          
    figure1 = dv.Figure()
    
    chart11 = dv.Chart2d(figure1, position=(2, 1, 1), ylim=(0, 4))
    [chart11_line1] = chart11.plot(x, f1, label=f1_label)
    [chart11_line2] = chart11.plot(x, f2, label=f2_label)
    chart11.set_legend(loc=(0.65, 0.0))
    
    chart12 = dv.Chart2d(figure1, position=(2, 1, 2), ylim=(0, 4))
    [chart12_line1] = chart12.plot(x, f1, label=f1_label)
    [chart12_line2] = chart12.plot(x, f2, label=f2_label)
    chart12.set_legend(loc=(0.65, 0.0))

    figure1.show()

    #
    figure2 = dv.Figure()
    
    chart21 = dv.Chart2d(figure2, position=((2, 1), (0, 0), (1, 1)), ylim=(0, 4))
    [chart21_line1] = chart21.plot(x, f1, label=f1_label)
    [chart21_line2] = chart21.plot(x, f2, label=f2_label)
    chart21.set_legend(loc=(0.65, 0.0))
    
    chart22 = dv.Chart2d(figure2, position=((2, 1), (1, 0), (1, 1)), ylim=(0, 4))
    [chart22_line1] = chart22.plot(x, f1, label=f1_label)
    [chart22_line2] = chart22.plot(x, f2, label=f2_label)
    chart22.set_legend(loc=(0.65, 0.0))

    figure2.show()


"""------------------------------------------------------------------------------------------------
"""     
if __name__ == '__main__':
    test()

