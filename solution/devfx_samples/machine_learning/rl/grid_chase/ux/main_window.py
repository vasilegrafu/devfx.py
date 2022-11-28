import itertools
import time
import numpy as np
import devfx.exceptions as ex
import devfx.core as core
import devfx.diagnostics as dgn
import devfx.machine_learning as ml
import devfx.processing.concurrent as pc
import devfx.ux.windows.wx as ux

from ..logic.grid_environment import GridEnvironment
from ..logic.grid_agent_kind import GridAgentKind

class MainWindow(ux.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__init_model()

        self.__init_widgets()
        self.__init_layout()

    """------------------------------------------------------------------------------------------------
    """
    def __init_model(self):
        self.grid_environment_for_training = GridEnvironment(training=True)
        self.grid_environment_for_training.setup()

        self.grid_environment = GridEnvironment()
        self.grid_environment.setup()
        
    """------------------------------------------------------------------------------------------------
    """
    def __init_widgets(self):
        self.grid_canvas = ux.Canvas(self, size=(64, 64))
        self.grid_canvas.OnDraw += self.__grid_canvas__OnDraw

        self.train_button = ux.Button(parent=self, label='Train')
        self.train_button.OnPress += self.__train_button__OnPress
        self.cancel_training_button = ux.Button(parent=self, label='Cancel training')
        self.cancel_training_button.OnPress += self.__cancel_training_button__OnPress
        self.train_count_text = ux.Text(parent=self, label='0', size=(64, -1))
        self.train_batch_time_elapsed_text = ux.Text(parent=self, label='0', size=(64, -1))
        self.training_is_running = False
        
        self.do_iteration_button = ux.Button(parent=self, label='Do iteration')
        self.do_iteration_button.OnPress += self.__do_iteration_button__OnPress
        
        self.do_iterations_speed_label = ux.Text(parent=self, label='Speed:')
        self.do_iterations_speed_spinbox = ux.FloatSpinBox(parent=self, min=0.01, max=1.0, initial=0.10, inc=0.01, size=(64, -1))
        self.do_iterations_button = ux.Button(parent=self, label='Do iterations')
        self.do_iterations_button.OnPress += self.__do_iterations_button__OnPress
        self.cancel_iterations_button = ux.Button(parent=self, label='Cancel iterations')
        self.cancel_iterations_button.OnPress += self.__cancel_iterations_button__OnPress
        self.do_iterations_is_running = False

    def __init_layout(self):
        #
        self.main_sizer = ux.GridBagSizer().AddToWindow(self)
        self.grid_sizer = ux.GridBagSizer().AddToSizer(self.main_sizer, pos=(0, 0), flag=ux.EXPAND)
        self.grid_sizer.AddGrowableCol(0)
        self.grid_sizer.AddGrowableRow(0)
        self.command_sizer = ux.GridBagSizer(hgap=32).AddToSizer(self.main_sizer, pos=(1, 0), flag=ux.ALIGN_CENTER)
        self.main_sizer.AddGrowableCol(0)
        self.main_sizer.AddGrowableRow(0, 1)
        self.main_sizer.AddGrowableRow(1, 0)

        self.training_sizer = ux.BoxSizer(ux.HORIZONTAL).AddToSizer(self.command_sizer, pos=(0, 0), span=(1, 2), flag=ux.ALIGN_RIGHT | ux.TOP, border=4)
        self.agent_settings_sizer = ux.BoxSizer(ux.HORIZONTAL).AddToSizer(self.command_sizer, pos=(1, 0), span=(2, 1), flag=ux.ALIGN_CENTER_VERTICAL | ux.ALIGN_RIGHT)
        self.do_iteration_sizer = ux.BoxSizer(ux.HORIZONTAL).AddToSizer(self.command_sizer, pos=(1, 1), flag=ux.ALIGN_RIGHT | ux.TOP, border=4)
        self.do_iterations_sizer = ux.BoxSizer(ux.HORIZONTAL).AddToSizer(self.command_sizer, pos=(2, 1), flag=ux.ALIGN_RIGHT | ux.TOP | ux.BOTTOM, border=4)

        # 
        self.grid_canvas.AddToSizer(self.grid_sizer, pos=(0, 0), flag=ux.ALIGN_CENTER | ux.SHAPED)

        self.train_button.AddToSizer(self.training_sizer, flag=ux.ALIGN_CENTER_VERTICAL | ux.LEFT)
        self.cancel_training_button.AddToSizer(self.training_sizer, flag=ux.ALIGN_CENTER_VERTICAL | ux.LEFT, border=4) 
        self.train_count_text.AddToSizer(self.training_sizer, flag=ux.ALIGN_CENTER_VERTICAL | ux.LEFT, border=4)
        self.train_batch_time_elapsed_text.AddToSizer(self.training_sizer, flag=ux.ALIGN_CENTER_VERTICAL | ux.LEFT, border=4)
        
        self.do_iteration_button.AddToSizer(self.do_iteration_sizer, flag=ux.ALIGN_CENTER_VERTICAL)

        self.do_iterations_speed_label.AddToSizer(self.do_iterations_sizer, flag=ux.ALIGN_CENTER_VERTICAL)
        self.do_iterations_speed_spinbox.AddToSizer(self.do_iterations_sizer, flag=ux.ALIGN_CENTER_VERTICAL | ux.LEFT, border=2) 
        self.do_iterations_button.AddToSizer(self.do_iterations_sizer, flag=ux.ALIGN_CENTER_VERTICAL | ux.LEFT, border=4) 
        self.cancel_iterations_button.AddToSizer(self.do_iterations_sizer, flag=ux.ALIGN_CENTER_VERTICAL | ux.LEFT, border=4)


    """------------------------------------------------------------------------------------------------
    """
    def __grid_canvas__OnDraw(self, sender, event_args):
        cgc = event_args.CGC

        # scene
        scene = self.grid_environment.get_scene()

        # cell size
        (cw, ch) = (cgc.GetSize()[0]/scene.shape[1:3][0], cgc.GetSize()[1]/scene.shape[1:3][1])

        # draw grid
        for ci in np.ndindex(scene.shape[1:3]):
            (x, y, w, h) = (ci[1]*cw, ci[0]*ch, cw, ch)
            match scene[0,ci[0],ci[1]]:
                case 0:
                    cgc.DrawRectangle(x=x, y=y, w=w, h=h, pen=ux.BLACK_PEN, brush=ux.WHITE_BRUSH)
                case 1: 
                    cgc.DrawRectangle(x=x, y=y, w=w, h=h, pen=ux.BLACK_PEN, brush=ux.GRAY_BRUSH)
            
        # draw agents
        for agent in self.grid_environment.get_agents():
            ci = np.argwhere(scene[agent.get_id(),:,:] == agent.get_id())[0]
            match agent.get_kind():
                case GridAgentKind.CHASER:
                    (x, y, r) = (ci[1]*cw + cw/2, ci[0]*ch + ch/2, min(cw/4, ch/4))
                    cgc.DrawCircle(x=x, y=y, r=r, pen=ux.BLACK_PEN, brush=ux.RED_BRUSH)
                case GridAgentKind.CHASED:
                    (x, y, r) = (ci[1]*cw + cw/2, ci[0]*ch + ch/2, min(cw/5, ch/5))
                    cgc.DrawCircle(x=x, y=y, r=r, pen=ux.BLACK_PEN, brush=ux.LIME_BRUSH)
                   
    """------------------------------------------------------------------------------------------------
    """
    def __train_button__OnPress(self, sender, event_args):
        if(self.training_is_running):
            return
        self.training_is_running = True

        def _():
            N = 0
            while self.training_is_running:
                sw = dgn.Stopwatch().start()
                n = 500
                self.grid_environment_for_training.do_iterations(n, log_transition=True)
                self.grid_environment.learn_from_logged_transitions(self.grid_environment_for_training)
                N += n
                self.train_count_text.Label = str(N)
                self.train_batch_time_elapsed_text.Label = str(sw.stop().elapsed)
        thread = pc.Thread(fn=_)
        thread.start()
        
    def __cancel_training_button__OnPress(self, sender, event_args):
        if(not self.training_is_running):
            return
        self.training_is_running = False

    """------------------------------------------------------------------------------------------------
    """
    def __do_iteration_button__OnPress(self, sender, event_args):
        agents_iterator = core.ObjectStorage.intercept(self, 'agents_iterator', lambda: itertools.cycle(self.grid_environment.get_agents()))
        agent = next(agents_iterator)
        self.grid_environment.do_iteration(agents=(agent,))
        self.grid_canvas.UpdateDrawing()  

    """------------------------------------------------------------------------------------------------
    """
    def __do_iterations_button__OnPress(self, sender, event_args):
        if(self.do_iterations_is_running):
            return
        self.do_iterations_is_running = True

        self.do_iteration_sizer.DisableChildren()

        def _():
            agents_iterator = core.ObjectStorage.intercept(self, 'agents_iterator', lambda: itertools.cycle(self.grid_environment.get_agents()))
            while self.do_iterations_is_running:
                agent = next(agents_iterator)
                self.grid_environment.do_iteration(agents=(agent,))
                self.grid_canvas.UpdateDrawing()
                time.sleep(self.do_iterations_speed_spinbox.GetValue())          
        thread = pc.Thread(fn=_)
        thread.start()

    def __cancel_iterations_button__OnPress(self, sender, event_args):
        if(not self.do_iterations_is_running):
            return
        self.do_iterations_is_running = False

        self.do_iteration_sizer.EnableChildren()
