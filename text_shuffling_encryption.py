from tkinter import *
import tkinter.messagebox as tmsg
import random
from os.path import exists
from tkinter import filedialog
import os
import threading
import time
import shutil


root = Tk()
title = 'Text Shuffling Encrypter'
root.title(title)
root.iconbitmap('icon.ico')

# Starting Operation
paths = os.getenv('APPDATA')
dirr = f'{paths}\\Text Shuffling Encrypter'
try:	
	os.mkdir(dirr)
except:
	pass

try:

	f = open(f'{dirr}\\data.dta','x')
	f.write('All Encrypted Files Data Saved Below')
	f.close()

except:

	pass

# Making Variables

lister = []

replaced = ""

final = ""

namee = ""

output4 = ""

from_to = []

final_text="" #Important

initial_text=''

times=[] #Important

is_file_saved = 0

save=None

open_it=None

my_backup = ""

files_to_backup = ""

true_list = []

total_files=0

multi_new_name = ""

multi_another_name = ""

errorlevel = 0

save_backup = None

decrypted_item = ""

decrypted_items_name = ""

file_is_saved = 'File Saved & Encrypted Successfully\nPlease, Do Not Change The File Name By Renaming It....'
text_warning = 'Your input must be at least 25 characters long. Please enter a longer text.'
about_text = '''
** INFORMATION **
Creator: Aaditya Kandel
Website: www.github.com/AadityaKandel
Contact: kandelaaditya11@gmail.com

Note: This Application Was Only Made For Testing Purposes
The Main Objective Of This Application Is To Help Encrypt 
Personal Data And Information That A User Wants To Protect
'''

help_text='''
This application functions similar to a notepad. Consider 
it as a digital notepad where you can type anything you 
want in the text area. It's recommended to type at least 
25 characters or more. Once you've entered your text, you
have multiple options to save the file:

* Press (Ctrl+S) to save the file.
* Click on "File" and choose either "Save" or "Save As" to perform the same action.

You don't need to worry about specifying a specific location
to save the file. Feel free to save it anywhere on your 
computer that you find convenient for future access.

The application encrypts the saved file, ensuring that only
this app can open it. If you attempt to open the encrypted
file using other text editors, such as Notepad, the content
will be unreadable. If you wish to backup all your encrypted
files at once, click on "Tools" and select "Backup". Additionally,
you have the option to clear all data associated with this
application by clicking on "Tools" and choosing "Clear Data"

Additionally, it also has two more features which allows the
user to "Multi Encrypt" and "Multi Decrypt". The Multi Encrypt
feature allows the user to select their multiple files which
they want to keep safe. After selecting the file, they are
asked to choose the folder where they'd like to save the 
encrypted files and then, the process begins and gets
completed. The user must know that they shouldn't change 
the location of their encrypted files. Likewise, the multi
decrypt feature allows the user to decrypt their multiple
files which were already encrypted. To use these features,
simply head to the Tools option and click either of the
features.
'''
backup_msg=f'''
- Number of files given for backup:978
- Number of files successfully backed up:9897
- Number of files with backup errors:876
'''

filetypes = [
    ("Text Files", "*.txt"),
    ("BATCH Files", "*.bat"),
    ("Python Files","*.py"),
    ("All Files", "*.*")
]

# Making Functions

def finder(name,give_me,another_please,called_from_or_not4):

	global lister,final,namee,output4,replaced,save,multi_another_name,multi_new_name

	while True:

		if os.path.exists(name) ==  True:

			i1 = name.rindex('.')
			i2 = name.rindex('\\')

			result1 = name[i2+1:i1] #try1

			namee = result1

			if result1[-1].isnumeric() == False:

				result1=result1+'0'

			else:

				pass

			length = len(result1)

			for i in range (0,length):

				if result1[i].isnumeric() == True:

					lister.append(i)

				else:

					pass


			for i in range(0, len(lister)):

				final = final+result1[lister[i]]

			output = int(final)+1
			output1 = namee[0:lister[0]]
			output2 = output1+str(output)
			output3 = output2+namee[i1::]
			output4 = name.replace(namee,output3) #Important

			lister = []
			final = ""
			name=output4

		else:

			i11 = name.rindex('.')
			last_words = name[i11::]
			replaced = name.replace(last_words,give_me)

			i22 = replaced.rindex('\\') #try1.et

			replaced_again = replaced[i22+1::] #try1.py

			i33 = another_please.rindex('/')
			i44 = another_please[i33+1::] #try.py

			finallyy = another_please.replace(i44,replaced_again)
			if called_from_or_not4 == True:
				multi_new_name=finallyy
				multi_another_name=replaced_again
			else:
				save=finallyy
			break

