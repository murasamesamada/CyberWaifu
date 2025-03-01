import ctypes
from pathlib import Path
import tkinter as tk
import tkinter.messagebox as messagebox
import _thread
import configparser
import sys
import os

file_path = 'memory/小柔.csv'

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

WIDTH=680
HEIGHT=370
CONFIG_PATH = "config.ini"
modle=None

def Save():
    oid_model= config.get('LLM', 'model')
    oid_id= config.get('LLM_OpenAI', 'openai_key')
    oid_pw= config.get('LLM_Claude', 'user_oauth_token')
    oid_uid= config.get('LLM_Claude', 'bot_id')
    modle = oid_model.replace(oid_model, str(env.modls_input.get()))
    ids = oid_id.replace(oid_id, str(env.id_input.get()))    
    pws = oid_pw.replace(oid_pw, str(env.pw_input.get()))  
    uids = oid_uid.replace(oid_uid, str(env.uid_input.get()))  
    oid_username=config.get('CyberWaifu', 'username')
    usernames=oid_username.replace(oid_username, str(env.username_input.get())) 
    
    # 将修改后的账号列表保存到INI文件中
    config['LLM']['model'] = modle
    config['LLM_OpenAI']['openai_key'] = ids
    config['LLM_Claude']['user_oauth_token'] = pws
    config['LLM_Claude']['bot_id'] = uids
    config['CyberWaifu']['username'] = usernames

    oid_api=config.get('Thoughts_GoogleSerperAPI', 'api')
    apis=oid_api.replace(oid_api, str(env.api_input.get())) 
    config['Thoughts_GoogleSerperAPI']['api'] = apis
    oid_baidu_appid=config.get('Translate_Baidu', 'baidu_appid')
    baidu_appids=oid_baidu_appid.replace(oid_baidu_appid, str(env.baidu_appid_input.get())) 
    config['Translate_Baidu']['baidu_appid'] = baidu_appids
    oid_baidu_secretKey=config.get('Translate_Baidu', 'baidu_secretKey')
    baidu_secretKeys=oid_baidu_secretKey.replace(oid_baidu_secretKey, str(env.baidu_secretKey_input.get())) 
    config['Translate_Baidu']['baidu_secretKey'] = baidu_secretKeys
    oid_model=config.get('TTS_Vits', 'model')
    models=oid_model.replace(oid_model, str(env.model_input.get())) 
    config['TTS_Vits']['model'] = models
    oid_speaker=config.get('TTS_Vits', 'speaker')
    speakers=oid_speaker.replace(oid_speaker, str(env.speaker_input.get())) 
    config['TTS_Vits']['speaker'] = speakers
    oid_azure_speech_key=config.get('TTS_Edge', 'azure_speech_key')
    azure_speech_keys=oid_azure_speech_key.replace(oid_azure_speech_key, str(env.azure_speech_key_input.get())) 
    config['TTS_Edge']['azure_speech_key'] = azure_speech_keys
    oid_azure_region=config.get('TTS_Edge', 'azure_region')
    azure_regions=oid_azure_region.replace(oid_azure_region, str(env.azure_region_input.get())) 
    config['TTS_Edge']['azure_region'] = azure_regions    
    # 将修改后的INI文件写入磁盘中
    with open('config.ini', 'w',encoding='utf-8') as f:
        config.write(f)
    print("data save succsful!")

def Quit():
    sys.exit()
    
