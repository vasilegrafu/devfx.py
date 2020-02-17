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

        self.train_button = wx.Button(self, label="Train")
        self.train_button.Bind(wx.EVT_BUTTON, self.__train_button_click)

        self.randomness_variator_label = wx.StaticText(self, label='randomness:')
        self.randomness_variator = wx.SpinCtrlDouble(self, min=0.0, max=1.0, initial=1.0, inc=0.05)

        self.speed_variator_label = wx.StaticText(self, label='speed:')
        self.speed_variator = wx.SpinCtrlDouble(self, min=0.0, max=1.0, initial=0.25, inc=0.05)
 
        self.__apply_styles()

        self.environment = GridEnvironment()
        self.environment.create_agent(id='agent1',
                                      kind='AGENT', 
                                      state=self.environment.get_random_non_terminal_state(agent_kind='AGENT'),
                                      policy=ml.rl.QPolicy(discount_factor=0.95, learning_rate=0.25))
 
        self.runner = ml.rl.Runner(agent=self.environment())
        self.runner.running_status += core.SignalHandler(self.__running_status)

    def __apply_styles(self):
        self.SetTitle("RL")
        self.SetSize((1024, 768))
        self.Centre()

        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.grid_panel, proportion=1, flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=10)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(self.train_button, flag=wx.ALIGN_CENTER_VERTICAL)
        hsizer.AddSpacer(5) 
        hsizer.Add(self.randomness_variator_label, flag=wx.ALIGN_CENTER_VERTICAL)
        hsizer.Add(self.randomness_variator, flag=wx.ALIGN_CENTER_VERTICAL)
        hsizer.AddSpacer(5) 
        hsizer.Add(self.speed_variator_label, flag=wx.ALIGN_CENTER_VERTICAL)
        hsizer.Add(self.speed_variator, flag=wx.ALIGN_CENTER_VERTICAL)
        hsizer.AddSpacer(5) 
        vsizer.Add(hsizer, proportion=0, flag=wx.ALIGN_RIGHT | wx.TOP | wx.BOTTOM | wx.LEFT | wx.RIGHT, border=10)
        self.SetSizer(vsizer)


    """------------------------------------------------------------------------------------------------
    """
    def __grid_panel_paint(self, event):
        self.__draw_grid_environment()

    def __train_button_click(self, event):
        thread = th.Thread(target=self.__train_grid_agents)
        thread.start()

    """------------------------------------------------------------------------------------------------
    """
    def __train_grid_agents(self):
        self.train_button.Enabled = False
        self.runner.run(randomness=self.randomness_variator.GetValue(), action_count=1000)
        self.train_button.Enabled = True

    def __running_status(self, source, signal_args):
        self.__draw_grid_environment()
        
        t.sleep(self.speed_variator.GetValue())
        signal_args.running_parameters.randomness=self.randomness_variator.GetValue() 

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
        for agent in self.environment.get_agents():
            for (ci, cc) in self.environment.get_cells():
                self.__draw_grid_agent_policy(agent=agent, ci=ci, cc=cc, dc=dc)

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

    def __draw_grid_agent_policy(self, agent, ci, cc, dc):
        if(cc is None):
            pass
        else:
            (c_ri, c_ci) = ci
            (env_rc, env_cc) = self.environment.get_size()
            (dc_w, dc_h) = dc.GetSize()
            (r_w0, r_h0) = (dc_w*(c_ci/env_cc), dc_h*(c_ri/env_rc))
            (r_dw, r_dh) = (dc_w/env_cc, dc_h/env_rc)

            (state, reward) = cc
            policy = agent.get_policy()
            if(state in policy.qtable):
                actions = policy.qtable[state]
                for action in actions:
                    if(action == GridActions.Left):
                        (cw, ch) = (r_w0+2, r_h0+r_dh/2-4)
                    elif(action == GridActions.Right):
                        (cw, ch) = (r_w0+r_dw-30, r_h0+r_dh/2-4) 
                    elif(action == GridActions.Up):
                        (cw, ch) = (r_w0+r_dw/2-10, r_h0+2) 
                    elif(action == GridActions.Down):
                        (cw, ch) = (r_w0+r_dw/2-10, r_h0+r_dh-16) 
                    else:
                        raise exps.NotImplementedError()
                    dc.SetPen(wx.Pen(wx.Colour(0, 0, 0))) 
                    dc.SetBrush(wx.Brush(wx.Colour(255, 0, 0))) 
                    dc.DrawText(f'{policy.qtable[state][action]:.2f}', cw, ch) 





