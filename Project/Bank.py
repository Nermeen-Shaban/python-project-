import tkinter 
y=0
my_dict={"215321701332":{"Name":"Ahmed Abdelrazek Mohamed","Password":"1783","Balance" :3500166,"status":'0'},
"203659302214":{"Name":"Salma Mohamed Foaad","Password":"1390","Balance":520001,"status":'0'},
"126355700193":{"Name":"Adel Khaled Abdelrahman","Password":"1214","Balance":111000,"status":'0'},
"201455998011":{"Name":"Saeed Amin Elsawy","Password":"2001","Balance" :1200,"status":'0'},
"201122369851":{"Name":"Amir Salama Elgendy","Password":"8935","Balance":178933,"status":'0'},
"201356788002":{"Name":"Wael Mohamed khairy","Password" :"3420","Balance":55000,"status":'0'},
"203366789564":{"Name":"Mina Sameh Bishoy","Password":"1179","Balance":18000,"status":'0'},
"201236787812":{"Name":"Omnia Ahmed Awad","Password":"1430","Balance":180350,"status":'0'}}

window_var=tkinter.Tk()
window_var.title("main")
window_var.geometry("400x200")

label_AccountNum=tkinter.Label(window_var,text="Account Number")
label_AccountNum.place(x=0,y=20)

entry_user=tkinter.Entry(window_var)
entry_user.place(x=100,y=20)

label_Password=tkinter.Label(window_var,text="Password")
label_Password.place(x=0,y=70)
entry_Password=tkinter.Entry(window_var,show='*')
entry_Password.place(x=100,y=70)

x=my_dict.keys()
group1= tkinter.IntVar()
group2= tkinter.IntVar()

def login_func():
	global y,s
	if entry_user.get() in x and my_dict[entry_user.get()]["status"]=='0':
		if entry_Password.get() == my_dict[entry_user.get()]["Password"]:
			s=entry_user.get()
			Option()
		else :
			if (y==0 or y==1):
				label_try=tkinter.Label(window_var,text="Please Try again")
				label_try.place(x=150,y=120)
				label_try.after(1000, label_try.destroy)
				entry_Password.delete(0,'end')
				y=y+1
			elif (y==2):
				label_error=tkinter.Label(window_var,text="you try 3 times")
				label_error.place(x=150,y=140)
				label_error.after(2000, label_error.destroy)
				my_dict[entry_user.get()]["status"]='1'
				entry_Password.delete(0,'end')
				entry_user.delete(0,'end')
				y=y+1
				#label_Password.after(0, label_Password.destroy)
				#entry_Password.after(0,entry_Password.destroy)
				
	elif entry_user.get() in x and my_dict[entry_user.get()]["status"]=='1':
		label_Locked=tkinter.Label(window_var,text="This account is locked")
		label_Locked.place(x=150,y=150)
		label_Locked.after(1000, label_Locked.destroy)
		
		
	else :
		label_user=tkinter.Label(window_var,text="This account number is not identified !")
		label_user.place(x=150,y=150)
		label_user.after(1000, label_user.destroy)
		entry_user.delete(0,'end')
		entry_Password.delete(0,'end')
	

	
btn1=tkinter.Button(window_var,text='login',bg='blue',command=login_func)
btn1.place(x=90,y=100)

def Thanking_msg():
	global msg_var
	msg_var=tkinter.Toplevel()
	msg_var.title("Cash Withdraw")
	msg_var.geometry("200x200")
	label_msg=tkinter.Label(msg_var,text="Thank You")
	label_msg.place(x=0,y=20)
	btn_msg=tkinter.Button(msg_var,text='close',bg='red',command=msg_var.destroy)
	btn_msg.place(x=150,y=100)

