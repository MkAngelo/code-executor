
from distutils.cmd import Command
from django.shortcuts import render
import subprocess
from os import remove

def home(request):
    if request.method == "POST":
        #import pdb; pdb.set_trace()
        lang = request.POST['languages']
        source = request.POST['code']

        # Create a route
        name = "code." + lang
        route = "static/temp/"+name

        # Create a new file
        temp = open(route, "w")
        temp.write(source)
        temp.close()

        ans='' # Save the process

        # Execute
        if(lang == 'py'): 
            ans=subprocess.run(["python3", route], capture_output=True, text=True)
        elif(lang == 'java'): 
            ans=subprocess.run(["java", route], capture_output=True, text=True)
        elif(lang == 'c'): 
            compiler=subprocess.run(["gcc", route], capture_output=True, text=True)
            ans = subprocess.run(["./a.out"], capture_output=True, text=True)
        elif(lang == 'cpp'): 
            compiler=subprocess.run(["g++", route], capture_output=True, text=True)
            ans = subprocess.run(["./a.out"], capture_output=True, text=True)
        
        if ans.stderr:
            ans = "Upps... something was wrong"
        else:
            ans = ans.stdout
        
        context = {'ans': ans, 'text':source}  
        remove(route)
        
        return render(request, "index.html", context)
    return render(request, "index.html")