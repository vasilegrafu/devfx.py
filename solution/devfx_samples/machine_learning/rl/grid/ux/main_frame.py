import wx
import time as t
import random as rnd
import devfx.exceptions as exps
import devfx.core as core
import devfx.machine_learning as ml
from .. logic.environment import Environment
from .. logic.possible_actions import PossibleActions

class MainFrame(wx.Frame):
    """------------------------------------------------------------------------------------------------
    """
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.grid_panel = wx.Panel(self)
        self.grid_panel.Bind(wx.EVT_PAINT, self.grid_panel_paint)

        self.train_button = wx.Button(self, label="Train")
        self.train_button.Bind(wx.EVT_BUTTON, self.train_button_click)

        self.__apply_styles()

        self.environment = Environment()
        agent1 = self.environment.create_agent(name='agent1',
                                               state=self.environment.get_random_non_terminal_state(),
                                               policy=ml.rl.QPolicy(discount_factor=0.9, learning_rate=0.25))
        agent1.training_info_update += core.SignalHandler(self.training_info_update)
        agent1.training_progress += core.SignalHandler(self.training_progress)

    def __apply_styles(self):
        self.SetTitle("RL")
        self.SetSize((1024, 768))
        self.Centre()

        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.grid_panel, proportion=1, flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=10)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(self.train_button)
        vsizer.Add(hsizer, proportion=0, flag=wx.ALIGN_RIGHT | wx.TOP | wx.BOTTOM | wx.LEFT | wx.RIGHT, border=10)
        self.SetSizer(vsizer)

    """------------------------------------------------------------------------------------------------
    """
    def grid_panel_paint(self, event):
        self.__draw_grid_environment()

    def train_button_click(self, event):
        for agent in self.environment.get_agents():
            agent.train(episodes=1000, epsilon=1.0)
        self.__draw_grid_environment()

    """------------------------------------------------------------------------------------------------
    """
    def training_info_update(self, source, event_args):
        pass

    def training_progress(self, source, event_args):
        self.__draw_grid_environment()
        t.sleep(0.1)

    """------------------------------------------------------------------------------------------------
    """
    def __draw_grid_environment(self):
        dc = wx.ClientDC(self.grid_panel)
        dc.SetBackground(wx.Brush(wx.Colour(255, 255, 255)))
        dc.Clear()

        # draw grid_cells
        for state in self.environment.get_states():
            self.__draw_grid_cell_state(state=state, dc=dc)

        # draw grid_agents
        for agent in self.environment.get_agents():
            self.__draw_grid_agent(agent=agent, dc=dc)

         # draw grid_agent policies
        for agent in self.environment.get_agents():
            for state in self.environment.get_states():
                self.__draw_grid_agent_policy(agent=agent, state=state, dc=dc)

       
    def __draw_grid_cell_state(self, state, dc):
        (sv_ri, sv_ci) = state.value
        (env_rc, env_cc) = self.environment.get_size()
        (dc_w, dc_h) = dc.GetSize()
        (r_w0, r_h0) = (dc_w*((sv_ci-1)/env_cc), dc_h*((sv_ri-1)/env_rc))
        (r_dw, r_dh) = (dc_w/env_cc, dc_h/env_rc)

        if(state.kind == ml.rl.StateKind.BLOCKED):
            dc.SetBrush(wx.Brush(wx.Colour(0, 0, 0))) 
        elif(state.kind == ml.rl.StateKind.TERMINAL):
            dc.SetBrush(wx.Brush(wx.Colour(0, 0, 255))) 
        elif(state.kind == ml.rl.StateKind.NON_TERMINAL):
            dc.SetBrush(wx.Brush(wx.Colour(0, 255, 0)))
        else:
            raise exps.NotImplementedError()
        dc.SetPen(wx.Pen(wx.Colour(0, 0, 0)))
        dc.DrawRectangle(r_w0, r_h0, r_dw, r_dh) 

        dc.DrawText(f'r:{state.reward:.2f}', r_w0+2, r_h0+2) 

    def __draw_grid_agent(self, agent, dc):
        (sv_ri, sv_ci) = agent.get_state().value
        (env_rc, env_cc) = self.environment.get_size()
        (dc_w, dc_h) = dc.GetSize()
        (r_w0, r_h0) = (dc_w*((sv_ci-1)/env_cc), dc_h*((sv_ri-1)/env_rc))
        (r_dw, r_dh) = (dc_w/env_cc, dc_h/env_rc)

        dc.SetPen(wx.Pen(wx.Colour(0, 0, 0))) 
        dc.SetBrush(wx.Brush(wx.Colour(255, 0, 0))) 
        dc.DrawCircle(r_w0 + r_dw/2, r_h0 + r_dh/2, min(r_dw/4, r_dh/4)) 

    def __draw_grid_agent_policy(self, agent, state, dc):
        (sv_ri, sv_ci) = state.value
        (env_rc, env_cc) = self.environment.get_size()
        (dc_w, dc_h) = dc.GetSize()
        (r_w0, r_h0) = (dc_w*((sv_ci-1)/env_cc), dc_h*((sv_ri-1)/env_rc))
        (r_dw, r_dh) = (dc_w/env_cc, dc_h/env_rc)

        policy = agent.get_policy()
        if(state in policy.qtable):
            actions = policy.qtable[state]
            for action in actions:
                if(action == PossibleActions.Left):
                    (cw, ch) = (r_w0+2, r_h0+r_dh/2)
                elif(action == PossibleActions.Right):
                    (cw, ch) = (r_w0+r_dw-40, r_h0+r_dh/2) 
                elif(action == PossibleActions.Up):
                    (cw, ch) = (r_w0+r_dw/2, r_h0+2) 
                elif(action == PossibleActions.Down):
                    (cw, ch) = (r_w0+r_dw/2, r_h0+r_dh-16) 
                else:
                    raise exps.NotImplementedError()
                dc.SetPen(wx.Pen(wx.Colour(0, 0, 0))) 
                dc.SetBrush(wx.Brush(wx.Colour(255, 0, 0))) 
                dc.DrawText(f'{policy.qtable[state][action]:.4f}', cw, ch) 