def search(called_from_or_not1):
	global save,times,multi_new_name,multi_another_name
	if called_from_or_not1 == True:
		indexx = multi_new_name.rindex('/')
		indexx1 = multi_new_name.rindex('.')
		new_save = multi_new_name[indexx+1:indexx1]
	else:
		indexx = save.rindex('/')
		indexx1 = save.rindex('.')
		new_save = save[indexx+1:indexx1]

	f = open(f"{dirr}\\{new_save}.et",'w')
	f.write(str(times))
	f.close()
	times = []

def check(called_from_or_not2):
	global save,times,multi_new_name,multi_another_name
	if called_from_or_not2 == True:
		indexx = multi_new_name.rindex('/')
		indexx1 = multi_new_name.rindex('.')
		new_save = multi_new_name[indexx+1:indexx1]

		extension = multi_new_name[indexx1::]

		multi_another_name=new_save+extension

		if os.path.exists(f"{dirr}\\{new_save}.et") ==  True:

			finder(f"{dirr}\\{new_save}.et",extension,multi_new_name,True)
			
		else:

			pass
	else:
		indexx = save.rindex('/')
		indexx1 = save.rindex('.')
		new_save = save[indexx+1:indexx1]

		extension = save[indexx1::]

		if os.path.exists(f"{dirr}\\{new_save}.et") ==  True:

			finder(f"{dirr}\\{new_save}.et",extension,save,False)
			
		else:

			pass

def saves(called_from_or_not3):
	global multi_new_name,multi_another_name
	f = open(f'{dirr}\\data.dta','a')
	if called_from_or_not3 == True:
		f.write(f'\n{open_it}/{multi_another_name}')
	else:
		f.write(f'\n{save}')
	f.close()

def encrypt(text):

	global final_text,times

	final_text=""

	times = []

	number = len(text)

	for i in range(0,number+1):

    
		from_to.append(i)

	text = text

	root.title('Encrypting Please Wait....')

	area.config(state=DISABLED)

	while True:

		ran = random.randint(0, number-1)

		if len(final_text) == number:

			# final_text==""
			break

		elif ran in times:

			pass

		else:

			final_text+=text[ran]
			times.append(ran)

		root.update()

	area.config(state=NORMAL)

def decrypt(from_backup_or_not):

	global initial_text,open_it,times,final_text,my_backup,files_to_backup,errorlevel,decrypted_item,decrypted_items_name

	initial_text=''
	final_text=""
	times=[]

	if from_backup_or_not == False:

		try:

			f = open(open_it,'r')
			read = f.read()
			f.close()
			index = open_it.rindex('/')
			index1 = open_it.rindex('.')
			new_name = save[index+1:index1]
			area.config(state=DISABLED)

		except:

			pass

	elif from_backup_or_not == True:

		try:

			f = open(files_to_backup,'r')
			read = f.read()
			f.close()

			index = files_to_backup.rindex('/')
			index1 = files_to_backup.rindex('.')
			new_name = files_to_backup[index+1:index1]

		except:

			pass

	elif from_backup_or_not == None:

		try:

			f = open(multi_new_name,'r')
			read = f.read()
			f.close()

			index = multi_new_name.rindex('/')
			index1 = multi_new_name.rindex('.')
			new_name = multi_new_name[index+1:index1]
			decrypted_items_name = multi_new_name[index+1::]

		except:

			pass

	try:
		f = open(f"{dirr}\\{new_name}.et",'r')
		times = eval(f.read())
		f.close()

		final_text = read

		initial_number=0

		if from_backup_or_not==False:
			root.title('Opening File....') 
		else:
			pass

		while True:

			if initial_number==len(final_text):

				if from_backup_or_not == False:

					area.config(state=NORMAL)
					area.delete(1.0,END)
					area.insert(1.0,initial_text)

				elif from_backup_or_not == True:

					my_backup = initial_text

				elif from_backup_or_not == None:

					decrypted_item=initial_text

				initial_text=''
				final_text=""
				times=[]
				break

			else:

				index_finder = times.index(initial_number)
				initial_text+=final_text[index_finder]
				initial_number=initial_number+1

			root.update()

	except:
		if from_backup_or_not == False:
			tmsg.showerror('Info','This File Was Not Made Using This Application\n(Decryption Failed)')
		else:
			pass

		errorlevel=errorlevel+1
		area.config(state=NORMAL)

