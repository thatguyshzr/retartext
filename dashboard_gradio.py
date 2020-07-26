import gradio as gr
from retartext import *

input= gr.inputs.Textbox(lines=7, label= 'Enter text:', placeholder= 'Type what you like.')
output = gr.outputs.Textbox(placeholder= 'tp wht U lk')

gr.Interface(fn = add_emoji, inputs= input, outputs= output).launch();
