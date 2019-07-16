import numpy as np
import devfx.data_containers as dc
import devfx.statistics as stats
import devfx.computation_graphs.tensorflow as cg
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
class UnivariateLinearRegressionDataGenerator():
    def __init__(self):
        pass

    def generate(self):
        M = 1024
        a = 1.0
        b = 0.75
        x = np.random.normal(0.0, 0.5, size=M)
        y = a*x + b + np.random.normal(0.0, 0.1, size=M)
        return [x, y]

"""------------------------------------------------------------------------------------------------
"""
class UnivariateLinearRegressionModel(cg.models.DeclarativeModel):
    # ----------------------------------------------------------------
    def _build_model(self):
        pass

    # ----------------------------------------------------------------
    def _on_training_begin(self, context):
        pass

    def _on_training_epoch_begin(self, epoch, context):
        pass

    def _on_append_to_training_log(self, training_log, context):
        pass

    def _on_training_epoch_end(self, epoch, context):
        pass

    def _on_training_end(self, context):
        pass

"""------------------------------------------------------------------------------------------------
"""
def main():
    # generating data
    generated_data = UnivariateLinearRegressionDataGenerator().generate()
    dataset = dc.Dataset(data=generated_data)

    figure = dv.Figure(size=(8, 6))
    chart = dv.Chart2d(figure=figure)
    chart.scatter(dataset[0], dataset[1])
    figure.show()

    # splitting data
    (training_dataset, test_dataset) = dataset.split()
    print(training_dataset, test_dataset)

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()