def open_file():
	global open_it,save,is_file_saved,title,save_backup,errorlevel
	open_it = filedialog.askopenfilename(defaultextension=".txt",initialdir="Desktop",filetypes=filetypes,title="Choose The File That You've Already Encrypted")
	if open_it=="":

		tmsg.showerror('Error','File Cannot Be Found')

	else:

		save=open_it
		save_backup=save
		title=open_it+'-- Opened'
		decrypt(False)
		if errorlevel == 0:
			is_file_saved=1
			root.title(title)
		else:
			root.title('Text Shuffling Encryption [File Opening Failed]')
			errorlevel = 0

def save_file():

	global final_text, is_file_saved,save,title,save_backup
	text_content = area.get("1.0", "end-1c")

	if len(text_content) <25:

		tmsg.showwarning('Warning',text_warning)

	else:

		if is_file_saved == 0:

			save = filedialog.asksaveasfilename(defaultextension=".txt", initialdir="Desktop",filetypes=filetypes, title="Choose the location where you want to Encrypt & Save Your File")

			if save == "":

				tmsg.showerror('Error','Saving File Incomplete')

			else:

				is_file_saved=1
				save_backup=save
				encrypt(text_content)

				check(False)

				f = open(save,'w')
				f.write(final_text)
				f.close()

				search(False)

				saves(False)

				tmsg.showinfo('Info',file_is_saved)

				title = save+"-- Saved"
				root.title(title)

		elif is_file_saved==1:

			#Yes

			encrypt(text_content)

			try:
				f = open(save,'w')
			except:
				save=save_backup
				f = open(save,'w')

			f.write(final_text)
			f.close()

			search(False)

			title=save+"-- Updated Successfully"
			root.title(title)


def save_file_as():
	global save,is_file_saved,title,save_backup
	text_content = area.get("1.0", "end-1c")

	if len(text_content) <25:

		tmsg.showwarning('Warning',text_warning)

	else:

		save = filedialog.asksaveasfilename(defaultextension=".txt",initialdir="Desktop",filetypes=filetypes,title="Choose the location where you want to Encrypt & Save Your File")

		if save == "":

			tmsg.showerror('Error','Saving File Incomplete')

		else:

			encrypt(text_content)

			check(False)

			f = open(save,'w')
			f.write(final_text)
			f.close()

			search(False)
			is_file_saved = 1
			save_backup=save

			saves(False)
			tmsg.showinfo('Info',file_is_saved)

			title=save+'-- Saved'
			root.title(title)

def hotkeys(event):

	if event.keysym=="s" and event.state==4:
		save_file()

	elif event.keysym=="o" and event.state==4:
		open_file()

	else:
		root.title("Text Shuffling Encrypter")

def about():

	tmsg.showinfo('Info',about_text)

def help_me():

	tmsg.showinfo('How To Use?',help_text)

def backup():

	yes_no = tmsg.askquestion('QUESTION','Are You Sure To Backup All Your Files?')
	
	if yes_no=="yes":

		start_the_backup(False)

	else:

		pass