def Calc_Balance():
	global entry_Cash
	global Cash_Withdraw_var
	global msg_var
	if (int(entry_Cash.get())<my_dict[s]["Balance"] and int(entry_Cash.get())<=5000):
		if (int(entry_Cash.get())%100==0):
			my_dict[s]["Balance"]=my_dict[s]["Balance"]-int(entry_Cash.get())
			print(my_dict[s]["Balance"])
			Thanking_msg()
			
		else :
			label_errormsg1=tkinter.Label(Cash_Withdraw_var,text="not allowed value")
			label_errormsg1.place(x=100,y=150)
			label_errormsg1.after(1000, label_errormsg1.destroy)
			entry_Cash.delete(0,'end')
			
	elif int(entry_Cash.get()) > 5000:
		label_errormsg2=tkinter.Label(Cash_Withdraw_var,text="Maximum allowed value per transaction is 5000 L.E")
		label_errormsg2.place(x=50,y=150)
		label_errormsg2.after(1000, label_errormsg2.destroy)
		entry_Cash.delete(0,'end')
		
	else :
		label_errormsg3=tkinter.Label(Cash_Withdraw_var,text="no sufficient balance")
		label_errormsg3.place(x=200,y=100)
		label_errormsg3.after(1000, label_errormsg3.destroy)
		entry_Cash.delete(0,'end')

def PassChange():
	global Password_Change_var
	global entry_PassChange
	global entry_PassChange
	
	
	if int(entry_PassChange.get()) >10000 or int(entry_PassChange2.get()) >10000:
		label_Error=tkinter.Label(Password_Change_var,text=" Error Must 4 digits only ")
		label_Error.place(x=100,y=110)
		label_Error.after(2000, label_Error.destroy)
		
		
	elif (int(entry_PassChange.get())==int(entry_PassChange2.get())):
		label_Done=tkinter.Label(Password_Change_var,text=" Done ")
		label_Done.place(x=100,y=110)
		label_Done.after(2000, label_Done.destroy)
		
	else :
		label_Error2=tkinter.Label(Password_Change_var,text=" Two Passwords Not Matched ")
		label_Error2.place(x=100,y=110)
		label_Error2.after(2000, label_Error2.destroy)
		entry_PassChange.delete(0,'end')
		entry_PassChange2.delete(0,'end')
	

def Rad_func():
	global entry_Cash
	global Cash_Withdraw_var
	global Password_Change_var
	global entry_PassChange
	global entry_PassChange2
	if group1.get() == 1:
		Cash_Withdraw_var=tkinter.Toplevel()
		Cash_Withdraw_var.title("Cash Withdraw")
		Cash_Withdraw_var.geometry("400x200")
		label_Cash=tkinter.Label(Cash_Withdraw_var,text="Enter desired amount to withdraw")
		label_Cash.place(x=0,y=20)
		entry_Cash=tkinter.Entry(Cash_Withdraw_var)
		entry_Cash.place(x=250,y=20)
		
		btnCash=tkinter.Button(Cash_Withdraw_var,text='OK',bg='blue',command=Calc_Balance)
		btnCash.place(x=300,y=100)
		
		
		
	elif group1.get() == 2:
		Balance_Inquiry_var=tkinter.Toplevel()
		Balance_Inquiry_var.title("Balance Inquiry")
		Balance_Inquiry_var.geometry("300x200")
		label_Inquiry=tkinter.Label(Balance_Inquiry_var,text=my_dict[s]["Name"])
		label_Inquiry.place(x=60,y=50)
		label_Inquiry=tkinter.Label(Balance_Inquiry_var,text=my_dict[s]["Balance"])
		label_Inquiry.place(x=100,y=100)
		btn_Inquiry=tkinter.Button(Balance_Inquiry_var,text='OK',bg='red',command=Balance_Inquiry_var.destroy)
		btn_Inquiry.place(x=150,y=150)
		
	elif group1.get() == 3:
		Password_Change_var=tkinter.Toplevel()
		Password_Change_var.title("Password Change")
		Password_Change_var.geometry("400x200")
		label_PassChange=tkinter.Label(Password_Change_var,text="Enter Password")
		label_PassChange.place(x=20,y=50)
		entry_PassChange=tkinter.Entry(Password_Change_var,show='*')
		entry_PassChange.place(x=170,y=50)
		label_PassChange2=tkinter.Label(Password_Change_var,text="Enter Password again")
		label_PassChange2.place(x=20,y=80)
		entry_PassChange2=tkinter.Entry(Password_Change_var,show='*')
		entry_PassChange2.place(x=170,y=80)
		btn_PassChange_ok=tkinter.Button(Password_Change_var,text='OK',bg='red',command=PassChange)
		btn_PassChange_ok.place(x=150,y=150)
		btn_PassChange_close=tkinter.Button(Password_Change_var,text='close',bg='red',command=Password_Change_var.destroy)
		btn_PassChange_close.place(x=200,y=150)
		
	elif group1.get()==4:
	
		Fawry_Service_var=tkinter.Toplevel()
		Fawry_Service_var.title("Fawry Options")
		Fawry_Service_var.geometry("600x400")

		Rad_Btn1 = tkinter.Radiobutton(Fawry_Service_var, text = "Orange Recharge", command =Fawry_Service, value = 1, variable = group2)
		Rad_Btn1.place(x=50,y=30)
	
		Rad_Btn2 = tkinter.Radiobutton(Fawry_Service_var, text = "Etisalat Recharge", command =Fawry_Service, value = 2, variable = group2)
		Rad_Btn2.place(x=50,y=60)
		
		Rad_Btn3 = tkinter.Radiobutton(Fawry_Service_var, text = "Vodafone Recharge", command =Fawry_Service, value = 3, variable = group2)
		Rad_Btn3.place(x=50,y=90)
		
		Rad_Btn3 = tkinter.Radiobutton(Fawry_Service_var, text = "We Recharge", command =Fawry_Service, value = 4, variable = group2)
		Rad_Btn3.place(x=50,y=120)
		
		Rad_Btn3 = tkinter.Radiobutton(Fawry_Service_var, text = "Exit", command = Fawry_Service_var.destroy, value = 5, variable = group2)
		Rad_Btn3.place(x=50,y=150)
		
	elif group1.get()==5:
		Exit()
		

