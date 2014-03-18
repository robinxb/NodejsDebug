from subprocess import Popen
import re
import sublime, sublime_plugin
import webbrowser
import subprocess  
 
SETTINGS_FILE = "nodejs_debug.sublime-settings"
config = sublime.load_settings(SETTINGS_FILE)
chrome_path = config.get('chrome_path',"")
nodejs_path = config.get('nodejs_path',"")
inspector_path = config.get('inspector',"")
debug_port = config.get('debug_port',"")
web_port = config.get('web_port',"")


class NodejsDebugCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sublime.set_timeout(self.launch, 100)
 
  def launch(self):

    window = sublime.active_window()
    window.run_command('save')

    regx = re.compile(" ")
    cmd = nodejs_path +" --debug-brk=%d "%(debug_port) + regx.sub("\ ", self.view.file_name());
    cmd2 = inspector_path + " --web-port=%s --debug-port=%s"%(web_port, debug_port) 
    Popen(cmd, shell = True) 
    Popen(inspector_path, shell = True)
    sublime.set_timeout(self.openChrome,300)
  

  def openChrome(self):
      
    url = "http://localhost:%d/debug?port=%d"%(web_port, debug_port)
    cmd = "/usr/bin/open " + chrome_path + url
    print(cmd)
    subprocess.Popen("/usr/bin/open " + url, shell = True) 
 
