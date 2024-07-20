from tkinter import *
import customtkinter
from tkinter import messagebox
#main frame
customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue")
Login_Page = customtkinter.CTk()
Login_Page.geometry("600x450")


#data bases
dataF=open("faculty_data.txt",'r+')
dataS=open("student_data(original).txt",'r+')
dataC=open("courses.txt",'r+')
infoHU=open("HU_grades.txt",'r+')
infoCS=open("CS_grades.txt",'r+')
infoMA=open("MA_grades.txt",'r+')
infoPH=open("PH_grades.txt",'r+')
dataS_L=dataS.read().split("\n")
dataF_L=dataF.read().split("\n")
dataC_L=dataC.read().split("\n")
infoHU_L=infoHU.read().split("\n")
infoCS_L=infoCS.read().split("\n")
infoMA_L=infoMA.read().split("\n")
infoPH_L=infoPH.read().split("\n")

# data from the files into python
Year=[]
GradesHU=[]
GradesMA=[]
GradesCS=[]
GradesPH=[]
Names=[]
Smails=[]
Fmails=[]
course=[]
Spasswords=[]
Fpasswords=[]
IDs=[]
IDf=[]
Sdigits=''
Fdigits=''
SID_cnt=-1
FID_cnt=0
for i in dataS_L:
    Sdigits=i.split(',')
    Names.append(Sdigits[0])
    IDs.append(Sdigits[1])
    Smails.append(Sdigits[2])
    Spasswords.append(Sdigits[3])
    Year.append(Sdigits[4])
    SID_cnt+=1
for a in infoCS_L:
    AinfoCS=a.split(',')
    GradesCS.append(AinfoCS[4])
for b in infoHU_L:
    BinfoHU=b.split(',')
    GradesHU.append(BinfoHU[4])
for c in infoPH_L:
    CinfoPH=c.split(',')
    GradesPH.append(CinfoPH[4])
for d in infoMA_L:
    DinfoMA=d.split(',')
    GradesMA.append(DinfoMA[4])
for j in dataF_L:
    Fdigits=j.split(',')
    IDf.append(Fdigits[1])
    Fmails.append(Fdigits[2])
    Fpasswords.append(Fdigits[3])
    course.append(Fdigits[5])
    FID_cnt+=1
# trial counter + new students/faculty tracker
trials=0
nextSID="S"
nextFID="F"


