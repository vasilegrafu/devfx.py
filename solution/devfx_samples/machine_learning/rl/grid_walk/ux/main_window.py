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

class MainWindow(ux.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__init_model()

        self.__init_widgets()
        self.__init_layout()

    """------------------------------------------------------------------------------------------------
    """
    def __init_model(self):
        self.grid_environment_for_training = GridEnvironment()
        self.grid_environment_for_training.create()
        self.grid_environment_for_training.setup(iteration_randomness=1.0)

        self.grid_environment = GridEnvironment()
        self.grid_environment.create()
        self.grid_environment.setup()
        
        for grid_agent in self.grid_environment.get_agents():
            grid_agent.share_policy_from(self.grid_environment_for_training.get_agent(grid_agent.id))

    """------------------------------------------------------------------------------------------------
    """
    def __init_widgets(self):
        self.grid_canvas = ux.Canvas(self, size=(64, 64))
        self.grid_canvas.OnDraw += self.__grid_canvas__OnDraw

        self.agent_iteration_randomness_label = ux.Text(self, label='Randomness:') 
        self.agent_iteration_randomness_combobox = ux.ComboBox(self, choices=[str(agent.id) + '|' + agent.name for agent in self.grid_environment.get_agents()])
        self.agent_iteration_randomness_combobox.SetSelection(0)
        def agent_iteration_randomness_combobox__OnItemSelected(sender, event_args): 
            self.agent_iteration_randomness_spinbox.SetValue(self.grid_environment.get_agent(int(self.agent_iteration_randomness_combobox.GetValue().split('|')[0])).get_iteration_randomness())
            self.grid_canvas.UpdateDrawing()
        self.agent_iteration_randomness_combobox.OnItemSelected += agent_iteration_randomness_combobox__OnItemSelected
        self.agent_iteration_randomness_spinbox = ux.FloatSpinBox(self, min=0.0, max=1.0, initial=0.0, inc=0.05, size=(64, -1))
        self.agent_iteration_randomness_spinbox.SetValue(self.grid_environment.get_agent(id=int(self.agent_iteration_randomness_combobox.GetValue().split('|')[0])).get_iteration_randomness())
        def agent_iteration_randomness_spinbox_OnValueChanged(sender, event_args): 
            self.grid_environment.get_agent(id=int(self.agent_iteration_randomness_combobox.GetValue().split('|')[0])).set_iteration_randomness(self.agent_iteration_randomness_spinbox.GetValue())
            self.grid_canvas.UpdateDrawing()
        self.agent_iteration_randomness_spinbox.OnValueChanged += agent_iteration_randomness_spinbox_OnValueChanged

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

        self.agent_iteration_randomness_label.AddToSizer(self.agent_settings_sizer, flag=ux.ALIGN_CENTER_VERTICAL)
        self.agent_iteration_randomness_combobox.AddToSizer(self.agent_settings_sizer, flag=ux.ALIGN_CENTER_VERTICAL | ux.LEFT, border=2) 
        self.agent_iteration_randomness_spinbox.AddToSizer(self.agent_settings_sizer, flag=ux.ALIGN_CENTER_VERTICAL | ux.LEFT, border=2) 
 
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
        scene_shape = self.grid_environment.scene.shape
        layer_shape = (scene_shape[1], scene_shape[2])
        state_kind_layer = self.grid_environment.scene[0,:,:]
        reward_layer = self.grid_environment.scene[1,:,:]
        agent_layer = self.grid_environment.scene[2,:,:]

        # cell size
        (cw, ch) = (cgc.GetSize()[0]/layer_shape[0], cgc.GetSize()[1]/layer_shape[1])

        # draw grid
        for ci in np.ndindex(layer_shape):
            (x, y, w, h) = (ci[1]*cw, ci[0]*ch, cw, ch)
            if(state_kind_layer[ci] == ml.rl.StateKind.UNDEFINED):                              brush=ux.GRAY_BRUSH
            elif(state_kind_layer[ci] == ml.rl.StateKind.NON_TERMINAL):                         brush=ux.WHITE_BRUSH
            elif(state_kind_layer[ci] == ml.rl.StateKind.TERMINAL and reward_layer[ci] >= 0):   brush=ux.GREEN_BRUSH
            elif(state_kind_layer[ci] == ml.rl.StateKind.TERMINAL and reward_layer[ci] < 0):    brush=ux.RED_BRUSH
            else:                                                                               raise ex.NotSupportedError()
            cgc.DrawRectangle(x=x, y=y, w=w, h=h, pen=ux.BLACK_PEN, brush=brush)

        # draw rewards
        for ci in np.ndindex(layer_shape):
            (x, y) = (ci[1]*cw + cw, ci[0]*ch)
            cgc.DrawText(text=f'{reward_layer[ci]:.2f}', x=x, y=y, offx=4, offy=0, anchor=(ux.TOP, ux.RIGHT), colour=ux.BLACK)

        # draw agents
        for agent in self.grid_environment.get_agents():
            ci = np.argwhere(agent.state.value[2,:,:] == 1)[0]
            (x, y, r) = (ci[1]*cw + cw/2, ci[0]*ch + ch/2, min(cw/4, ch/4))
            cgc.DrawCircle(x=x, y=y, r=r, pen=ux.BLACK_PEN, brush=ux.RED_BRUSH)

        # draw policy
        agent = self.grid_environment.get_agent(id=int(self.agent_iteration_randomness_combobox.GetValue().split('|')[0]))
        for (state, action, value) in agent.policy.iter:
            ci = np.argwhere(state[2,:,:] == 1)[0]
            if(action.name == 'LEFT'):      (x, y, anchor) = (ci[1]*cw, ci[0]*ch + ch/2, ux.LEFT)
            elif(action.name == 'RIGHT'):   (x, y, anchor) = (ci[1]*cw + cw, ci[0]*ch + ch/2, ux.RIGHT)
            elif(action.name == 'UP'):      (x, y, anchor) = (ci[1]*cw + cw/2, ci[0]*ch, ux.TOP) 
            elif(action.name == 'DOWN'):    (x, y, anchor) = (ci[1]*cw + cw/2, ci[0]*ch + ch, ux.BOTTOM)
            else:                           raise ex.NotImplementedError()
            cgc.DrawText(text=f'{value:.2f}', x=x, y=y, offx=4, offy=0, anchor=anchor, colour=ux.GRAY)
    
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
                n = 1000
                self.grid_environment_for_training.do_iterations(n)
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