bhing=30
bhingj=bhing+30
class Maze(tk.Tk, object):
    def __init__(self):

        super(Maze, self).__init__()
        self.title('CyberWaifu GUI版 | 小璃雪特供嗷！')
        self.protocol("WM_DELETE_WINDOW", lambda: Quit())
        self._build_maze()
        self.Init_Home()
    
    def _build_maze(self):
        moni=ctypes.windll.user32
        global wt
        global ht
        wt=moni.GetSystemMetrics(0)
        ht=moni.GetSystemMetrics(1)
        self.geometry("{0}x{1}+{2}+{3}".format(WIDTH,HEIGHT,int((wt-WIDTH)/2),int((ht-HEIGHT)/2)))
        self.canvas = tk.Canvas(self,bg='pink',
                        height=HEIGHT,
                        width=WIDTH)
        global bk
        bk = tk.PhotoImage(file ="UI/2.png")
        image = self.canvas.create_image(WIDTH/2, HEIGHT/2, image=bk)
        self.canvas.pack()
    
    def Init_Home(self):
        '''
        # 创建选择框和拖拽功能
        self.selectbox = tk.Label(self, text="Select box:")
        self.selectbox.pack(side=tk.LEFT, padx=5)
        self.selectbox_var = tk.StringVar()
        self.selectbox_var.set("Select one")
        self.selectbox_entry = tk.Entry(self, textvariable=self.selectbox_var)
        self.selectbox_entry.pack(side=tk.LEFT)
            
        self.dragbox = tk.Label(self, text="Drag box:")
        self.dragbox.pack(side=tk.LEFT, padx=5)
        
        self.dragbox_var = tk.StringVar()
        self.dragbox_var.set("Drag me!")
        self.dragbox_entry = tk.Entry(self, textvariable=self.dragbox_var)
        self.dragbox_entry.pack(side=tk.LEFT)
        '''


        modls=config.get('LLM', 'model')
        id=config.get('LLM_OpenAI', 'openai_key')
        pw=config.get('LLM_Claude', 'user_oauth_token')
        uid=config.get('LLM_Claude', 'bot_id')
        modls_ = tk.StringVar()
        id_ = tk.StringVar()
        pw_ = tk.StringVar()
        uid_=tk.StringVar()
        modls_.set(str(modls))
        id_.set(str(id))
        pw_.set(str(pw))
        uid_.set(str(uid))
        self.modls_input=tk.Entry(self,textvariable=modls_)
        self.id_input=tk.Entry(self,textvariable=id_)
        self.pw_input=tk.Entry(self,textvariable=pw_)
        self.uid_input=tk.Entry(self,textvariable=uid_)
        self.modls_label=tk.Label(self,text="模式:")
        self.id_label=tk.Label(self,text="Openaikey:")
        self.pw_label=tk.Label(self,text="claude token:")
        self.uid_label=tk.Label(self,text="成员id")
        self.Launch=tk.Button(self,text="运行程序",command=self.Launch)
        self.Exit=tk.Button(self,text="退出程序",command=Quit)

        self.Exit.pack()
        self.Exit.place(x=300,y=250,width=100)
        self.modls_label.pack()
        self.modls_label.place(x=10,y=bhing,width=80)
        self.modls_input.pack()
        self.modls_input.place(x=90,y=bhing,width=150)
        self.id_label.pack()
        self.id_label.place(x=10,y=bhing+30,width=80)
        self.id_input.pack()
        self.id_input.place(x=90,y=bhing+30,width=400)
        self.pw_label.pack()
        self.pw_label.place(x=10,y=bhing+60,width=80)
        self.pw_input.pack()
        self.pw_input.place(x=90,y=bhing+60,width=400)
        self.uid_label.pack()
        self.uid_label.place(x=10,y=bhing+90,width=80)
        self.uid_input.pack()
        self.uid_input.place(x=90,y=bhing+90,width=100)
        self.Launch.pack()
        self.Launch.place(x=450,y=250,width=100)
        
        username=config.get('CyberWaifu', 'username')
        username_=tk.StringVar()
        username_.set(str(username))
        self.username_input=tk.Entry(self,textvariable=username_)
        self.username_label=tk.Label(self,text="对你的称呼:")
        self.username_label.pack()
        self.username_label.place(x=310,y=bhing,width=80)
        self.username_input.pack()
        self.username_input.place(x=390,y=bhing,width=100)

        api=config.get('Thoughts_GoogleSerperAPI', 'api')
        api_=tk.StringVar()
        api_.set(str(api))
        self.api_input=tk.Entry(self,textvariable=api_)
        self.api_label=tk.Label(self,text="谷歌联网api：")
        self.api_label.pack()
        self.api_label.place(x=10,y=bhing+120,width=80)
        self.api_input.pack()
        self.api_input.place(x=90,y=bhing+120,width=100)

        baidu_appid=config.get('Translate_Baidu', 'baidu_appid')
        baidu_appid_=tk.StringVar()
        baidu_appid_.set(str(baidu_appid))
        self.baidu_appid_input=tk.Entry(self,textvariable=baidu_appid_)
        self.baidu_appid_label=tk.Label(self,text="百度翻译id：")
        self.baidu_appid_label.pack()
        self.baidu_appid_label.place(x=10,y=bhing+150,width=80)
        self.baidu_appid_input.pack()
        self.baidu_appid_input.place(x=90,y=bhing+150,width=100)

        baidu_secretKey=config.get('Translate_Baidu', 'baidu_secretKey')
        baidu_secretKey_=tk.StringVar()
        baidu_secretKey_.set(str(baidu_secretKey))
        self.baidu_secretKey_input=tk.Entry(self,textvariable=baidu_secretKey_)
        self.baidu_secretKey_label=tk.Label(self,text="百度翻译Key：")
        self.baidu_secretKey_label.pack()
        self.baidu_secretKey_label.place(x=10,y=bhing+180,width=80)
        self.baidu_secretKey_input.pack()
        self.baidu_secretKey_input.place(x=90,y=bhing+180,width=100)
     
        model=config.get('TTS_Vits', 'model')
        model_=tk.StringVar()
        model_.set(str(model))
        self.model_input=tk.Entry(self,textvariable=model_)
        self.model_label=tk.Label(self,text="TTSvits模型：")
        self.model_label.pack()
        self.model_label.place(x=10,y=bhing+210,width=80)
        self.model_input.pack()
        self.model_input.place(x=90,y=bhing+210,width=100)  

        speaker=config.get('TTS_Vits', 'speaker')
        speaker_=tk.StringVar()
        speaker_.set(str(speaker))
        self.speaker_input=tk.Entry(self,textvariable=speaker_)
        self.speaker_label=tk.Label(self,text="TTSvits声线：")
        self.speaker_label.pack()
        self.speaker_label.place(x=10,y=bhing+240,width=80)
        self.speaker_input.pack()
        self.speaker_input.place(x=90,y=bhing+240,width=100)

        azure_speech_key=config.get('TTS_Edge', 'azure_speech_key')
        azure_speech_key_=tk.StringVar()
        azure_speech_key_.set(str(azure_speech_key))
        self.azure_speech_key_input=tk.Entry(self,textvariable=azure_speech_key_)
        self.azure_speech_key_label=tk.Label(self,text="azure key：")
        self.azure_speech_key_label.pack()
        self.azure_speech_key_label.place(x=10,y=bhing+270,width=80)
        self.azure_speech_key_input.pack()
        self.azure_speech_key_input.place(x=90,y=bhing+270,width=100)

        azure_region=config.get('TTS_Edge', 'azure_region')
        azure_region_=tk.StringVar()
        azure_region_.set(str(azure_region))
        self.azure_region_input=tk.Entry(self,textvariable=azure_region_)
        self.azure_region_label=tk.Label(self,text="azure region：")
        self.azure_region_label.pack()
        self.azure_region_label.place(x=10,y=bhing+300,width=80)
        self.azure_region_input.pack()
        self.azure_region_input.place(x=90,y=bhing+300,width=100)

    def Launch(self):
        check()
        init()
        Save()
        os.system('start cmd /K Python310\python.exe main.py')
        Quit()

def init():
    if os.path.exists(file_path):
        os.remove(file_path)
        print('rm succs')
    else:
        print('file dont found')

def check():#检查填写内容正确性
    if env.modls_input.get()!="OpenAI":
        if env.modls_input.get()!="Claude":
            messagebox.showinfo("模式错误", "模式只能填OpenAI或者Claude")
            Quit()
    else:
        pass
    if env.pw_input.get()== "" :
        pass
    else:
        if env.pw_input.get()[:4] != "xoxp":
            messagebox.showinfo("Claude token格式错误", "请检查claude user token填写是否正确")
            Quit()   
'''
def SelectBox(event):
    global selectbox_var, selectbox_entry
    selectbox_var.set("Select one")
    selectbox_entry.delete(0, "END") #清空当前文本框中的字符串。此处省略具体实现过程。
    
def DragBox(event):
    global dragbox_var, dragbox_entry
    dragbox_var.set("Drag me!")
    selectbox_entry.delete(0, "END") #清空当前文本框中的字符串。此处省略具体实现过程。
'''  
import os
if __name__=='__main__':
    env=Maze()
    env.mainloop()
