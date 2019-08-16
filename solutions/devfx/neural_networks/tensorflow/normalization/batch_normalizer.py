import devfx.computation_graphs.tensorflow as cg

class BatchNormalizer(object):
    def __init__(self, is_training):
        self.is_training = is_training

    def __call__(self, z):
        is_training = self.is_training

        batch_mean = cg.reduce_mean(z, axis=0)
        batch_var = cg.reduce_var(z, axis=0)

        ema = cg.train.ema(decay=0.99)

        def update_mean_var(ema, batch_mean, batch_var):
            ema_apply_op = ema.apply([batch_mean, batch_var])
            with cg.control_dependencies([ema_apply_op]):
                return (cg.identity(batch_mean), cg.identity(batch_var))

        def get_mean_var(ema, batch_mean, batch_var):
            return (ema.average(batch_mean), ema.average(batch_var))

        mean, var = cg.condition(cg.equal(is_training, True), lambda: update_mean_var(ema, batch_mean, batch_var), lambda: get_mean_var(ema, batch_mean, batch_var))

        z = (z - mean)/cg.sqrt(var + 1e-8)
        gamma = cg.Variable(dtype=cg.float32, initial_value=1.0)
        beta = cg.Variable(dtype=cg.float32, initial_value=0.0)
        z = gamma*z + beta

        return z

batch_normalizer = BatchNormalizer