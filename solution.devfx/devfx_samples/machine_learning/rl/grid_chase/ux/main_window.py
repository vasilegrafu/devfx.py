import time
import numpy as np
import devfx.exceptions as excs
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

        self.__setup_logic()

        self.Center()
        self.__setup_widgets()
        self.__setup_layout()

    """------------------------------------------------------------------------------------------------
    """
    def __setup_logic(self):
        self.grid_environment_for_training = GridEnvironment(training=True)
        self.grid_environment_for_training.setup()

        self.grid_environment = GridEnvironment()
        self.grid_environment.setup()
        
    """------------------------------------------------------------------------------------------------
    """
    def __setup_widgets(self):
        self.grid_canvas = ux.Canvas(self, size=(256, 256))
        self.grid_canvas.OnDraw += self.__grid_canvas__OnDraw

        self.train_button = ux.Button(parent=self, label='Train')
        self.train_button.OnPress += self.__train_button__OnPress
        self.cancel_training_button = ux.Button(parent=self, label='Cancel training')
        self.cancel_training_button.OnPress += self.__cancel_training_button__OnPress
        self.train_count_text_label = ux.Text(parent=self, label='Iterations:')
        self.train_count_text = ux.Text(parent=self, label='0', size=(64, -1))
        self.train_batch_time_elapsed_text_label = ux.Text(parent=self, label='Time elapsed/batch:')
        self.train_batch_time_elapsed_text = ux.Text(parent=self, label='0', size=(64, -1))
        self.training_is_running = False
        
        self.do_action_button = ux.Button(parent=self, label='Do action')
        self.do_action_button.OnPress += self.__do_action_button__OnPress
        
        self.do_actions_speed_label = ux.Text(parent=self, label='Speed:')
        self.do_actions_speed_spinbox = ux.FloatSpinBox(parent=self, min=0.01, max=1.0, initial=0.10, inc=0.01, size=(64, -1))
        self.do_actions_button = ux.Button(parent=self, label='Do actions')
        self.do_actions_button.OnPress += self.__do_actions_button__OnPress
        self.cancel_actions_button = ux.Button(parent=self, label='Cancel actions')
        self.cancel_actions_button.OnPress += self.__cancel_actions_button__OnPress
        self.do_actions_is_running = False

        self.reset_button = ux.Button(parent=self, label='Reset')
        self.reset_button.OnPress += self.__reset_button__OnPress

    def __init_layout(self):
        #
        self.window_sizer = ux.BoxSizer(ux.HORIZONTAL).AddToWindow(self)

        self.grid_canvas.AddToSizer(self.window_sizer, flag=ux.SHAPED | ux.EXPAND | ux.ALL, border=4)

        self.command_sizer = ux.BoxSizer(ux.VERTICAL).AddToSizer(self.window_sizer, flag=ux.EXPAND)

        self.training_sizer = ux.BoxSizer(ux.HORIZONTAL).AddToSizer(self.command_sizer, flag=ux.EXPAND)
        self.train_button.AddToSizer(self.training_sizer, flag=ux.ALIGN_LEFT | ux.ALIGN_CENTER_VERTICAL | ux.ALL, border=4)
        self.cancel_training_button.AddToSizer(self.training_sizer, flag=ux.ALIGN_LEFT | ux.ALIGN_CENTER_VERTICAL | ux.ALL, border=4) 
        self.training_sizer_info = ux.BoxSizer(ux.HORIZONTAL).AddToSizer(self.command_sizer, flag=ux.EXPAND)
        self.train_count_text_label.AddToSizer(self.training_sizer_info, flag=ux.ALIGN_LEFT | ux.ALIGN_CENTER_VERTICAL | ux.ALL, border=4)
        self.train_count_text.AddToSizer(self.training_sizer_info, flag=ux.ALIGN_LEFT | ux.ALIGN_CENTER_VERTICAL | ux.ALL, border=4)
        self.train_batch_time_elapsed_text_label.AddToSizer(self.training_sizer_info, flag=ux.ALIGN_LEFT | ux.ALIGN_CENTER_VERTICAL | ux.ALL, border=4)
        self.train_batch_time_elapsed_text.AddToSizer(self.training_sizer_info, flag=ux.ALIGN_LEFT | ux.ALIGN_CENTER_VERTICAL | ux.ALL, border=4)

        self.do_action_sizer = ux.BoxSizer(ux.HORIZONTAL).AddToSizer(self.command_sizer, flag=ux.EXPAND)
        self.do_action_button.AddToSizer(self.do_action_sizer, flag=ux.ALIGN_LEFT | ux.ALIGN_CENTER_VERTICAL | ux.ALL, border=4)

        self.do_actions_sizer = ux.BoxSizer(ux.HORIZONTAL).AddToSizer(self.command_sizer, flag=ux.EXPAND)
        self.do_actions_button.AddToSizer(self.do_actions_sizer, flag=ux.ALIGN_LEFT | ux.ALIGN_CENTER_VERTICAL | ux.ALL, border=4)
        self.cancel_actions_button.AddToSizer(self.do_actions_sizer, flag=ux.ALIGN_LEFT | ux.ALIGN_CENTER_VERTICAL | ux.ALL, border=4)
        self.do_actions_speed_label.AddToSizer(self.do_actions_sizer, flag=ux.ALIGN_LEFT | ux.ALIGN_CENTER_VERTICAL | ux.ALL, border=4)
        self.do_actions_speed_spinbox.AddToSizer(self.do_actions_sizer, flag=ux.ALIGN_LEFT | ux.ALIGN_CENTER_VERTICAL | ux.ALL, border=4)
 
        self.reset_sizer = ux.BoxSizer(ux.HORIZONTAL).AddToSizer(self.command_sizer, flag=ux.EXPAND)
        self.reset_button.AddToSizer(self.reset_sizer, flag=ux.ALIGN_LEFT | ux.ALIGN_CENTER_VERTICAL | ux.ALL, border=4)


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
                self.grid_environment.transfer_logged_transitions_from(self.grid_environment_for_training)
                self.grid_environment.learn_from_logged_transitions()
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
    def __do_action_button__OnPress(self, sender, event_args):
        if(self.grid_environment.has_agents_in_terminal_state()):
            self.grid_environment.reset()
        else:
            agent = next(self.grid_environment.get_agents_cycler())
            agent.do_action(log_transition=True)
            agent.learn_from_logged_transitions()
        self.grid_canvas.UpdateDrawing()  

    """------------------------------------------------------------------------------------------------
    """
    def __do_actions_button__OnPress(self, sender, event_args):
        if(self.do_actions_is_running):
            return
        self.do_actions_is_running = True

        self.do_action_sizer.DisableChildren()

        def _():
            while self.do_actions_is_running:
                if(self.grid_environment.has_agents_in_terminal_state()):
                    self.grid_environment.reset()
                else:
                    agent = next(self.grid_environment.get_agents_cycler())
                    agent.do_action(log_transition=True)
                    agent.learn_from_logged_transitions()
                self.grid_canvas.UpdateDrawing()
                time.sleep(self.do_actions_speed_spinbox.GetValue())          
        thread = pc.Thread(fn=_)
        thread.start()

    def __cancel_actions_button__OnPress(self, sender, event_args):
        if(not self.do_actions_is_running):
            return
        self.do_actions_is_running = False

        self.do_action_sizer.EnableChildren()

    """------------------------------------------------------------------------------------------------
    """
    def __reset_button__OnPress(self, sender, event_args):
        self.grid_environment.reset()
        self.grid_canvas.UpdateDrawing()  