def start_the_backup(called_or_not):

	global total_files

	backup_root = Tk()
	backup_root.iconbitmap('icon.ico')
	if called_or_not == False:
		backup_root.title('Backup')
	elif called_or_not == True:
		backup_root.title('Clear Data')

	try:
		f = open(f'{dirr}\\data.dta','r')
		lines_read = [line.strip() for line in f.readlines()]
		total_files = len(lines_read)-1
		f.close()
	except:
		pass

	try:

		os.mkdir('BACKUP')

	except:

		pass

	def thread1():
		global total_files,files_to_backup,my_backup,true_list,errorlevel,backup_msg

		errorlevel=0
		
		l2.config(text="Finding Files....")
		time.sleep(1)
		l2.config(text=f"Files Found: ({total_files}/{total_files})")
		time.sleep(1)

		for i in range(1,total_files+1):

			status = f"Checking Files: ({i}/{total_files})"

			if os.path.exists(f'{lines_read[i]}') == True:

				l2.config(text=status)
				true_list.append(lines_read[i])
			
			else:

				l2.config(text=status)
				total_files=total_files-1

			backup_root.update()

		for i in range(0,total_files):

			try:

				files_to_backup=true_list[i]
				decrypt(True)
				backup_index = files_to_backup.rindex('/')
				f = open(f'BACKUP\\{files_to_backup[backup_index+1::]}','w')
				f.write(my_backup)
				f.close()
				status1 = f"\n[{files_to_backup[backup_index+1::]}] -- ({i+1}/{total_files})"
				my_backup=""
				l2.config(text=status1)

			except:

				pass

			backup_root.update()
		new_msg = backup_msg.replace('978',str(total_files)).replace('876',str(errorlevel))
		neww_msg = new_msg.replace('9897',str(total_files-errorlevel))

		if called_or_not == True:

			l1.config(text="DELETING FILES",fg="red")
			l2.config(text="Checking...")

			time.sleep(2)
			
			for i in range(0,total_files):

				status1 = f"Deleting ALL Files: ({i+1}/{total_files})"
				files_to_delete = true_list[i]
				try:
					os.remove(files_to_delete)
				except:
					pass
				l2.config(text=status1)

			l2.config(text="Clearing Encryption....")
			try:
				shutil.rmtree(f'{dirr}')
				os.mkdir(f'{dirr}')

			except:

				pass

			tmsg.showinfo('Info',"DATA CLEARING SUCCESSFUL... ALL FILES WERE ALSO BACKED UP AUTOMATICALLY\nHere's The BackUp Detail"+neww_msg)

		else:

			tmsg.showinfo('Info',"*** BACKUP SUCCESSFUL ***"+neww_msg)

		backup_root.destroy()

	l1 = Label(backup_root,text="BACKING UP ALL FILES",font="arial 12 bold",bg="white",fg="green")
	l1.pack()
	l2 = Label(backup_root,text="",font="comicsansms 12 italic",bg="white",fg="green")
	l2.pack()

	backup_root.config(bg="white")

	t1 = threading.Thread(target=thread1)
	t1.start()

	backup_root.mainloop()

def clear_all():

	yes_no = tmsg.askquestion('QUESTION','Do You Really Want To Clear All Data?')
	
	if yes_no == "yes":
		
		start_the_backup(True)
	
	elif yes_no == "no":
		pass

def multi_encrypt():

	global save,open_it

	tmsg.showinfo('Info','Multi Encrypt Means To Select Multiple Files That You Want To Encrypt All At Once')
	save = filedialog.askopenfilenames(initialdir='Desktop',defaultextension=".txt",filetypes=filetypes,title="Choose Multiple Files That You Want To Encrypt")

	if save == "":

		tmsg.showerror('Error','No Files Were Selected')

	else:

		tmsg.showinfo('Info','Now, You Should Select The Location Where You Want To Save Your Encrypted Files')
		open_it = filedialog.askdirectory(initialdir="Desktop",title="Choose The Folder Where You Want To Save Your Encrypted Files")

		if open_it == "":
			tmsg.showerror('Error','Location Was Not Given')

		else:

			try:
				os.mkdir('Encrypted Files')
			except:
				pass

			multi_root = Tk()
			multi_root.iconbitmap('icon.ico')
			multi_root.title('Multi Encrypt')

			def multi_function():

				time.sleep(1)

				global multi_new_name,multi_another_name,save

				for i in range(0, len(save)):

					# l1.config(text=f"Encrypting File ({i}/{len(save)})")
					multi_new_name = save[i]
					f = open(multi_new_name,'r')
					multi_read = f.read()
					f.close()

					try:
						encrypt(multi_read)
					except:
						pass
					check(True)
					search(True)
					saves(True)

					f = open(f'{open_it}/{multi_another_name}','w')
					l2.config(text=f'[{multi_another_name}] -- ({i}/{len(save)})')
					f.write(final_text)
					f.close()

				tmsg.showinfo('Info',f'All {len(save)} Files Are Successfully Encrypted')
				root.title('Text Shuffling Encrypter')
				multi_root.destroy()

			l1 = Label(multi_root,text="Encrypting Files",font="arial 12 bold",fg="red")
			l1.pack()
			l2 = Label(multi_root,text="",font="comicsansms 12 italic",fg="red")
			l2.pack()
			t1 = threading.Thread(target=multi_function)
			t1.start()

			multi_root.mainloop()