def Check_Balance():
	global entry_AmountCharge
	global charging_var
	
	if (int(entry_AmountCharge.get())> my_dict[s]["Balance"]):
	
		label_Number=tkinter.Label(charging_var,text="no sufficient balance")
		label_Number.place(x=80,y=130)
		label_Number.after(2000, label_Number.destroy)
	
	else :
		my_dict[s]["Balance"]=my_dict[s]["Balance"]-int(entry_AmountCharge.get())
		label_Number=tkinter.Label(charging_var,text="Done")
		label_Number.place(x=80,y=130)
		label_Number.after(2000, label_Number.destroy)
	
def Fawry_Service():
	global entry_AmountCharge
	global charging_var
	charging_var=tkinter.Toplevel()
	charging_var.title("Fawry Options")
	charging_var.geometry("300x200")
	label_Number=tkinter.Label(charging_var,text="Enter Number")
	label_Number.place(x=20,y=50)
	entry_Number=tkinter.Entry(charging_var)
	entry_Number.place(x=150,y=50)
	label_AmountCharge=tkinter.Label(charging_var,text="Amount of Charge")
	label_AmountCharge.place(x=20,y=90)
	entry_AmountCharge=tkinter.Entry(charging_var)
	entry_AmountCharge.place(x=150,y=90)
	btn_Charge=tkinter.Button(charging_var,text='OK',bg='blue',command=Check_Balance)
	btn_Charge.place(x=200,y=150)
	btn_Charge=tkinter.Button(charging_var,text='Close',bg='red',command=charging_var.destroy)
	btn_Charge.place(x=250,y=150)

	


def Option():

	top_var=tkinter.Toplevel()
	top_var.title("Options")
	top_var.geometry("600x400")
	Rad_Btn11 = tkinter.Radiobutton(top_var, text = "Cash Withdraw", command = Rad_func, value = 1, variable = group1)
	Rad_Btn11.place(x=50,y=30)

	Rad_Btn12 = tkinter.Radiobutton(top_var, text = "Balance Inquiry", command = Rad_func, value = 2, variable = group1)
	Rad_Btn12.place(x=50,y=60)
	
	Rad_Btn12 = tkinter.Radiobutton(top_var, text = "Password Change", command = Rad_func, value = 3, variable = group1)
	Rad_Btn12.place(x=50,y=90)
	
	Rad_Btn12 = tkinter.Radiobutton(top_var, text = "Fawry Service", command = Rad_func, value = 4, variable = group1)
	Rad_Btn12.place(x=50,y=120)
	
	Rad_Btn12 = tkinter.Radiobutton(top_var, text = "Exit", command = top_var.destroy, value = 5, variable = group1)
	Rad_Btn12.place(x=50,y=150)

	

window_var.mainloop()