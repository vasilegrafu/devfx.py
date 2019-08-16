import devfx.mathematics as math
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
def test():
    figure = dv.Figure()
    chart = dv.Chart2d(figure=figure, ylim=(-2, 2))

    def plot_chart(i, delta):
        x_offset = i*0.1
        
        x_interval = (x_offset, x_offset + delta)
        x = math.range(*x_interval, 0.1)
        f = math.sin(x)
        chart.set_xlim(x_interval)
        chart.plot(x, f, 'r')
        
    figure.animation_fn(fn=plot_chart, fn_args=(32,))

    figure.show()


"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    test()

