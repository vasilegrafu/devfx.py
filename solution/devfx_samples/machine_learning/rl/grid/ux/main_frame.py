import wx
import threading as th
import time as t
import random as rnd
import devfx.exceptions as exps
import devfx.core as core
import devfx.machine_learning as ml
from .. logic.grid_environment import GridEnvironment
from .. logic.grid_actions import GridActions

class MainFrame(wx.Frame):
    """------------------------------------------------------------------------------------------------
    """
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.grid_panel = wx.Panel(self)
        self.grid_panel.Bind(wx.EVT_PAINT, self.__grid_panel_paint)

        """----------------------------------------------------------------
        """
        self.run_visual_training_button = wx.Button(self, label="Run visual training")
        self.run_visual_training_button.Enabled = True
        self.run_visual_training_button.Bind(wx.EVT_BUTTON, self.__run_visual_training_button_click)

        self.visual_training_randomness_variator_label = wx.StaticText(self, label='Randomness:')
        self.visual_training_randomness_variator = wx.SpinCtrlDouble(self, min=0.0, max=1.0, initial=1.0, inc=0.05)

        self.visual_training_speed_variator_label = wx.StaticText(self, label='Speed:')
        self.visual_training_speed_variator = wx.SpinCtrlDouble(self, min=0.0, max=1.0, initial=0.25, inc=0.05)

        self.cancel_visual_training_running_button = wx.Button(self, label="Cancel")
        self.cancel_visual_training_running_button.Bind(wx.EVT_BUTTON, self.__cancel_visual_training_running_button_click)
        self.cancel_visual_training_running_button.Enabled = False

        self.__visual_training_is_running = False
        self.__visual_training_cancelling_is_requested = False

        """----------------------------------------------------------------
        """
        self.run_training_button = wx.Button(self, label="Run training")
        self.run_training_button.Enabled = True
        self.run_training_button.Bind(wx.EVT_BUTTON, self.__run_training_button_click)

        self.training_randomness_variator_label = wx.StaticText(self, label='Randomness:')
        self.training_randomness_variator = wx.SpinCtrlDouble(self, min=0.0, max=1.0, initial=1.0, inc=0.05)

        self.cancel_training_running_button = wx.Button(self, label="Cancel")
        self.cancel_training_running_button.Bind(wx.EVT_BUTTON, self.__cancel_training_running_button_click)
        self.cancel_training_running_button.Enabled = False

        self.__training_is_running = False
        self.__training_cancelling_is_requested = False

        """----------------------------------------------------------------
        """
        self.__apply_styles()

        """----------------------------------------------------------------
        """
        self.environment = GridEnvironment()
        self.environment.create_agent(id='agent1',
                                      kind='AGENT', 
                                      state=self.environment.get_random_non_terminal_state(agent_kind='AGENT'),
                                      policy=ml.rl.QPolicy(discount_factor=0.95, learning_rate=0.25))
        self.environment.create_agent(id='agent2',
                                      kind='AGENT', 
                                      state=self.environment.get_random_non_terminal_state(agent_kind='AGENT'),
                                      policy=ml.rl.QPolicy(discount_factor=0.95, learning_rate=0.25))
        self.runner = ml.rl.EpisodicRunner(agents=self.environment.get_agents())
        self.runner.running_status += core.SignalHandler(self.__running_status)

    def __apply_styles(self):
        self.SetTitle("RL")
        self.SetSize((1024, 768))
        self.Centre()

        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.grid_panel, proportion=1, flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=10)

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(self.run_visual_training_button, flag=wx.ALIGN_CENTER_VERTICAL)
        hsizer1.AddSpacer(5) 
        hsizer1.Add(self.visual_training_randomness_variator_label, flag=wx.ALIGN_CENTER_VERTICAL)
        hsizer1.Add(self.visual_training_randomness_variator, flag=wx.ALIGN_CENTER_VERTICAL)
        hsizer1.AddSpacer(5)
        hsizer1.Add(self.visual_training_speed_variator_label, flag=wx.ALIGN_CENTER_VERTICAL)
        hsizer1.Add(self.visual_training_speed_variator, flag=wx.ALIGN_CENTER_VERTICAL)
        hsizer1.AddSpacer(5)
        hsizer1.Add(self.cancel_visual_training_running_button, flag=wx.ALIGN_CENTER_VERTICAL)
        hsizer1.AddSpacer(5)
        vsizer.Add(hsizer1, proportion=0, flag=wx.ALIGN_RIGHT | wx.TOP | wx.BOTTOM | wx.LEFT | wx.RIGHT, border=10)

        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.Add(self.run_training_button, flag=wx.ALIGN_CENTER_VERTICAL)
        hsizer2.AddSpacer(5) 
        hsizer2.Add(self.training_randomness_variator_label, flag=wx.ALIGN_CENTER_VERTICAL)
        hsizer2.Add(self.training_randomness_variator, flag=wx.ALIGN_CENTER_VERTICAL)
        hsizer2.AddSpacer(5)
        hsizer2.Add(self.cancel_training_running_button, flag=wx.ALIGN_CENTER_VERTICAL)
        hsizer2.AddSpacer(5)
        vsizer.Add(hsizer2, proportion=0, flag=wx.ALIGN_RIGHT | wx.TOP | wx.BOTTOM | wx.LEFT | wx.RIGHT, border=10)
        self.SetSizer(vsizer)


    """------------------------------------------------------------------------------------------------
    """
    def __grid_panel_paint(self, event):
        self.__draw_grid_environment()


    def __run_visual_training_button_click(self, event):
        thread = th.Thread(target=self.__visual_train_grid_agents)
        thread.start()

    def __cancel_visual_training_running_button_click(self, event):
        self.__visual_training_cancelling_is_requested = True

    def __run_training_button_click(self, event):
        thread = th.Thread(target=self.__train_grid_agents)
        thread.start()

    def __cancel_training_running_button_click(self, event):
        self.__training_cancelling_is_requested = True

    """------------------------------------------------------------------------------------------------
    """
    def __visual_train_grid_agents(self):
        self.run_visual_training_button.Enabled = False
        self.cancel_visual_training_running_button.Enabled = True

        self.__visual_training_is_running = True
        self.runner.run(episode_count=10000, randomness=self.visual_training_randomness_variator.GetValue())
        self.__visual_training_is_running = False

        self.run_visual_training_button.Enabled = True
        self.cancel_visual_training_running_button.Enabled = False

        self.__draw_grid_environment()

    def __train_grid_agents(self):
        self.run_training_button.Enabled = False
        self.cancel_training_running_button.Enabled = True

        self.__training_is_running = True
        self.runner.run(episode_count=10000, randomness=self.training_randomness_variator.GetValue())
        self.__training_is_running = False

        self.run_training_button.Enabled = True
        self.cancel_training_running_button.Enabled = False

        self.__draw_grid_environment()
        

    def __running_status(self, source, signal_args):
        if(self.__visual_training_is_running):
            self.__draw_grid_environment()
            t.sleep(self.visual_training_speed_variator.GetValue())
            signal_args.running_parameters.randomness=self.visual_training_randomness_variator.GetValue()
            if(self.__visual_training_cancelling_is_requested):
                signal_args.running_parameters.cancellation_token.request_cancellation()
                self.__visual_training_cancelling_is_requested = False

        if(self.__training_is_running):
            signal_args.running_parameters.randomness=self.training_randomness_variator.GetValue()
            if(self.__training_cancelling_is_requested):
                signal_args.running_parameters.cancellation_token.request_cancellation()
                self.__training_cancelling_is_requested = False

    """------------------------------------------------------------------------------------------------
    """
    def __draw_grid_environment(self):
        dc = wx.BufferedDC(wx.ClientDC(self.grid_panel))
        dc.Clear()

        # draw cells
        for (ci, cc) in self.environment.get_cells():
            self.__draw_grid_cell(ci=ci, cc=cc, dc=dc)

        # draw agents
        for agent in self.environment.get_agents():
            self.__draw_grid_agent(agent=agent, dc=dc)

        # draw agent policies
        for (ci, cc) in self.environment.get_cells():
            self.__draw_grid_agent_policy(agents=self.environment.get_agents(), ci=ci, cc=cc, dc=dc)

    def __draw_grid_cell(self, ci, cc, dc):
        (c_ri, c_ci) = ci
        (env_rc, env_cc) = self.environment.get_size()
        (dc_w, dc_h) = dc.GetSize()
        (r_w0, r_h0) = (dc_w*(c_ci/env_cc), dc_h*(c_ri/env_rc))
        (r_dw, r_dh) = (dc_w/env_cc, dc_h/env_rc)

        if(cc is None):
            dc.SetPen(wx.Pen(wx.Colour(0, 0, 0, wx.ALPHA_TRANSPARENT))) 
            dc.SetBrush(wx.Brush(wx.Colour(0, 0, 0))) 
            dc.DrawRectangle(r_w0, r_h0, r_dw, r_dh) 
        else:
            (state, reward) = cc
            dc.SetPen(wx.Pen(wx.Colour(0, 0, 0, wx.ALPHA_TRANSPARENT))) 
            if(state.kind == ml.rl.StateKind.TERMINAL):
                dc.SetBrush(wx.Brush(wx.Colour(0, 0, 255))) 
            elif(state.kind == ml.rl.StateKind.NON_TERMINAL):
                dc.SetBrush(wx.Brush(wx.Colour(0, 255, 0)))
            else:
                raise exps.NotImplementedError()
            dc.DrawRectangle(r_w0, r_h0, r_dw, r_dh) 
            dc.DrawText(f'r:{reward.value:.2f}', r_w0+2, r_h0+2) 

    def __draw_grid_agent(self, agent, dc):
        (c_ri, c_ci) = agent.get_state().value
        (env_rc, env_cc) = self.environment.get_size()
        (dc_w, dc_h) = dc.GetSize()
        (r_w0, r_h0) = (dc_w*(c_ci/env_cc), dc_h*(c_ri/env_rc))
        (r_dw, r_dh) = (dc_w/env_cc, dc_h/env_rc)

        dc.SetPen(wx.Pen(wx.Colour(0, 0, 0))) 
        dc.SetBrush(wx.Brush(wx.Colour(255, 0, 0))) 
        dc.DrawCircle(r_w0 + r_dw/2, r_h0 + r_dh/2, min(r_dw/4, r_dh/4)) 

    def __draw_grid_agent_policy(self, agents, ci, cc, dc):
        if(cc is None):
            pass
        else:
            (c_ri, c_ci) = ci
            (env_rc, env_cc) = self.environment.get_size()
            (dc_w, dc_h) = dc.GetSize()
            (r_w0, r_h0) = (dc_w*(c_ci/env_cc), dc_h*(c_ri/env_rc))
            (r_dw, r_dh) = (dc_w/env_cc, dc_h/env_rc)

            (state, reward) = cc
            for agent in agents:
                policy = agent.get_policy()
                if(state in policy.qtable):
                    actions = policy.qtable[state]
                    for action in actions:
                        dc.SetPen(wx.Pen(wx.Colour(0, 0, 0))) 
                        dc.SetBrush(wx.Brush(wx.Colour(255, 0, 0))) 
                        text = f'{policy.qtable[state][action]:.2f}'
                        (tw, th) = dc.GetTextExtent(text)
                        if(action == GridActions.Left):
                            (cw, ch) = (r_w0+2, r_h0+r_dh/2-th/2)
                        elif(action == GridActions.Right):
                            (cw, ch) = (r_w0+r_dw-tw-2, r_h0+r_dh/2-th/2) 
                        elif(action == GridActions.Up):
                            (cw, ch) = (r_w0+r_dw/2-tw/2, r_h0+2) 
                        elif(action == GridActions.Down):
                            (cw, ch) = (r_w0+r_dw/2-tw/2, r_h0+r_dh-th-2)
                        elif(action == GridActions.Stay):
                            (cw, ch) = (r_w0+r_dw/2-tw/2, r_h0+r_dh/2-th/2) 
                        else:
                            raise exps.NotImplementedError()
                        dc.DrawText(text, cw, ch) 





