import win32com.client  # import win32com.client package to work with windows/microsoft application like outlook. Knowledge link- https://pbpython.com/windows-com.html

import re      # import re module to work with regular expression to search something in text.Knowledge link- https://www.w3schools.com/python/python_regex.asp

import time    # import time module to bring in sleep functionality to pause command execution.Knowledge Link-https://www.educative.io/edpresso/what-is-the-python-time-module?aid=5082902844932096&utm_source=google&utm_medium=cpc&utm_campaign=edpresso-dynamic&utm_term=&utm_campaign=Dynamic+-+Edpresso&utm_source=adwords&utm_medium=ppc&hsa_acc=5451446008&hsa_cam=8092184362&hsa_grp=86276435689&hsa_ad=397226000870&hsa_src=g&hsa_tgt=aud-475527062782:dsa-837376625453&hsa_kw=&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAjwlrqHBhByEiwAnLmYUEcYyzyk0DACD2iffzxGUqyljl7oeX-NbhxzoP8jRetMgytmJLHshxoCCpMQAvD_BwE

from datetime import datetime  # import datetime mode to compare time https://www.w3schools.com/python/python_datetime.asp



outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")   #open instance of outlook application

folder = outlook.Folders[0]   # selecting user account's folder

for x in range(len(folder.Folders)):  # len(folder.Folders) is the number of sub folders inside user account's folder
    
    Subfldr = folder.Folders[x]       # iterating to sub folders one by one
    
    #print(Subfldr)
    
    if Subfldr.name=='Salesforce':    # code when sub folder becomes folder of interest like Inbox or Sent or some other folder
        
        break
        
    else:
        
        pass
    


#declaring variables that will be searched in selected mail body later
    
customer_name='Test Client'   

severity='Severity : Major'

time_of_arrival=''

last_date_time_obj = datetime. strptime('2021-01-01 00:00:00','%Y-%m-%d %H:%M:%S')

#print(last_date_time_obj)



while True:   # below code will keep executing thereby enabling tracking of desired mail in desired outlook mail folder

        
        time.sleep(300)    # forcing continuous while loop to wait for 5min and then restart execution of codes inside while loop
    

        

        #find last message's body
    
    
        messages_REACH = Subfldr.Items

        message = messages_REACH.GetLast()

        msg_body=message.body


        

        # Find mail time


        pattern=r'[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]'  # for 2021-07-14 07:22:54

        match=re.search(pattern,msg_body)

        if match:

            time_of_arrival=match.group()

            

        

        #convert str formatted time to datetime object time
        
        date_time_str = time_of_arrival

        new_date_time_obj = datetime. strptime(date_time_str,'%Y-%m-%d %H:%M:%S')

        #print(new_date_time_obj)


        

        # Send mail to desired mail id when a particular mail arrives in the selected mail folder

        if new_date_time_obj > last_date_time_obj:
            
                #print("new mail")
                
                #print(customer_name)
                
                #print(severity)

                if customer_name in message.body and severity in message.body:

                    olMailItem = 0x0

                    obj = win32com.client.Dispatch("Outlook.Application")

                    mail = obj.CreateItem(olMailItem) # create a mail item like compose mail


                    # creating the mail

                    mail.To = 'test@test.com'
                    mail.Subject = 'Test'
                    #mail.HTMLBody = '<h3>This is HTML Body</h3>'
                    mail.Body = "This is a test message"
                    #mail.Attachments.Add('c:\\sample.xlsx')
                    #mail.Attachments.Add('c:\\sample2.xlsx')
                    mail.CC = 'test@test.com'

                    

                    #send mail

                    mail.Send()

                    #changing last mail time to old mail time

                    last_date_time_obj=new_date_time_obj
                    
                    

                    

                else:

                    pass