import numpy as np
import devfx.math as math
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""
def test():
    theta_head = math.linspace(0.0, 1.0, 512)

    p_theta_head_func = lambda n: (theta_head**n)*((1-theta_head)**n)
    p_x_theta_head_func = lambda heads: (theta_head**math.sum(heads))*((1-theta_head)**(heads.size-math.sum(heads)))
    p_theta_head_x_func = lambda n, heads: p_x_theta_head_func(heads)*p_theta_head_func(n)


    figure = dv.Figure(size=(12, 6), grid=(3,4))

    def build_chart(p_theta_head_func, n, heads, chart_column):
        heads = np.asarray(heads)

        chart = dv.Chart2d(figure=figure, position=figure[0, chart_column])
        chart.plot(theta_head, p_theta_head_func(n))

        chart = dv.Chart2d(figure=figure, position=figure[1, chart_column])
        chart.plot(theta_head, p_x_theta_head_func(heads))

        chart = dv.Chart2d(figure=figure, position=figure[2, chart_column])
        chart.plot(theta_head, p_theta_head_x_func(n, heads))

    heads = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    build_chart(p_theta_head_func=p_theta_head_func, n=1, heads=heads, chart_column=0)
    build_chart(p_theta_head_func=p_theta_head_func, n=2, heads=heads, chart_column=1)
    build_chart(p_theta_head_func=p_theta_head_func, n=4, heads=heads, chart_column=2)
    build_chart(p_theta_head_func=p_theta_head_func, n=8, heads=heads, chart_column=3)

    figure.show()


"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    test()