def multi_decrypt():
	global save,open_it

	tmsg.showinfo('Info','Multi Decrypt Means To Select Multiple Files That You Want To Decrypt All At Once\n\
Remember That It Only Works For The Files That You Have Already Encrypted')

	save = filedialog.askopenfilenames(initialdir='Desktop',defaultextension=".txt",filetypes=filetypes,title="Choose Your Multiple Files That Were Already Encrypted")

	if save == "":

		tmsg.showerror('Error','No Files Were Selected')

	else:

		tmsg.showinfo('Info','Now, You Should Select The Location Where You Want To Save Your Decrypted Files')
		open_it = filedialog.askdirectory(initialdir="Desktop",title="Choose The Location Where You Want To Save Your Decrypted Files")

		if open_it == "":
			tmsg.showerror('Error','Location Was Not Given')

		else:
			
			multi_decrypt_root = Tk()
			multi_decrypt_root.title('Multi Decrypt')
			multi_decrypt_root.iconbitmap('icon.ico')

			def multi_decrypt_function():

				global multi_new_name,save,errorlevel,decrypted_item,decrypted_items_name

				errorlevel=0

				for i in range(0, len(save)):

					l2.config(text=f"\n[{decrypted_items_name}] -- ({i}/{len(save)})")
					multi_new_name = save[i]
					decrypt(None)
					f = open(f'{open_it}/{decrypted_items_name}','w')
					f.write(decrypted_item)
					f.close()

				tmsg.showinfo('Info',f'Total Files To Decrypt:{len(save)}\nSuccessfully Decrypted Files: {len(save)-errorlevel}\nError:{errorlevel}')
				multi_decrypt_root.destroy()

			l1 = Label(multi_decrypt_root,text="Decrypting Files",font="arial 12 bold",fg="green")
			l1.pack()

			l2 = Label(multi_decrypt_root,text="",font='comicsansms 12 italic',fg="green")
			l2.pack()

			t1 = threading.Thread(target=multi_decrypt_function)
			t1.start()

			multi_decrypt_root.mainloop()

def count_it():

	try:
		total_errors=0
		f = open(f'{dirr}\\data.dta','r')
		total_number = [line.strip() for line in f.readlines()]
		total_len = len(total_number)
		f.close()
		if total_len <=1:
			tmsg.showinfo('Info','No Files Were Encrypted')
		else:
			for i in range(1,len(total_number)):
				if os.path.exists(total_number[i]) == True:
					pass
				else:
					total_errors=total_errors+1

			tmsg.showinfo('Status',f'Total Encrypted Files: {total_len-1}\nTotal Files Active: {(total_len-1)-total_errors}\nFiles Not Found: {total_errors}')
	except:

		tmsg.showinfo('Info','No Files Were Encrypted')

#papoopaksjadf

# Create a menu bar
menu_bar = Menu(root)

# Make a sub Menu For File
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open [Encrypted]", command=open_file)
file_menu.add_command(label="Save [Encrypted]", command=save_file)
file_menu.add_command(label="Save As [Encrypted]", command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Make a sub Menu For Tools
tool_menu = Menu(menu_bar, tearoff=0)
tool_menu.add_command(label="Backup",command=backup)
tool_menu.add_command(label="Clear Data",command=clear_all)
tool_menu.add_command(label="Files Status",command=count_it)
tool_menu.add_separator()
tool_menu.add_command(label="Multi Encrypt",command=multi_encrypt)
tool_menu.add_command(label="Multi Decrypt",command=multi_decrypt)

# Make a sub Menu For Help
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About",command=about)
help_menu.add_command(label="How To Use?",command=help_me)

# Make The Main Menu Called "File"
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Tools",menu=tool_menu)
menu_bar.add_cascade(label="Help",menu=help_menu)

area = Text(height=30,width=80, wrap=NONE)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=area.yview)

scrollbar1 = Scrollbar(root, orient=HORIZONTAL)
scrollbar1.pack(side=BOTTOM, fill=X)
scrollbar1.config(command=area.xview)

area.pack(fill=BOTH, side=LEFT, expand=True)
area.config(yscrollcommand=scrollbar.set)
area.config(xscrollcommand=scrollbar1.set)

root.config(bg="white", menu=menu_bar)

root.bind('<Key>',hotkeys)
root.mainloop()