#main fonction
def login():
    global trials
    global nextSID
    global nextFID
    global choice
    global written_username
    global written_password
    written_username=username.get()
    written_password=password.get()
    tempID=""
    for k in written_username:
        if k in ['S','F']:
            continue
        else:
            tempID=tempID+k
    if written_username=='' or written_password=='':
        messagebox.showwarning(title="Error",message="Enter your username and password.")
    #Student page
    elif (written_username in IDs) and (written_password==Spasswords[int(tempID)]):
        Swindow=Toplevel(Login_Page)
        Swindow.geometry("1920x1080")
        Swindow.config(bg="#2b2b2b")
        label = customtkinter.CTkLabel(master=Swindow,text="✨ STUDENT PAGE ✨",font=("Arial",30))
        label.pack(pady=12,padx=10)
        def display():
            sdisplay_box.delete("1.0", "end")
            term=search_box.get()
            if term.lower() == "cs" or term.lower() == "computing":
                sdisplay_box.insert("end","Select an option from the report menu to display.")
            elif term.lower() == "ph" or term.lower() == "physics":
                sdisplay_box.insert("end","Select an option from the report menu to display.")
            elif term.lower() == "hu" or term.lower() == "humanities":
                sdisplay_box.insert("end","Select an option from the report menu to display.")
            elif term.lower() == "ma" or term.lower() == "calculus":
                sdisplay_box.insert("end","Select an option from the report menu to display.")
        display_B=customtkinter.CTkButton(master=Swindow ,text="Display",command=display)
        display_B.place(x=350,y=60)
        search_box= customtkinter.CTkEntry(master=Swindow,placeholder_text="Course Code / Name",width=300)
        search_box.place(x=40,y=60)
        sdisplay_box = customtkinter.CTkTextbox(master=Swindow,width=900,height=800,font=("Arial",22))
        sdisplay_box.place(x=40,y=100)
        cdisplay_box = customtkinter.CTkTextbox(master=Swindow,width=900,height=800,font=("Arial",22))
        cdisplay_box.place(x=980,y=100)
        ID=username.get()
        tempID=""
        for k in ID:
            if k=="S":
                continue
            else:
                tempID=tempID+k
        syear=dataS_L[int(tempID)]
        syear_L=syear.split(",")
        if syear_L[4]=="1":
            sdisplay_box.insert("end","You're a freshman in their first year")
        elif syear_L[4]=="2":
            sdisplay_box.insert("end","You're a sophomore in their second year")
        elif syear_L[4]=="3":
            sdisplay_box.insert("end","You're a junior in their third year")
        elif syear_L[4]=="4":
            sdisplay_box.insert("end","You're a senior in their fourth and last year")
        def optionmenu_stats(choice):
            term=search_box.get()
            if choice == "C-GPA":
                if term.lower() == "cs" or term.lower() == "computing":
                    sdisplay_box.delete("1.0", "end")
                elif term.lower() == "hu" or term.lower() == "humanities":
                    sdisplay_box.delete("1.0", "end")
                elif term.lower() == "ph" or term.lower() == "physics":
                    sdisplay_box.delete("1.0", "end")
                elif term.lower() == "ma" or term.lower() == "calculus":
                    sdisplay_box.delete("1.0", "end")
            elif choice == "Letter GPA":
                if term.lower() == "cs" or term.lower() == "computing":
                    sdisplay_box.delete("1.0", "end")
                elif term.lower() == "hu" or term.lower() == "humanities":
                    sdisplay_box.delete("1.0", "end")
                elif term.lower() == "ph" or term.lower() == "physics":
                    sdisplay_box.delete("1.0", "end")
                elif term.lower() == "ma" or term.lower() == "calculus":
                    sdisplay_box.delete("1.0", "end")
            elif choice == "Percentage":
                if term.lower() == "cs" or term.lower() == "commputing":
                    sdisplay_box.delete("1.0", "end")
                    sdisplay_box.insert("end","Your Percentage in the CS course is "+str(GradesCS[int(tempID)])+'%')
                elif term.lower() == "hu" or term.lower() == "humanities":
                    sdisplay_box.delete("1.0", "end")
                    sdisplay_box.insert("end","Your Percentage in the humanities course is "+str(GradesHU[int(tempID)])+'%')
                elif term.lower() == "ph" or term.lower() == "physics":
                    sdisplay_box.delete("1.0", "end")
                    sdisplay_box.insert("end","Your Percentage in the physics course is "+str(GradesPH[int(tempID)])+'%')
                elif term.lower() == "ma" or term.lower() == "calculus":
                    sdisplay_box.delete("1.0", "end")
                    sdisplay_box.insert("end","Your Percentage in the calculus course is "+str(GradesMA[int(tempID)])+'%')
            elif choice == "All":
                if term.lower() == "cs" or term.lower() == "commputing":
                    sdisplay_box.delete("1.0", "end")
                elif term.lower() == "hu" or term.lower() == "humanities":
                    sdisplay_box.delete("1.0", "end")
                elif term.lower() == "ph" or term.lower() == "physics":
                    sdisplay_box.delete("1.0", "end")
                elif term.lower() == "ma" or term.lower() == "calculus":
                    sdisplay_box.delete("1.0", "end")
        stats = customtkinter.CTkOptionMenu(master=Swindow,
                                       values=["C-GPA","Letter GPA","Percentage","All"],
                                       command=optionmenu_stats)
        stats.place(x=500, y=60)
        stats.set("REPORT CARD")
        label2 = customtkinter.CTkLabel(master=Swindow,text="✨AVAILIBALE COURSES✨",font=("Arial",30))
        label2.place(x=1250,y=60)
        for q in dataC_L:
            cdisplay_box.insert("end",q+'\n')

    #Faculty page
    elif (written_username in IDf) and (written_password==Fpasswords[int(tempID)-1]):
        Fwindow=Toplevel(Login_Page)
        Fwindow.geometry("1920x1080")
        Fwindow.config(bg="#2b2b2b")
        label = customtkinter.CTkLabel(master=Fwindow,text="✨ FACULTY PAGE ✨",font=("Arial",30))
        label.pack(pady=12,padx=10)
        def update():
            messagebox.showwarning(title="UPDATE",message="update successfull.")
            if written_username in ['F0001','F0002','F0003','F0004','F0005']:
                # Get the modified information from the search display box
                modified_info = display_box.get("1.0", "end")
                # Split the modified information into a list
                modified_info_list = modified_info.split(',')
                tempL=list(modified_info_list)
                tempv=''
                # Get the ID of the student or faculty member to be updated
                id_to_update = modified_info_list[1]
                # Find the index of the student or faculty member in the appropriate list
                if id_to_update in IDs:
                    # It's a student
                    for x in tempL[-1]:
                        if x !='\n':
                            tempv+=x
                    else:
                        modified_info_list[-1]=tempv
                index = IDs.index(id_to_update)
                data_list = infoCS_L
                # Update the appropriate data file with the modified information
                data_string = ','.join(modified_info_list)
                data_list[index] = data_string
                data_text = '\n'.join(data_list)
                infoCS.seek(0)
                infoCS.truncate()
                infoCS.write(data_text)
            elif written_username == 'F0006':
                # Get the modified information from the search display box
                modified_info = display_box.get("1.0", "end")
                # Split the modified information into a list
                modified_info_list = modified_info.split(',')
                tempL=list(modified_info_list)
                tempv=''
                # Get the ID of the student or faculty member to be updated
                id_to_update = modified_info_list[1]
                # Find the index of the student or faculty member in the appropriate list
                if id_to_update in IDs:
                    # It's a student
                    for x in tempL[-1]:
                        if x !='\n':
                            tempv+=x
                    else:
                        modified_info_list[-1]=tempv
                index = IDs.index(id_to_update)
                data_list = infoCS_L
                # Update the appropriate data file with the modified information
                data_string = ','.join(modified_info_list)
                data_list[index] = data_string
                data_text = '\n'.join(data_list)
                infoPH.seek(0)
                infoPH.truncate()
                infoPH.write(data_text)
            elif written_username == 'F0007':
                # Get the modified information from the search display box
                modified_info = display_box.get("1.0", "end")
                # Split the modified information into a list
                modified_info_list = modified_info.split(',')
                tempL=list(modified_info_list)
                tempv=''
                # Get the ID of the student or faculty member to be updated
                id_to_update = modified_info_list[1]
                # Find the index of the student or faculty member in the appropriate list
                if id_to_update in IDs:
                    # It's a student
                    for x in tempL[-1]:
                        if x !='\n':
                            tempv+=x
                    else:
                        modified_info_list[-1]=tempv
                index = IDs.index(id_to_update)
                data_list = infoCS_L
                # Update the appropriate data file with the modified information
                data_string = ','.join(modified_info_list)
                data_list[index] = data_string
                data_text = '\n'.join(data_list)
                infoHU.seek(0)
                infoHU.truncate()
                infoHU.write(data_text)
            elif written_username == 'F0008':
                # Get the modified information from the search display box
                modified_info = display_box.get("1.0", "end")
                # Split the modified information into a list
                modified_info_list = modified_info.split(',')
                tempL=list(modified_info_list)
                tempv=''
                # Get the ID of the student or faculty member to be updated
                id_to_update = modified_info_list[1]
                # Find the index of the student or faculty member in the appropriate list
                if id_to_update in IDs:
                    # It's a student
                    for x in tempL[-1]:
                        if x !='\n':
                            tempv+=x
                    else:
                        modified_info_list[-1]=tempv
                index = IDs.index(id_to_update)
                data_list = infoCS_L
                # Update the appropriate data file with the modified information
                data_string = ','.join(modified_info_list)
                data_list[index] = data_string
                data_text = '\n'.join(data_list)
                infoMA.seek(0)
                infoMA.truncate()
                infoMA.write(data_text)
        update_B=customtkinter.CTkButton(master=Fwindow ,text="UPDATE",command=update)
        update_B.place(x=500,y=60)
        def search_names_ids2(term):
            results = []
            # Search the names and IDs
            if written_username in ['F0001','F0002','F0003','F0004','F0005']:
                for name in infoCS_L:
                    if term in name:
                        results.append(name)
            elif written_username == 'F0006':
                for name in infoPH_L:
                    if term in name:
                        results.append(name)
            elif written_username == 'F0007':
                for name in infoHU_L:
                    if term in name:
                        results.append(name)
            elif written_username == 'F0008':
                for name in infoMA_L:
                    if term in name:
                        results.append(name)
            return results
        def search2():
            term = search_box.get()
            l_term = list(term)
            try:
                l_term[0]=l_term[0].upper()
                for i in range(len(l_term)):
                    if l_term[i] == " ":
                        l_term[i+1]=l_term[i+1].upper()
                    else:
                        continue
            except IndexError as error:
                error=messagebox.showerror(title="Error",message="Please enter an ID or name.")
            term_cap="".join(l_term)
            results = search_names_ids2(term_cap)
            display_box.delete("1.0", "end")
            for result in results:
                if result in results:
                    display_box.insert("end", result + "\n")
                    display_box.insert("end","\n")
            if results==[]:
                    display_box.insert("end","No such ID/Name was found in the data base...")
                    display_box.insert("end","\n")
                    display_box.insert("end","Please Try Again")
        search_B=customtkinter.CTkButton(master=Fwindow ,text="SEARCH",command=search2)
        search_B.place(x=350,y=60)
        search_box= customtkinter.CTkEntry(master=Fwindow,placeholder_text="ID number / Name",width=300)
        search_box.place(x=40,y=60)
        display_box = customtkinter.CTkTextbox(master=Fwindow,width=900,height=800,font=("Arial",22))
        display_box.place(x=40,y=100)
        def process(Range,ptype,interval1,interval2):
            fdisplay_box.delete("1.0","end")
            if written_username in ['F0001','F0002','F0003','F0004','F0005']:
                grade=''
                GL=[]
                for i in GradesCS:
                    for j in i:
                        if j in ['C','S',':']:
                            continue
                        else:
                            grade+=j
                    GL.append(int(grade))
                    grade=''
                for k in range(len(GL)):
                    if ptype == '<':
                        if GL[k] < int(interval1) :
                            fdisplay_box.insert("end", str(infoCS_L[k]) + "\n")
                            fdisplay_box.insert("end","\n")
                        else:
                            continue
                    elif ptype == '>':
                        if GL[k] > int(interval1):
                            fdisplay_box.insert("end",str(infoCS_L[k])+'\n')
                            fdisplay_box.insert("end","\n")
                        else:
                            continue
            elif written_username == 'F0006':
                grade=''
                GL=[]
                for i in GradesPH:
                    for j in i:
                        if j in ['P','H',':']:
                            continue
                        else:
                            grade+=j
                    GL.append(int(grade))
                    grade=''
                for k in range(len(GL)):
                    if ptype == '<':
                        if GL[k] < int(interval1) :
                            fdisplay_box.insert("end", str(infoPH_L[k]) + "\n")
                            fdisplay_box.insert("end","\n")
                        else:
                            continue
                    elif ptype == '>':
                        if GL[k] > int(interval1):
                            fdisplay_box.insert("end",str(infoPH_L[k])+'\n')
                            fdisplay_box.insert("end","\n")
                        else:
                            continue
            elif written_username == 'F0007':
                grade=''
                GL=[]
                for i in GradesHU:
                    for j in i:
                        if j in ['H','U',':']:
                            continue
                        else:
                            grade+=j
                    GL.append(int(grade))
                    grade=''
                for k in range(len(GL)):
                    if ptype == '<':
                        if GL[k] < int(interval1) :
                            fdisplay_box.insert("end", str(infoHU_L[k]) + "\n")
                            fdisplay_box.insert("end","\n")
                        else:
                            continue
                    elif ptype == '>':
                        if GL[k] > int(interval1):
                            fdisplay_box.insert("end",str(infoHU_L[k])+'\n')
                            fdisplay_box.insert("end","\n")
                        else:
                            continue
            elif written_username == 'F0008':
                grade=''
                GL=[]
                for i in GradesMA:
                    for j in i:
                        if j in ['M','A',':']:
                            continue
                        else:
                            grade+=j
                    GL.append(int(grade))
                    grade=''
                for k in range(len(GL)):
                    if ptype == '<':
                        if GL[k] < int(interval1) :
                            fdisplay_box.insert("end", str(infoMA_L[k]) + "\n")
                            fdisplay_box.insert("end","\n")
                        else:
                            continue
                    elif ptype == '>':
                        if GL[k] > int(interval1):
                            fdisplay_box.insert("end",str(infoMA_L[k])+'\n')
                            fdisplay_box.insert("end","\n")
                        else:
                            continue
                    elif ptype == '=':
                        if GL[k] == int(interval1):
                            fdisplay_box.insert("end",str(infoMA_L[k])+'\n')
                            fdisplay_box.insert("end","\n")
                        else:
                            continue
        def Sfilter():
            Range=filter_box.get()
            interval1=''
            interval2=''
            ptype=''
            for x in Range:
                if x in ['>','<','=']:
                    ptype+=x
                else:
                    interval1+=x
            process(Range,ptype,interval1,interval2)

        search_B2=customtkinter.CTkButton(master=Fwindow ,text="SEARCH",command=Sfilter,font=("Arial",20))
        search_B2.place(x=1290,y=60)
        filter_box= customtkinter.CTkEntry(master=Fwindow,placeholder_text="Custom students filter (ex:<X)",width=300)
        filter_box.place(x=980,y=60)
        fdisplay_box = customtkinter.CTkTextbox(master=Fwindow,width=900,height=800,font=("Arial",22))
        fdisplay_box.place(x=980,y=100)
        def optionmenu_stats(choice):
            fdisplay_box.delete("1.0","end")
            if choice=='Average':
                if written_username in ['F0001','F0002','F0003','F0004','F0005']:
                    grade=''
                    somme=0
                    total=0
                    for i in GradesCS:
                        for j in i:
                            if j in ['C','S',':']:
                                continue
                            else:
                                grade+=j
                        total+=1
                        somme+=int(grade)
                        grade=''
                    average=somme/total
                    average_ph=round(average,2)
                    fdisplay_box.insert("end", "The average is the CS course is :"+ str(average_ph) + "\n")
                elif written_username == 'F0006':
                    grade=''
                    somme=0
                    total=0
                    for i in GradesPH:
                        for j in i:
                            if j in ['P','H',':']:
                                continue
                            else:
                                grade+=j
                        total+=1
                        somme+=int(grade)
                        grade=''
                    average=somme/total
                    average_ph=round(average,2)
                    fdisplay_box.insert("end", "The average is the physics course is :"+ str(average_ph) + "\n")
                elif written_username == 'F0007':
                    grade=''
                    somme=0
                    total=0
                    for i in GradesHU:
                        for j in i:
                            if j in ['H','U',':']:
                                continue
                            else:
                                grade+=j
                        total+=1
                        somme+=int(grade)
                        grade=''
                    average=somme/total
                    average_hu=round(average,2)
                    fdisplay_box.insert("end", "THe average is the humanities course is :"+ str(average_hu) + "\n")
                elif written_username == 'F0008':
                    grade=''
                    somme=0
                    total=0
                    for i in GradesMA:
                        for j in i:
                            if j in ['M','A',':']:
                                continue
                            else:
                                grade+=j
                        total+=1
                        somme+=int(grade)
                        grade=''
                    average=somme/total
                    average_ma=round(average,2)
                    fdisplay_box.insert("end", "THe average is the calculus course is :"+ str(average_ma) + "\n")
            elif choice=='highest grade' or choice=='lowest grade':
                if written_username in ['F0001','F0002','F0003','F0004','F0005']:
                    grade=''
                    GL=[]
                    for i in GradesCS:
                        for j in i:
                            if j in ['C','S',':']:
                                continue
                            else:
                                grade+=j
                        GL.append(int(grade))
                        grade=''
                    if choice=='lowest grade':
                        fdisplay_box.insert("end", "The lowest grade in the CS course is :"+ str(min(GL)) + "\n")
                    elif choice=='highest grade':
                        fdisplay_box.insert("end", "THe highest grade in the CS course is :"+ str(max(GL)) + "\n")
                elif written_username == 'F0006':
                    grade=''
                    GL=[]
                    for i in GradesPH:
                        for j in i:
                            if j in ['P','H',':']:
                                continue
                            else:
                                grade+=j
                        GL.append(int(grade))
                        grade=''
                    if choice=='lowest grade':
                        fdisplay_box.insert("end", "The lowest grade in the physics course is :"+ str(min(GL)) + "\n")
                    elif choice=='highest grade':
                        fdisplay_box.insert("end", "THe highest grade in the physics course is :"+ str(max(GL)) + "\n")
                elif written_username == 'F0007':
                    grade=''
                    GL=[]
                    for i in GradesHU:
                        for j in i:
                            if j in ['H','U',':']:
                                continue
                            else:
                                grade+=j
                        GL.append(int(grade))
                        grade=''
                    if choice=='lowest grade':
                        fdisplay_box.insert("end", "The lowest grade in the humanities course is :"+ str(min(GL)) + "\n")
                    elif choice=='highest grade':
                        fdisplay_box.insert("end", "THe highest grade in the humanities course is :"+ str(max(GL)) + "\n")
                elif written_username == 'F0008':
                    grade=''
                    GL=[]
                    for i in GradesMA:
                        for j in i:
                            if j in ['M','A',':']:
                                continue
                            else:
                                grade+=j
                        GL.append(int(grade))
                        grade=''
                    if choice=='lowest grade':
                        fdisplay_box.insert("end", "The lowest grade in the calculus course is :"+ str(min(GL)) + "\n")
                    elif choice=='highest grade':
                        fdisplay_box.insert("end", "THe highest grade in the calculus course is :"+ str(max(GL)) + "\n")
            elif choice=='Failed students':
                if written_username in ['F0001','F0002','F0003','F0004','F0005']:
                    grade=''
                    GL=[]
                    Failed_L=[]
                    for i in GradesCS:
                        for j in i:
                            if j in ['C','S',':']:
                                continue
                            else:
                                grade+=j
                        GL.append(int(grade))
                        grade=''
                    for k in range(len(GL)):
                        if GL[k] < 60 :
                            fdisplay_box.insert("end", str(infoCS_L[k]) + "\n")
                            fdisplay_box.insert("end","\n")
                        else:
                            continue
                elif written_username == 'F0006':
                    grade=''
                    GL=[]
                    Failed_L=[]
                    for i in GradesPH:
                        for j in i:
                            if j in ['P','H',':']:
                                continue
                            else:
                                grade+=j
                        GL.append(int(grade))
                        grade=''
                    for k in range(len(GL)):
                        if GL[k] < 60 :
                            fdisplay_box.insert("end", str(infoPH_L[k]) + "\n")
                            fdisplay_box.insert("end","\n")
                        else:
                            continue
                elif written_username == 'F0007':
                    grade=''
                    GL=[]
                    Failed_L=[]
                    for i in GradesHU:
                        for j in i:
                            if j in ['H','U',':']:
                                continue
                            else:
                                grade+=j
                        GL.append(int(grade))
                        grade=''
                    for k in range(len(GL)):
                        if GL[k] < 60 :
                            fdisplay_box.insert("end", str(infoHU_L[k]) + "\n")
                            fdisplay_box.insert("end","\n")
                        else:
                            continue
                elif written_username == 'F0008':
                    grade=''
                    GL=[]
                    Failed_L=[]
                    for i in GradesMA:
                        for j in i:
                            if j in ['M','A',':']:
                                continue
                            else:
                                grade+=j
                        GL.append(int(grade))
                        grade=''
                    for k in range(len(GL)):
                        if GL[k] < 60 :
                            fdisplay_box.insert("end", str(infoMA_L[k]) + "\n")
                            fdisplay_box.insert("end","\n")
                        else:
                            continue
            elif choice=='regestered students':
                if written_username in ['F0001','F0002','F0003','F0004','F0005']:
                    for W in range(len(infoCS_L)):
                        fdisplay_box.insert("end", str(infoCS_L[W]) + "\n")
                        fdisplay_box.insert("end","\n")
                elif written_username == 'F0006':
                    for W in range(len(infoPH_L)):
                        fdisplay_box.insert("end", str(infoPH_L[W]) + "\n")
                        fdisplay_box.insert("end","\n")
                elif written_username == 'F0007':
                    for W in range(len(infoHU_L)):
                        fdisplay_box.insert("end", str(infoHU_L[W]) + "\n")
                        fdisplay_box.insert("end","\n")
                elif written_username == 'F0008':
                    for W in range(len(infoMA_L)):
                        fdisplay_box.insert("end", str(infoMA_L[W]) + "\n")
                        fdisplay_box.insert("end","\n")
        stats = customtkinter.CTkOptionMenu(master=Fwindow,
                                       values=["Average","highest grade","lowest grade","Failed students","regestered students"],
                                       command=optionmenu_stats)
        stats.place(x=1440, y=60)
        stats.set("Statistics")


    #Admin page
    elif (written_username == 'Admin') and (written_password=='Admin'):
        Awindow=Toplevel(Login_Page)
        Awindow.geometry("1920x1080")
        Awindow.config(bg="#2b2b2b")
        #entry boxes
        label = customtkinter.CTkLabel(master=Awindow,text="- Admin TERMINAL -",font=("Arial",30))
        label.pack(pady=12,padx=0)
        add_box= customtkinter.CTkEntry(master=Awindow,placeholder_text="Add new student or faculty member",font=("Arial",20),width=1080,height=50,)
        add_box.place(x=350,y=850)
        def save():
            # Get the modified information from the search display box
            new_info=add_box.get()
            # Split the modified information into a list
            L_new_info=new_info.split(',')
            # Get the ID type to process into which file the new data will be added
            id_type = L_new_info[1]
            # Find the index of the student or faculty member
            if id_type[0] == "S" :
                # It's a student
                dataS_L.append(','.join(L_new_info))
                dataS.write('\n' + ','.join(L_new_info))
            elif id_type[0] == "F":
                # It's a faculty member
                dataF_L.append(','.join(L_new_info))
                dataF.write('\n' + ','.join(L_new_info))
            messagebox.showwarning(title="success",message="The new data has been added successfully.")
        save_B=customtkinter.CTkButton(master=Awindow ,text="ADD",command=save,font=("Arial",20))
        save_B.place(x=350,y=910)
        def update():
            messagebox.showwarning(title="UPDATE",message="update successfull.")
            # Get the modified information from the search display box
            modified_info = display_box.get("1.0", "end")
            # Split the modified information into a list
            modified_info_list = modified_info.split(',')
            tempL=list(modified_info_list)
            tempv=''
            # Get the ID of the student or faculty member to be updated
            id_to_update = modified_info_list[1]
            # Find the index of the student or faculty member in the appropriate list
            if id_to_update in IDs:
                # It's a student
                for x in tempL[-1]:
                    if x !='\n':
                        tempv+=x
                    else:
                        modified_info_list[-1]=tempv
                index = IDs.index(id_to_update)
                data_list = dataS_L
            elif id_to_update in IDf:
                # It's a faculty member
                for x in tempL[-1]:
                    if x !='\n':
                        tempv+=x
                    else:
                        modified_info_list[-1]=tempv
                index = IDf.index(id_to_update)
                data_list = dataF_L
            # Update the appropriate data file with the modified information
            data_string = ','.join(modified_info_list)
            data_list[index] = data_string
            data_text = '\n'.join(data_list)
            if id_to_update in IDs:
                dataS.seek(0)
                dataS.truncate()
                dataS.write(data_text)
            else:
                dataF.seek(0)
                dataF.truncate()
                dataF.write(data_text)
            messagebox.showwarning(title="success",message="The data has been updated successfully.")
        update_B=customtkinter.CTkButton(master=Awindow ,text="UPDATE",command=update,font=("Arial",20))
        update_B.place(x=500,y=910)
        def delete():
            # Get the information to delete from the search display box
            info_delete=display_box.get("1.0","end")
            # Split the information into a list
            L_info_delete=info_delete.split(',')
            # Get the ID type to process to know from which file the data will be deleted
            id_type = L_info_delete[1]
            # Removes \n from the line
            tempd=''
            for x in L_info_delete[-1]:
                    if x !='\n':
                        tempd+=x
                    else:
                        continue
            L_info_delete[-1]=tempd
            L_info_delete2=','.join(L_info_delete)
            # Find the index of the student or faculty member
            if id_type[0] == "S" :
                data_list = dataS_L
                # It's a student
                for i in range(len(dataS_L)-1):
                    if dataS_L[i] == L_info_delete2:
                        del dataS_L[i]
                    elif dataS_L[i] != info_delete:
                        continue
                data_text = '\n'.join(dataS_L)
                dataS.seek(0)
                dataS.truncate()
                dataS.write(data_text)
            elif id_type[0] == "F":
                data_list = dataF_L
                # It's a faculty member
                for i in range(len(dataF_L)-1):
                    if dataF_L[i] == L_info_delete2:
                        del dataF_L[i]
                    elif dataF_L[i] != info_delete:
                        continue
                data_text = '\n'.join(dataF_L)
                dataF.seek(0)
                dataF.truncate()
                dataF.write(data_text)
            messagebox.showwarning(title="success",message="The data has been deleted successfully.")
        delete_B=customtkinter.CTkButton(master=Awindow ,text="DELETE",command=delete,font=("Arial",20))
        delete_B.place(x=650,y=910)
        def search_names_ids(term):
            results = []
            # Search the names and IDs for the search term
            for name in dataS_L:
                if term in name:
                    results.append(name)
            for name in dataF_L:
                if term in name:
                    results.append(name)
            return results
        def search():
            term = search_box.get()
            l_term = list(term)
            display_box.delete("1.0", "end")
            if term == "course":
                print(display_box.get("end"))

            try:
                l_term[0]=l_term[0].upper()
                for i in range(len(l_term)):
                    if l_term[i] == " ":
                        l_term[i+1]=l_term[i+1].upper()
                    else:
                        continue
                term_cap="".join(l_term)
                results = search_names_ids(term_cap)
                for result in results:
                    if result in results:
                        display_box.insert("end", result + "\n")
                        display_box.insert("end","\n")
                if results==[]:
                    display_box.insert("end","No such ID/Name was found in the data base...")
                    display_box.insert("end","\n")
                    display_box.insert("end","Please Try Again")
            except Exception as e:
                messagebox.showerror(title="Error",message="Please enter an ID or name.")
                display_box.delete("1.0", "end")
                display_box.insert("0.0","To add a new student or faculty member:"+'\n'+"     1-Get a new faculty or student ID from the drop down menu below."
                    +'\n'+"     2-Following our data base naming scheme type in the entry box down below the needed informations."
                    +'\n'+" -Naming schme :"+'\n'+'     First_Name Last_Name,New_ID,New_ID@gmail.com,EUI@New_ID,year,phone_number.'
                    +'\n'+"     * If you wish to add a new faculty member replace the year with the course taught abbreviation."
                    +'\n'+"\n"+"To delete a student or faculty member:"+'\n'+"    1-Search his/her ID or name (make sure only one result is shown)"
                    +'\n'+"     2-Press the delete button and restart the program."+'\n'+'\n'+"To add a course :"+'\n'+'     1-Type in the display box the course [name,code:(new line)course description]'
                +'\n'+'     2-Type in search bar:"course"')
        search_B=customtkinter.CTkButton(master=Awindow ,text="SEARCH",command=search,font=("Arial",20))
        search_B.place(x=660,y=50)
        search_box= customtkinter.CTkEntry(master=Awindow,placeholder_text="ID number / Name",width=300)
        search_box.place(x=350,y=50)
        display_box = customtkinter.CTkTextbox(master=Awindow,width=1080,height=750,font=("Arial",22))
        display_box.insert("0.0","To add a new student or faculty member:"+'\n'+"     1-Get a new faculty or student ID from the drop down menu below."
            +'\n'+"     2-Following our data base naming scheme type in the entry box down below the needed informations."
            +'\n'+" -Naming schme :"+'\n'+'     First_Name Last_Name,New_ID,New_ID@gmail.com,EUI@New_ID,year,phone_number.'
            +'\n'+"     * If you wish to add a new faculty member replace the year with the course taught abbreviation."
            +'\n'+"\n"+"To delete a student or faculty member:"+'\n'+"    1-Search his/her ID or name (make sure only one result is shown)"
            +'\n'+"     2-Press the delete button and restart the program."+'\n'+'\n'+"To add a course :"+'\n'+'     1-Type in the display box the course [name,code:(new line)course description]'
        +'\n'+'     2-Type in search bar:"course"')
        display_box.place(x=350,y=90)
        ID_textbox = customtkinter.CTkTextbox(Awindow,width=250,height=50)
        ID_textbox.insert("0.0","# To get a new ID choose a type from the drop down menu..")
        ID_textbox.place(x=950,y=910)
        def optionmenu_callback(choice):
            global FID_cnt
            global SID_cnt
            global nextSID
            global nextFID
            ID_textbox.delete("1.0", "end")
            if choice =='Faculty':
                if len(str(FID_cnt))==1:
                    nextFID+="000"+str(FID_cnt+1)
                elif len(str(FID_cnt))==2:
                    nextFID+="00"+str(FID_cnt+1)
                elif len(str(FID_cnt))==3:
                    nextFID+="0"+str(FID_cnt+1)
                elif len(str(FID_cnt))==4:
                    nextFID+=str(FID_cnt+1)
                ID_textbox.insert("0.0","The ID will be :"+f"{nextFID}")
                nextFID='F' 
            elif choice =='Student':
                if len(str(SID_cnt))==1:
                    nextSID+="000"+str(SID_cnt+1)
                elif len(str(SID_cnt))==2:
                    nextSID+="00"+str(SID_cnt+1)
                elif len(str(SID_cnt))==3:
                    nextSID+="0"+str(SID_cnt+1)
                elif len(str(SID_cnt))==4:
                    nextSID+=str(SID_cnt+1)
                ID_textbox.insert("0.0", "The ID will be :"+f"{nextSID}")
                nextSID='S'
        combobox = customtkinter.CTkOptionMenu(master=Awindow,
                                       values=["Student", "Faculty"],
                                       command=optionmenu_callback)
        combobox.place(x=800, y=910)
        combobox.set("ID type :")


    # Trials counter
    else:
        messagebox.showerror(title="Error",message="Your ID or password are not correct..")
        trials=trials+1
        if trials != 3:
            trials_label = customtkinter.CTkLabel(master=frame,text=f'You have {3-trials} trials left..')
            trials_label.place(x=175,y=210)
        if trials == 3:
            Login_B.destroy()
            locked_label = customtkinter.CTkLabel(master=frame,text="Your account is locked")
            locked_label.place(x=175,y=210)

