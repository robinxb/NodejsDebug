A simple plugin for sublime text2 to debug node file  in Chorme based browser.(os:**MacOS**)

I've port this to MacOS.
It works fine on my Mac OS X 10.9.1 with Sublime Text Build 3047.


### Requirements

* [nodeJS](http://github.com/ry/node) version >0.6.0 
* [npm](http://github.com/isaacs/npm)
* [node-inspector](https://github.com/dannycoates/node-inspector)
* Google Chrome

### Install 

1. install node-inspector (global mode) with npm

        $ npm install -g node-inspector
        
   ps: if you have trouble with  node-inspector when installing in  windowxp or window7, you can find answer in this link:
   http://stackoverflow.com/questions/11695739/installing-node-inspector-on-windows

2. download this plugin and unzip it . open the packages folder  by  clicking  the Preferences > Browser packages... entry in your sublime text2. then copy unziped folder in this folder. 

3. open  the  'nodejs_debug.sublime-settings'  file in plugin folder and set the parameter 'chrome_path' using your browser path!

4. Due to the limit of Python on MacOS, you **MUSH** do this before starting debug.

        sudo vim /path/to/node-inspector
    
    By default, the path is at `/usr/local/bin/node-inspector`.You can use `which node-inspector` to find the path.
    
    Replace the first line with 
    
        #!/usr/local/bin/node` 
    
    (the path to nodejs can be different on your Mac)

### Debugging

1. open a node.js file in sublime text 3

2. press ctrl+alt+b or click  item 'Nodejs Debug' on  contextmenu 

then you can debug your code in browser .
