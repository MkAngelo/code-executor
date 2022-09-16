
from django.shortcuts import render
import subprocess
from os import remove

def home(request):
    if request.method == "POST":
        #import pdb; pdb.set_trace()
        lang = request.POST['languages']
        source = request.POST['code']
        name = "code." + lang
        route = "static/temp/"+name
        temp = open(route, "w")
        temp.write(source)
        temp.close()

        ans=''
        if(lang == 'py'): ans=subprocess.run(["python3", route], capture_output=True, text=True)
        # elif(lang == 'c'): subprocess.run(["gcc",route])
        # elif(lang == 'cpp'): subprocess.run([])
        # elif(lang == 'java'): subprocess.run([])
        
        if ans.stderr:
            # print("Stderr:", ans.stderr)
            ans = "Upps... something was wrong"
        else:
            ans = ans.stdout
        
        context = {'ans': ans}  
        remove(route)
        return render(request, "index.html", context)
    return render(request, "index.html")