#frame design
frame = customtkinter.CTkFrame(master=Login_Page)
frame.pack(pady=20,padx=60,fill="both",expand=True)
label = customtkinter.CTkLabel(master=frame,text="✨ Student Management System ✨",font=("Arial",20))
label.pack(pady=12,padx=10)
username= customtkinter.CTkEntry(master=frame,placeholder_text="ID number")
username.pack(pady=12,padx=10)
password= customtkinter.CTkEntry(master=frame,placeholder_text="password")
password.pack(pady=12,padx=10)
Login_B=customtkinter.CTkButton(master=frame , text="Login",command=login,font=("Arial",20), height=30, width=100, border_width=2, corner_radius=20)
Login_B.pack(pady=12,padx=10)
def exit():
    dataS.close()
    dataF.close()
    infoCS.close()
    infoHU.close()
    infoMA.close()
    infoPH.close()
    quit()
exit_button = customtkinter.CTkButton(master= frame,command= exit,text= "EXIT",text_color="white",hover= True,hover_color= "#e06a61",
    height=20,width= 30,border_width=0,corner_radius=20,border_color= "#2b2b2b", bg_color="#2b2b2b",fg_color= "#c75d55",font=("Arial",20))
exit_button.place(x= 350, y= 350)
#loops initiators
Login_Page.mainloop()
