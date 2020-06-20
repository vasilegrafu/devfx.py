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

        """----------------------------------------------------------------
        """
        self.environment = GridEnvironment()
        self.environment.create_agent(id='agent1',
                                      kind='CHASER', 
                                      state=self.environment.get_random_non_terminal_state(agent_kind='CHASER'),
                                      policy=ml.rl.QPolicy(discount_factor=0.95, learning_rate=0.25))
        self.environment.create_agent(id='agent2',
                                      kind='CHASED', 
                                      state=self.environment.get_random_non_terminal_state(agent_kind='CHASED'),
                                      policy=ml.rl.QPolicy(discount_factor=0.95, learning_rate=0.25))
        self.runner = ml.rl.EpisodicTaskRunner(agents=self.environment.get_agents())
        self.runner.running_status += core.SignalHandler(self.__running_status)

        """----------------------------------------------------------------
        """
        self.grid_panel = wx.Panel(self)
        self.grid_panel.Bind(wx.EVT_PAINT, self.__grid_panel_paint)

        """----------------------------------------------------------------
        """
        self.agent_for_displaying_policy_choice_label = wx.StaticText(self, label="Display policy for agent:")
        self.agent_for_displaying_policy_choice = wx.Choice(self, choices=['No agent'] + [agent.get_id() for agent in self.environment.get_agents()])
        self.agent_for_displaying_policy_choice.Bind(wx.EVT_CHOICE, self.__agent_for_displaying_policy_choice_change)
        self.agent_for_displaying_policy_choice.SetSelection(0)

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

    def __apply_styles(self):
        self.SetTitle("RL")
        self.SetSize((1024, 768))
        self.Centre()

        sizer1 = wx.BoxSizer(wx.VERTICAL)
        sizer11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer1.Add(sizer11, proportion=1, flag=wx.EXPAND)
        sizer12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer1.Add(sizer12, proportion=0, flag=wx.EXPAND)  
        sizer121 = wx.BoxSizer(wx.HORIZONTAL)
        sizer12.Add(sizer121, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)  
        sizer122 = wx.BoxSizer(wx.VERTICAL)
        sizer12.Add(sizer122, proportion=3, flag=wx.EXPAND | wx.ALL, border=5)  
        sizer1221 = wx.BoxSizer(wx.HORIZONTAL)
        sizer122.Add(sizer1221, proportion=1, flag=wx.ALIGN_RIGHT) 
        sizer122.AddSpacer(5)
        sizer1222 = wx.BoxSizer(wx.HORIZONTAL)
        sizer122.Add(sizer1222, proportion=1, flag=wx.ALIGN_RIGHT)  
        self.SetSizer(sizer1)
        
        sizer11.Add(self.grid_panel, proportion=1, flag=wx.EXPAND)  
        sizer121.Add(self.agent_for_displaying_policy_choice_label, flag=wx.ALIGN_CENTER_VERTICAL)
        sizer121.Add(self.agent_for_displaying_policy_choice, flag=wx.ALIGN_CENTER_VERTICAL)
        sizer1221.Add(self.run_visual_training_button, flag=wx.ALIGN_CENTER_VERTICAL)
        sizer1221.AddSpacer(5) 
        sizer1221.Add(self.visual_training_randomness_variator_label, flag=wx.ALIGN_CENTER_VERTICAL)
        sizer1221.Add(self.visual_training_randomness_variator, flag=wx.ALIGN_CENTER_VERTICAL)
        sizer1221.AddSpacer(5)
        sizer1221.Add(self.visual_training_speed_variator_label, flag=wx.ALIGN_CENTER_VERTICAL)
        sizer1221.Add(self.visual_training_speed_variator, flag=wx.ALIGN_CENTER_VERTICAL)
        sizer1221.AddSpacer(5)
        sizer1221.Add(self.cancel_visual_training_running_button, flag=wx.ALIGN_CENTER_VERTICAL)
  
        sizer1222.Add(self.run_training_button, flag=wx.ALIGN_CENTER_VERTICAL)
        sizer1222.AddSpacer(5) 
        sizer1222.Add(self.training_randomness_variator_label, flag=wx.ALIGN_CENTER_VERTICAL)
        sizer1222.Add(self.training_randomness_variator, flag=wx.ALIGN_CENTER_VERTICAL)
        sizer1222.AddSpacer(5)
        sizer1222.Add(self.cancel_training_running_button, flag=wx.ALIGN_CENTER_VERTICAL)

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

    def __agent_for_displaying_policy_choice_change(self, event):
        self.__draw_grid_environment()

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
        for (cell_index, cell_content) in self.environment.get_cells():
            self.__draw_grid_cell(cell_index=cell_index, cell_content=cell_content, dc=dc)

        # draw agents
        for agent in self.environment.get_agents():
            self.__draw_grid_agent(agent=agent, dc=dc)

        # draw agent policies
        # for (cell_index, cell_content) in self.environment.get_cells():
        #     self.__draw_grid_agent_policy(agents=self.environment.get_agents(), cell_index=cell_index, cell_content=cell_content, dc=dc)

    def __draw_grid_cell(self, cell_index, cell_content, dc):
        (env_row_count, env_column_count) = self.environment.get_shape()
        (dc_w, dc_h) = dc.GetSize()
        (rect_w0, rect_h0) = (dc_w*((cell_index[1]-1)/env_column_count), dc_h*((cell_index[0]-1)/env_row_count))
        (rect_dw, rect_dh) = (dc_w/env_column_count, dc_h/env_row_count)

        if(cell_content is None):
            dc.SetPen(wx.Pen(wx.Colour(0, 0, 0, wx.ALPHA_TRANSPARENT))) 
            dc.SetBrush(wx.Brush(wx.Colour(0, 0, 0))) 
            dc.DrawRectangle(rect_w0, rect_h0, rect_dw, rect_dh) 
        else:
            dc.SetPen(wx.Pen(wx.Colour(0, 0, 0, wx.ALPHA_TRANSPARENT))) 
            dc.SetBrush(wx.Brush(wx.Colour(0, 255, 0)))
            dc.DrawRectangle(rect_w0, rect_h0, rect_dw, rect_dh) 

    def __draw_grid_agent(self, agent, dc):
        cell_index = agent.get_state().value[0]
        (env_row_count, env_column_count) = self.environment.get_shape()
        (dc_w, dc_h) = dc.GetSize()
        (rect_w0, rect_h0) = (dc_w*((cell_index[1]-1)/env_column_count), dc_h*((cell_index[0]-1)/env_row_count))
        (rect_dw, rect_dh) = (dc_w/env_column_count, dc_h/env_row_count)

        dc.SetPen(wx.Pen(wx.Colour(0, 0, 0))) 
        if(agent.get_kind() == 'CHASER'):
            dc.SetBrush(wx.Brush(wx.Colour(255, 0, 0))) 
            dc.DrawCircle(rect_w0 + rect_dw/2, rect_h0 + rect_dh/2, min(rect_dw/3, rect_dh/3)) 
        elif(agent.get_kind() == 'CHASED'):
            dc.SetBrush(wx.Brush(wx.Colour(0, 0, 255)))
            dc.DrawCircle(rect_w0 + rect_dw/2, rect_h0 + rect_dh/2, min(rect_dw/4, rect_dh/4)) 
        else:
            raise exps.ApplicationError()
        

    def __draw_grid_agent_policy(self, agents, cell_index, cell_content, dc):
        if(cell_content is None):
            pass
        else:
            (env_row_count, env_column_count) = self.environment.get_shape()
            (dc_w, dc_h) = dc.GetSize()
            (rect_w0, rect_h0) = (dc_w*((cell_index[1]-1)/env_column_count), dc_h*((cell_index[0]-1)/env_row_count))
            (rect_dw, rect_dh) = (dc_w/env_column_count, dc_h/env_row_count)

            state = ml.rl.State(value=cell_index)
            agent_id = self.agent_for_displaying_policy_choice.GetString(n=self.agent_for_displaying_policy_choice.GetSelection())
            if(self.environment.exists_agent(id=agent_id)):
                agent = self.environment.get_agent(id=agent_id)
                policy = agent.get_policy()
                if(state in policy.qtable):
                    actions = policy.qtable[state]
                    for action in actions:
                        dc.SetPen(wx.Pen(wx.Colour(0, 0, 0))) 
                        dc.SetBrush(wx.Brush(wx.Colour(255, 0, 0))) 
                        text = f'{policy.qtable[state][action]:.2f}'
                        (tw, th) = dc.GetTextExtent(text)
                        if(action == GridActions.Left):
                            (cw, ch) = (rect_w0+2, rect_h0+rect_dh/2-th/2)
                        elif(action == GridActions.Right):
                            (cw, ch) = (rect_w0+rect_dw-tw-2, rect_h0+rect_dh/2-th/2) 
                        elif(action == GridActions.Up):
                            (cw, ch) = (rect_w0+rect_dw/2-tw/2, rect_h0+2) 
                        elif(action == GridActions.Down):
                            (cw, ch) = (rect_w0+rect_dw/2-tw/2, rect_h0+rect_dh-th-2)
                        elif(action == GridActions.Stay):
                            (cw, ch) = (rect_w0+rect_dw/2-tw/2, rect_h0+rect_dh/2-th/2) 
                        else:
                            raise exps.NotImplementedError()
                        dc.DrawText(text, cw, ch) 





