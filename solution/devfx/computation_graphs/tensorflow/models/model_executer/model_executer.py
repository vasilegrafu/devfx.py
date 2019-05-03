import tensorflow as tf
import devfx.exceptions as exps
import devfx.reflection as refl

class ModelExecuter(object):
    def __init__(self, path=None):
        self.__graph = tf.Graph()

        self.__session = tf.Session(graph=self.__graph)

        if(path is not None):
            self.import_from(path=path)

    def close(self):
        self.__session.close()
        self.__session = None

        self.__graph = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    """------------------------------------------------------------------------------------------------
    """
    @property
    def graph(self):
        return self.__graph

    @property
    def session(self):
        return self.__session

    """------------------------------------------------------------------------------------------------
    """
    def import_meta_data_from(self, path):
        with self.__graph.as_default():
            tf.train.import_meta_graph(meta_graph_or_file=path+'.graph')

    #
    def import_variables_data_from(self, path):
        with self.__graph.as_default():
            tf.train.Saver(max_to_keep=1).restore(sess=self.__session, save_path=path+'.variables')

    #
    def import_from(self, path):
        self.import_meta_data_from(path=path)
        self.import_variables_data_from(path=path)

    """------------------------------------------------------------------------------------------------
    """
    def evaluate(self, fetch_names, feed_dict=None):
        def complete_name(name):
            return name if (':' in name) else name+':0'

        if(refl.is_typeof_str(fetch_names)):
            fetches = self.__graph.get_tensor_by_name(complete_name(fetch_names))
        elif(refl.is_typeof_list(fetch_names)):
            fetches = [self.__graph.get_tensor_by_name(complete_name(fetch_name)) for fetch_name in fetch_names]
        elif (refl.is_typeof_tuple(fetch_names)):
            fetches = [self.__graph.get_tensor_by_name(complete_name(fetch_name)) for fetch_name in fetch_names]
        else:
            raise exps.NotSupportedError()

        if(feed_dict is not None):
            feed_dict = {self.__graph.get_tensor_by_name(complete_name(feed_name)): feed_data for feed_name, feed_data in feed_dict.items()}

        return self.__session.run(fetches, feed_dict=feed_dict)

