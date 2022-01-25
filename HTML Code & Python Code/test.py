from flask import Flask,render_template,redirect,url_for,request,flash
from flask_mail import Mail, Message
import mysql.connector
import webbrowser
import random
import datetime
import time
import os

app=Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'hk8084262@gmail.com'
app.config['MAIL_PASSWORD'] = 'Password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

global Pnr
Pnr=random.randint(1000000000,9999999999)
global trans_no
trans_no=random.randint(1000000000,9999999999)

app.secret_key = 'random '
db=mysql.connector.connect(host='localhost',user='root',passwd='user',database='railway')
con=db.cursor()
current_date=time.strftime('%Y-%m-%d')


@app.route("/mail")
def index():
   msg = Message('Hello', sender = 'hk8084262@gmail.com', recipients = ['hk2152573@gmail.com'])
   msg.body = "This is the email body"
   mail.send(msg)
   return "Sent"

@app.route('/',methods=['GET','POST'])
def first():
      error=None
      if request.method=='POST':
            user=request.form.get('pass')
            user1=request.form.get('email')
            con.execute('select * from login')
            res=con.fetchall()
            for i in range(0,len(res)):
                  global USER
                  USER=res[i][0]
                  PASS=res[i][1]
                  if USER==user1 and PASS==user:
                        global name
                        name=res[i][2]
                        return redirect(url_for('info',user=res[i][2],usname=USER))

                        break
                  elif res[i][0]!=user and res[i][1]!=user1:
                        continue
            else:
                  error='invalid delails'
      return render_template('index.html',error=error)

@app.route('/create-account',methods=['GET','POST'])
def create():
      return render_template('create_account.html')
@app.route('/create-account/final',methods=['GET','POST'])
def crt_final():
   if request.method=='POST':
            user=request.form.get('user')
            name=request.form.get('name')
            pswd=request.form.get('pass')
            mail=request.form.get('mail')
            dob=request.form.get('date')
            gen=request.form.get('gen')
            mobile=request.form.get('mobile')
            con.execute(f'insert into login values("{user}","{pswd}","{name}","{mail}","{mobile}","{gen}")')
            db.commit()
            return redirect(url_for('first'))
   return render_template('create_account.html')
@app.route('/forgort',methods=['GET','POST'])
def forgort():
      return render_template('forgot.html')

@app.route('/rail',methods=['GET','POST'])
def start():
      return render_template('rail.html')

@app.route('/rail/info',methods=['GET','POST'])
def info():
      action='alert("Please select any train")'
      select=request.form.get('example')
      FROM=request.form.get('From')
      TO=request.form.get('To')
      usnm=request.args.get('user')
      con.execute('use railway')
      con.execute(f'select * from rail where START="{FROM}" and END="{TO}"')
      res=con.fetchall()
      if request.method=='POST':
            error=None
            date=request.form.get('dat')
            if date < current_date:
                  error='please enter valid date'
            if res== []:
                  error='No train founded'
            return render_template('train_detail1.html',action=action,user=USER,products=res,len_prod=len(res),error=error,lght=len(res),From=FROM,To=TO)
      return render_template('rail.html',user=request.args.get('user'),userNM=request.args.get('usname'))

@app.route('/rail/info/main',methods=['GET','POST'])
def rail():
      error=None
      DATE=request.form.get('DATE')
      dat=DATE
      TNUM=request.form.get('TR_NO')
      FROM=request.form.get('from')
      TO=request.form.get('to')
      
      CLS=request.form.get('example')
      cls=CLS
            
      fro=FROM
      to=TO
      user=request.form.get('user')
      
      con.execute(f'select train_name from rail where train_no ="{TNUM}"')
      re=con.fetchone()

      con.execute(f'select * from rail where START="{FROM}" and END="{TO}"')
      res=con.fetchall()
      
      length=request.form.get('length')
      l=[]

      for x in range(0,int(length)):
            opt=request.form.get(f'option{x+1}')
            l.append(opt)
      for c in l:
            if c=='on':
                  L=res[l.index(c)]
      MN=list(L).copy()
      if dat < current_date:
            error='Invalid date'
      
      if request.method=='POST':
            return render_template('ticket_booking.html',user=USER,error=error,tr_nm=MN[5],tr_no=MN[4],cls=CLS,date=DATE,from_code=MN[1],to_code=MN[3])
      return render_template('train_detail1.html')

@app.route('/rail/info/main/confirm',methods=['GET','POST'])
def confirm():
      error=None
      user=request.form.get('user')
      fro=request.form.get('fro')
      to=request.form.get('to')
      cls=request.form.get('clas')
      tr_no=request.form.get('trno')
      con.execute(f'select train_name from rail where train_no="{tr_no}"')
      re=con.fetchall()
      tr_nm=re[0][0]
      date=request.form.get('dat')
      train_list=[tr_nm,date,cls,fro,to,tr_no]
      
      if  request.method=='POST':
            clas=request.form.get('clas')
            dat=request.form.get('dat')
            to=request.form.get('to')
            trno=request.form.get('trno')
            tr_name=request.form.get('trn')
            if clas=='Sleeper':
                  ticket_fare=200
            elif clas=='3-AC':
                  ticket_fare=300
            elif clas=='2-AC':
                  ticket_fare=500
            elif clas=='First_Class':
                  ticket_fare=700
            name1=request.form['name1'].capitalize()
            age1=request.form['age1']
            gen1=request.form.get('gen1')
            berth1=request.form.get('berth1')
            fod1=request.form.get('fod1')

            name2=request.form['name2'].capitalize()
            age2=request.form['age2']
            gen2=request.form.get('gen2')
            berth2=request.form.get('berth2')
            fod2=request.form.get('fod2')

            name3=request.form['name3'].capitalize()
            age3=request.form['age3']
            gen3=request.form.get('gen3')
            berth3=request.form.get('berth3')
            fod3=request.form.get('fod3')

            name4=request.form['name4'].capitalize()
            age4=request.form['age4']
            gen4=request.form.get('gen4')
            berth4=request.form.get('berth4')
            fod4=request.form.get('fod4')
            
            name5=request.form['name5'].capitalize()
            age5=request.form['age5']
            gen5=request.form.get('gen5')
            berth5=request.form.get('berth5')
            fod5=request.form.get('fod5')

            name6=request.form['name6'].capitalize()
            age6=request.form['age6']
            gen6=request.form.get('gen6')
            berth6=request.form.get('berth6')
            fod6=request.form.get('fod6')

            main_cn=request.form.get('main_cnc')
            alt_cn=request.form.get('alt_cnc')
            LMain=[[name1,age1,gen1,berth1,fod1],[name2,age2,gen2,berth2,fod2],[name3,age3,gen3,berth3,fod3],[name4,age4,gen4,berth4,fod4],[name5,age5,gen5,berth5,fod5],[name6,age6,gen6,berth6,fod6]]
            global LMAIN
            LMAIN=[]
            for d in LMain:
                  if d != ['','','Select','Choose Berth','Select']:
                        LMAIN.append(d)
            total=ticket_fare*(len(LMAIN))+80
            if LMAIN==[]:
                  error='Go Back and fill passenger detail first'
            user=request.form.get('user')
            return render_template('transaction_page.html',error=error,total=total,MAIN=LMAIN,len_x=len(LMAIN),main_cnc=main_cn,alt_cnc=alt_cn,lst=train_list,cls=clas,date=dat,from_code=fro,to_code=to,tr_no=trno,aval='CNF Confirm',tik_fare=ticket_fare,srv=80,tot=total,mob_main=main_cn,brth1=berth1,brth2=berth2,brth3=berth3,brth4=berth4,brth5=berth5,brth6=berth6)
      return render_template('ticket_booking.html')                                                                                                                     
@app.route('/rail/info/main/confirm/final',methods=['GET','POST'])
def final():
      tr_no=request.form.get('trno')
      fro=(request.form.get('fro')).capitalize()
      to=(request.form.get('to')).capitalize()

      con.execute(f'SELECT FROM_CODE,TO_CODE FROM RAIL WHERE TRAIN_NO={tr_no}')
      detail=con.fetchall()
      
      user=request.form.get('user')
      
      clas=request.form.get('clas')
      dat=request.form.get('dat')
      sno=request.form.get('LEN')
      
      trans_fst=['AA','AB','BB','BC','CB','CC','VC','DC','MK','LM','GH','SW']
      e=random.randint(0,11)
      trans_id=trans_fst[e]+str(trans_no)

      con.execute(f'select train_name from rail where train_no="{tr_no}"')
      tr_nm=con.fetchone()
      train_name=tr_nm[0]
      
      berth1=request.form.get('brth1')

      berth2=request.form.get('brth2')

      berth3=request.form.get('brth3')
      
      berth4=request.form.get('brth4')
      
      berth5=request.form.get('brth5')
      
      berth6=request.form.get('brth6')
      
      LBerth=[berth1,berth2,berth3,berth4,berth5,berth6]
      brth=''
      for j in LBerth:
            if j !='Choose Berth':
                  brth+=j+','

      berth=['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5','C1','C2','C3','C4','C5','D1','D2','D3','D4','D4']
     
      if clas =='Sleeper':
            Class='SL'
            w=random.randint(14,19)
            seat=random.randint(77,100)
      elif clas =='3-AC':
            Class='3-AC'
            w=random.randint(10,14)
            seat=random.randint(51,76)
      elif clas =='2-AC':
            Class='2-AC'
            w=random.randint(4,9)
            seat=random.randint(26,50)
      elif clas =='First_Class':
            Class='FC'
            seat=random.randint(0,25)
            w=random.randint(0,4)
      SEAT=''
      
      len_main=len(LMAIN)
      coach=berth[w]

      for c in range(0,len_main):
            LMAIN[c].append(berth[w])
            LMAIN[c].append(f'{seat}({LMAIN[c][5]})')
            SEAT+=str(seat)+','
            seat+=1
      Name=''
      Age=''
      Gen=''
      Berth=''
      Food=''
      
      for c in range(0,len(LMAIN)):
            Name+=LMAIN[c][0]+','

      for c in range(0,len(LMAIN)):
            Age+=LMAIN[c][1]+','

      for c in range(0,len(LMAIN)):
            Gen+=LMAIN[c][2]+','

      for c in range(0,len(LMAIN)):
            Berth+=LMAIN[c][3]+','

      for c in range(0,len(LMAIN)):
            Food+=LMAIN[c][4]+','
            
      for c in range(0,len(LMAIN)):
            LMAIN[c].append(coach)
      total=request.form.get('total')
      now=datetime.datetime.now()
      string2=now.strftime(''' %Y-%m-%d''')
      
      main_cn=request.form.get('mobile')
      
      con.execute(f'insert into passenger values("{Name}","{Age}","{Gen}","{Berth}","{SEAT}","{Food}",{total},"{Pnr}","{coach}","{Class}","{USER}")')
      con.execute(f'insert into journey_det values("{Pnr}","{trans_id}","{string2}","{dat}","{detail[0][0]}","{detail[0][1]}","{main_cn}","{train_name}","{tr_no}","Confirmed","{USER}")')      
      BANK=request.form.get('bank')

      con.execute(f'select dept_time from rail where train_no="{tr_no}"')
      dept=con.fetchone()

      con.execute(f'select arr_time from rail where train_no={tr_no}')
      arr=con.fetchone()

      con.execute(f'select distance from distance where train_no={tr_no}')
      re=con.fetchone()

      con.execute(f'select train_name from rail where train_no="{tr_no}"')
      rw=con.fetchone()
      
      db.commit()
      train_no=str(tr_no)+'/'+str(rw[0])

      if request.method=='POST':
            return render_template('final_ticket.html',quota='GENERAL',total=total,pnr=Pnr,psng=len_main,sch_dept=dept[0],sch_arv=arr[0],BANK=BANK,MAIN=LMAIN,len_main=len_main,trns_id=trans_id,dat_book=string2,dat_jour=dat,FROM=fro,TO=to,cls=clas,dist=re[0],tr_na_id=train_no)
      return render_template('transaction_page.html')

def passenger_detail(pnr):
      con.execute(f'select user from passenger where PNR={pnr}')
      User=con.fetchone()
      con.execute(f'select passng from passenger where PNR={pnr} and user="{User[0]}"')
      nm=con.fetchone()
                              
      con.execute(f'select age from passenger where PNR={pnr} and user="{User[0]}"')
      ag=con.fetchone()

      con.execute(f'select gen from passenger where PNR={pnr} and user="{User[0]}"')
      ge=con.fetchone()

      con.execute(f'select BRTH from passenger where PNR={pnr} and user="{User[0]}"')
      br=con.fetchone()

      con.execute(f'select seat from passenger where PNR={pnr} and user="{User[0]}"')
      se=con.fetchone()

      con.execute(f'select food from passenger where PNR={pnr} and user="{User[0]}"')
      fo=con.fetchone()

      con.execute(f'select coach from passenger where PNR={pnr} and user="{User[0]}"')
      co=con.fetchone()

      con.execute(f'select class from passenger where PNR={pnr} and user="{User[0]}"')
      cls=con.fetchone()
                         
      NM=nm[0].split(',')
      NM.remove('')
                              
      AG=ag[0].split(',')
      AG.remove('')

      GE=ge[0].split(',')
      GE.remove('')

      BR=br[0].split(',')
      BR.remove('')

      SE=se[0].split(',')
      SE.remove('')

      FO=fo[0].split(',')
      FO.remove('')
                        
      CO=co[0]

      CLS=cls[0]
                        
      COACH=CO+' / '+CLS
      c=0
      a=0
      b=0
      y=0
      q=0
      z=0
      l=0
      
      LMAIN=[]
      for e in range(len(NM)):
            LMAIN.append([])
      for t in range(len(NM)):
            LMAIN[t].append(NM[a])
            a+=1
      for h in range(len(NM)):
            LMAIN[h].append(AG[c])
            c+=1
      for o in range(len(NM)):
             LMAIN[o].append(GE[b])
             b+=1
      for p in range(len(NM)):
             LMAIN[p].append(BR[y])
             y+=1
      for m in range(len(NM)):
             LMAIN[m].append(SE[q])
             q+=1
      for n in range(len(NM)):
             LMAIN[n].append(FO[z])
             z+=1
      for n in range(len(NM)):
             LMAIN[n].append(CO)
             LMAIN[n].append(CLS)
      return LMAIN

def cancel_detail(pnr):
      con.execute(f'select name from cancellation_detail where PNR={pnr}')
      nm=con.fetchone()
                              
      con.execute(f'select age from cancellation_detail where PNR={pnr}')
      ag=con.fetchone()

      con.execute(f'select gender from cancellation_detail where PNR={pnr}')
      ge=con.fetchone()

      con.execute(f'select berth from cancellation_detail where PNR={pnr}')
      br=con.fetchone()

      con.execute(f'select seat from cancellation_detail where PNR={pnr}')
      se=con.fetchone()

      con.execute(f'select food from cancellation_detail where PNR={pnr}')
      fo=con.fetchone()

      con.execute(f'select coach from cancellation_detail where PNR={pnr}')
      co=con.fetchone()

      con.execute(f'select class from cancellation_detail where PNR={pnr}')
      cls=con.fetchone()
                         
      NM=nm[0].split(',')
      NM.remove('')
                              
      AG=ag[0].split(',')
      AG.remove('')

      GE=ge[0].split(',')
      GE.remove('')

      BR=br[0].split(',')
      BR.remove('')

      SE=se[0].split(',')
      SE.remove('')

      FO=fo[0].split(',')
      FO.remove('')
                        
      CO=co[0]

      CLS=cls[0]
                        
      c=0
      a=0
      b=0
      y=0
      q=0
      z=0
      
      LMAIN=[]
      for e in range(len(NM)):
            LMAIN.append([])
      for t in range(len(NM)):
            LMAIN[t].append(NM[a])
            a+=1
      for h in range(len(NM)):
            LMAIN[h].append(AG[c])
            c+=1
      for o in range(len(NM)):
             LMAIN[o].append(GE[b])
             b+=1
      for p in range(len(NM)):
             LMAIN[p].append(BR[y])
             y+=1
      for m in range(len(NM)):
             LMAIN[m].append(SE[q])
             q+=1
      for n in range(len(NM)):
             LMAIN[n].append(FO[z])
             z+=1
      for n in range(len(NM)):
             LMAIN[n].append(CO)
             LMAIN[n].append(CLS)
      return LMAIN

@app.route('/pnr',methods=['GET','POST'])
def pnr():
      return render_template('pnr_1st_page.html')
@app.route('/pnr_detail',methods=['GET','POST'])
def pnr_det():
      error = None
      error_of_len=None
      pnr=request.form.get('pnr_value')
      print(type(pnr))
      if len(pnr) !=10:
            error_of_len='Error! PNR Number should be 10 digit numeric number.'
      else:
            con.execute('SELECT PNR FROM PASSENGER')
            re=con.fetchall()
            for r in re:
                  if r[0]==pnr:
                        LMAIN=passenger_detail(pnr)
                        len_MAIN=len(LMAIN)
                                                
                        con.execute(f'SELECT * FROM JOURNEY_DET WHERE PNR="{pnr}"')
                        train=con.fetchall()

                        con.execute(f'select train_name from journey_det where pnr="{pnr}"')
                        train_name=con.fetchall()
                        
                        con.execute(f'select price from passenger where pnr="{pnr}"')
                        total=con.fetchall()
                        
                        con.execute(f'SELECT date_jour FROM journey_det WHERE PNR="{pnr}"')
                        jour_dat=con.fetchone()                        

                        con.execute(f'SELECT coach FROM passenger WHERE PNR="{pnr}" ')
                        COACH=con.fetchall()                        
                        
                        if time.strftime('%Y-%M-%d') < jour_dat[0]:
                              train_status="Train has departed,Booking Not Allowed"
                              chart='Chart Prepared'
                        else:
                              train_status="Train has  not departed"
                              chart='Chart Not Prepared'
                        return render_template('pnr_enq.html',pnr=pnr,len_MAIN=len_MAIN,MAIN=LMAIN,TRAIN=train[0],coach=COACH[0][0],total_fare=total[0][0],train_stat=train_status,chart=chart)
                        break
                  elif r!=pnr:
                        continue
            else:
                  error='Error! PNR No. is not valid'
      return render_template('pnr_1st_page.html',error=error,error_of_len=error_of_len)
@app.route('/cancel_ticket',methods=['GET','POST'])
def cancel():
      con.execute(f'select * from journey_det  where user="{USER}"')
      list_main=con.fetchall()
      l=[]
      for x in range(0,len(list_main)):
            option=request.form.get(f'option{x+1}')
            l.append(option)
      for s in l:
            if s=='on':
                  con.execute(f'select status from journey_det where pnr="{list_main[l.index(s)][0]}"')
                  status=con.fetchone()
                  if status[0] == "Partially Cancelled":
                        cncl_list=cancel_detail(list_main[l.index(s)][0])
                        con.execute(f'select price,class from passenger where pnr="{list_main[l.index(s)][0]}" and user="{USER}"')
                        main=con.fetchall()
                        L=passenger_detail((list_main[l.index(s)][0]))
                        MAIN=[]
                        for i in L:
                           if i not in cncl_list:
                              MAIN.append(i)
                        print(MAIN)
                  else:
                     con.execute(f'select price,class from passenger where pnr="{list_main[l.index(s)][0]}" and user="{USER}"')
                     main=con.fetchall()
                     MAIN=passenger_detail((list_main[l.index(s)][0]))
                     print(MAIN)
                  len_MAIN=len(MAIN)
                  return render_template('cancel_request.html',pnr=list_main[l.index(s)][0],booking_stat='',LMAIN=list_main[l.index(s)],cls=main[0][1],tot=main[0][0],PASSNG=MAIN,len_list=len_MAIN)
                  break
      else:
            print('no')          
      return render_template('cancel_1st_page.html',len_main=len(list_main),List_Main=list_main)
@app.route('/cncl',methods=['GET','POST'])
def cncl():
      pnr=request.form.get('pnr_emp')
      MAIN=passenger_detail(pnr)
      l=[]
      cncl=random.randint(999999999,100000000000)
      cncl_list=[]
      CANCEL=[]
      c=0
      for x in range(0,len(MAIN)):
            option=request.form.get(f'option{x+1}')
            if option=='on':
                  cncl_list.append(x)
      for j in cncl_list:
            CANCEL.append(MAIN[j])
      
      Name=''
      Age=''
      Gen=''
      Berth=''
      Seat=''
      Food=''
      Coach=''
      Class=''
      
      for c in range(0,len(CANCEL)):
            Name+=CANCEL[c][0]+','

      for c in range(0,len(CANCEL)):
            Age+=CANCEL[c][1]+','

      for c in range(0,len(CANCEL)):
            Gen+=CANCEL[c][2]+','

      for c in range(0,len(CANCEL)):
            Berth+=CANCEL[c][3]+','

      for c in range(0,len(CANCEL)):
            Seat+=CANCEL[c][4]+','

      for c in range(0,len(CANCEL)):
            Food+=CANCEL[c][5]+','

      for c in range(0,len(CANCEL)):
            Coach+=CANCEL[c][6]+','
            
      for c in range(0,len(CANCEL)):
            Class+=CANCEL[c][7]+','
            
      con.execute(f"select train_name from journey_det where pnr='{pnr}'")
      train_name=con.fetchone()

      date_cancel=time.strftime('%d %M %Y')
      
      if len(CANCEL)==len(MAIN):
            status='Cancelled'
            con.execute(f'''update journey_det  set status="{status}" where PNR="{pnr}"''')
            con.execute(f'insert into cancellation_detail values("{cncl}","{pnr}","{Name}","{Age}","{Gen}","{train_name[0]}","{status}","{len(CANCEL)}","{date_cancel}","{Berth}","{Seat}","{Food}","{Coach}","{Class}")')
      else:
            status='Partially Cancelled'
            con.execute(f'update journey_det  set status="{status}" where PNR="{pnr}"')

      con.execute(f'select * from journey_det where pnr="{pnr}"  and user="{USER}"')
      LMAIN=con.fetchall() 

      con.execute(f'select class,price from passenger where pnr="{pnr}" and user="{USER}"')
      LM=con.fetchall()
      db.commit()
      totC=int(LM[0][1])-(len(CANCEL)*75)
      return render_template('cancel_confirmation.html',LMAIN=LMAIN[0],len_list=len(CANCEL),PASSNG=CANCEL,cncl_id=cncl,len_cncl=len(CANCEL),tot=LM[0][1],cls=LM[0][0],totc=totC)
@app.route('/search_cancel',methods=['GET','POST'])
def search_cancel():
      pnr=request.form.get('pnr_no')
      trns_id=request.form.get('trns_id')
      
      con.execute(f'select * from journey_det where pnr="{pnr}"')
      LMAIN=con.fetchone()
      PASSNG=passenger_detail(pnr)
            
      return render_template('cancel_request.html',pnr=pnr,LMAIN=LMAIN,PASSNG=PASSNG,len_list=len(PASSNG))

@app.route('/print_ticket_in_final',methods=['GET','POST'])
def print_ticket_in_final():
      error = None
      error_of_len=None
      con.execute('SELECT PNR FROM PASSENGER')
      re=con.fetchall()
      pnr=request.form.get('pnr')
      for r in re:                        
            if r[0]==pnr and len(pnr)==10:
                  con.execute(f'select * from journey_det where pnr={pnr}')
                  MAIN=con.fetchone()
                  LMAIN=passenger_detail(pnr)
                  
                  con.execute(f'select price from passenger where PNR={pnr}')
                  price=con.fetchone()

                  con.execute(f'select distance from distance where train_no={MAIN[8]}')
                  dist=con.fetchone()

                  con.execute(f'select dept_time from rail where train_no={MAIN[8]}')
                  time=con.fetchone()
      
                  f=open(f'tickets/{pnr}.txt','w')
                  f.write(f'''Transaction ID: {MAIN[1]} PNR No : {pnr}
Train No. & Name: {MAIN[8]}/{MAIN[7]} Date of Journey:{MAIN[3]}
Class: CC Date of Booking:{MAIN[2]} Date of Boarding:{MAIN[3]}
From: {MAIN[4]} To :{MAIN[5]} Distance: {dist[0]} KM
Boarding : {MAIN[4]} Resv Upto: {MAIN[5]} Quota: General
Scheduled Departure: {time[0]} Total Fare : Rs {price[0]} Adult: {len(LMAIN)} Child: 0
*Departure time printed on the ERS is liable to change. New time table from 01-07-2008''')
                  f.write('------------------------------------------------------------------------------------------------------------------------------------------------\n')
                  f.write('Sno\tName\tAge\tGender\tFood Choice\tBooking Status\tCurrent Status\n')
                  f.write('------------------------------------------------------------------------------------------------------------------------------------------------\n')
                  for c in range(0,len(LMAIN)):
                        f.write(f'{c+1}\t{LMAIN[c][0]}\t{LMAIN[c][1]}\t{LMAIN[c][2]}\t{LMAIN[c][5]}\t\t{LMAIN[c][4]}/{LMAIN[c][6]}/{LMAIN[c][3]}\t{LMAIN[c][4]}/{LMAIN[c][6]}/{LMAIN[c][3]}\n')
                        f.write('------------------------------------------------------------------------------------------------------------------------------------------------\n')
                  f.write('''Service Charges
1-IRCTC service charge:-Rs 25.00
2-Agents charge (in addition to IRCTC service charges) Rs.10/- for Second / Sleeper class per ticket and Rs. 20/- for
higher class per ticket.
3- GSA(Agent in Nepal,Sharjah)- will charge (in addition to IRCTC service charges) Rs.50/- for Second / Sleeper class
per ticket and Rs. 100/- for higher class per ticket.
Important
• One of the passenger booked on an E-ticket is required to present any of the five identity cards noted below in original during the
train journey and same will be accepted as a proof of identity failing which all the passengers will be treated as travelling without ticket
and shall be dealt as per extant Railway Rules. Valid Ids:- Voter Identity Card / Passport / PAN Card / Driving License / Photo ID card
issued by Central / State Govt. for their employees.
• The accommodation booked is not transferable and is valid only if one of the ID card noted above is presented during the journey.
The passenger should carry with him the Electronic Reservation Slip print out. In case the passenger does not carry the electronic
reservation slip, a charge of Rs.50/- per ticket shall be recovered by the ticket checking staff and an excess fare ticket will be issued in
lieu of that.
• E-ticket cancellations are permitted through www.irctc.co.in by the user. In case e-ticket is booked through an agent, please
contact respective agent for cancellations.
• Just dial 139 from your landline, mobile & CDMA phones for railway enquiries.
Contact us on:- 24*7 Hrs. Customer Support at 011-23340000 , MON - SAT(10 AM - 6 PM) 011-
23345500/4787/4773/5800/8539/8543 , Chennai Customer Care 044 - 25300000.or Mail To: care@irctc.co.in ''')
                  f.close()
                  return 'Ticket Is saved in folder'

                  break
            elif r!=pnr:
                  continue
      return render_template('print_ticket.html')
@app.route('/print_ticket',methods=['GET','POST'])
def print_ticket():
      pnr=request.form.get('pnr_emp')
      con.execute(f'select * from journey_det where pnr={pnr}')
      MAIN=con.fetchone()
      LMAIN=passenger_detail(pnr)

      con.execute(f'select price from passenger where PNR={Pnr}')
      price=con.fetchone()

      con.execute(f'select distance from distance where train_no={MAIN[8]}')
      dist=con.fetchone()

      con.execute(f'select dept_time from rail where train_no={MAIN[8]}')
      time=con.fetchone()
      
      f=open(f'tickets/{pnr}.txt','w')
      f.write(f'''Transaction ID: {MAIN[1]} PNR No : {Pnr}
Train No. & Name: {MAIN[8]}/{MAIN[7]} Date of Journey:{MAIN[3]}
Class: CC Date of Booking:{MAIN[2]} Date of Boarding:{MAIN[3]}
From: {MAIN[4]} To :{MAIN[5]} Distance: {dist[0]} KM
Boarding : {MAIN[4]} Resv Upto: {MAIN[5]} Quota: General
Scheduled Departure: {time[0]} Total Fare : Rs {price[0]} Adult: {len(LMAIN)} Child: 0
*Departure time printed on the ERS is liable to change. New time table from 01-07-2008''')
      f.write('------------------------------------------------------------------------------------------------------------------------------------------------\n')
      f.write('Sno\tName\tAge\tGender\tFood Choice\tBooking Status\tCurrent Status\n')
      f.write('------------------------------------------------------------------------------------------------------------------------------------------------\n')
      for c in range(0,len(LMAIN)):
            f.write(f'{c+1}\t{LMAIN[c][0]}\t{LMAIN[c][1]}\t{LMAIN[c][2]}\t{LMAIN[c][5]}\t{LMAIN[c][4]}/{LMAIN[c][6]}/{LMAIN[c][3]}\t{LMAIN[c][4]}/{LMAIN[c][6]}/{LMAIN[c][3]}\n')
            f.write('------------------------------------------------------------------------------------------------------------------------------------------------\n')
      f.write('''Service Charges
1-IRCTC service charge:-Rs 25.00
2-Agents charge (in addition to IRCTC service charges) Rs.10/- for Second / Sleeper class per ticket and Rs. 20/- for
higher class per ticket.
3- GSA(Agent in Nepal,Sharjah)- will charge (in addition to IRCTC service charges) Rs.50/- for Second / Sleeper class
per ticket and Rs. 100/- for higher class per ticket.
Important
• One of the passenger booked on an E-ticket is required to present any of the five identity cards noted below in original during the
train journey and same will be accepted as a proof of identity failing which all the passengers will be treated as travelling without ticket
and shall be dealt as per extant Railway Rules. Valid Ids:- Voter Identity Card / Passport / PAN Card / Driving License / Photo ID card
issued by Central / State Govt. for their employees.
• The accommodation booked is not transferable and is valid only if one of the ID card noted above is presented during the journey.
The passenger should carry with him the Electronic Reservation Slip print out. In case the passenger does not carry the electronic
reservation slip, a charge of Rs.50/- per ticket shall be recovered by the ticket checking staff and an excess fare ticket will be issued in
lieu of that.
• E-ticket cancellations are permitted through www.irctc.co.in by the user. In case e-ticket is booked through an agent, please
contact respective agent for cancellations.
• Just dial 139 from your landline, mobile & CDMA phones for railway enquiries.
Contact us on:- 24*7 Hrs. Customer Support at 011-23340000 , MON - SAT(10 AM - 6 PM) 011-
23345500/4787/4773/5800/8539/8543 , Chennai Customer Care 044 - 25300000.or Mail To: care@irctc.co.in ''')
      f.close()
      return f'<strong><h1 style="background-color:aqua;">Ticket Is saved in folder of PNR:{pnr}</h1></strong>'

@app.route('/another',methods=['GET','POST'])
def another():
      return redirect(url_for('info',user=name))

@app.route('/mail',methods=['GET','POST'])
def send_ticket():
      return render_template('send_ticket_mail.html')

@app.route('/send_ticket_mail',methods=['GET','POST'])
def send_ticket_mail():
      con.execute(f'select * from journey_det where pnr={Pnr}')
      MAIN=con.fetchone()
      LMAIN=passenger_detail(Pnr)
      
      con.execute(f'select price from passenger where PNR={Pnr}')
      price=con.fetchone()

      con.execute(f'select distance from distance where train_no={MAIN[8]}')
      dist=con.fetchone()

      con.execute(f'select dept_time from rail where train_no={MAIN[8]}')
      time=con.fetchone()
      
      f=open(f'tickets/{Pnr}.txt','w')
      f.write(f'''Transaction ID: {MAIN[1]} PNR No : {Pnr}
Train No. & Name: {MAIN[8]}/{MAIN[7]} Date of Journey:{MAIN[3]}
Class: CC Date of Booking:{MAIN[2]} Date of Boarding:{MAIN[3]}
From: {MAIN[4]} To :{MAIN[5]} Distance: {dist[0]} KM
Boarding : {MAIN[4]} Resv Upto: {MAIN[5]} Quota: General
Scheduled Departure: {time[0]} Total Fare : Rs {price[0]} Adult: {len(LMAIN)} Child: 0
*Departure time printed on the ERS is liable to change. New time table from 01-07-2008''')
      f.write('------------------------------------------------------------------------------------------------------------------------------------------------\n')
      f.write('Sno\tName\tAge\tGender\tFood Choice\tBooking Status\tCurrent Status\n')
      f.write('------------------------------------------------------------------------------------------------------------------------------------------------\n')
      for c in range(0,len(LMAIN)):
            f.write(f'{c+1}\t{LMAIN[c][0]}\t{LMAIN[c][1]}\t{LMAIN[c][2]}\t{LMAIN[c][5]}\t{LMAIN[c][4]}/{LMAIN[c][6]}/{LMAIN[c][3]}\t{LMAIN[c][4]}/{LMAIN[c][6]}/{LMAIN[c][3]}\n')
            f.write('------------------------------------------------------------------------------------------------------------------------------------------------\n')
      f.write('''Service Charges
1-IRCTC service charge:-Rs 25.00
2-Agents charge (in addition to IRCTC service charges) Rs.10/- for Second / Sleeper class per ticket and Rs. 20/- for
higher class per ticket.
3- GSA(Agent in Nepal,Sharjah)- will charge (in addition to IRCTC service charges) Rs.50/- for Second / Sleeper class
per ticket and Rs. 100/- for higher class per ticket.
Important
• One of the passenger booked on an E-ticket is required to present any of the five identity cards noted below in original during the
train journey and same will be accepted as a proof of identity failing which all the passengers will be treated as travelling without ticket
and shall be dealt as per extant Railway Rules. Valid Ids:- Voter Identity Card / Passport / PAN Card / Driving License / Photo ID card
issued by Central / State Govt. for their employees.
• The accommodation booked is not transferable and is valid only if one of the ID card noted above is presented during the journey.
The passenger should carry with him the Electronic Reservation Slip print In case the passenger does not carry the electronic
reservation slip, a charge of Rs.50/- per ticket shall be recovered by the ticket checking staff and an excess fare ticket will be issued in
lieu of that.
• E-ticket cancellations are permitted through www.irctc.co.in by the user. In case e-ticket is booked through an agent, please
contact respective agent for cancellations.
• Just dial 139 from your landline, mobile & CDMA phones for railway enquiries.
Contact us on:- 24*7 Hrs. Customer Support at 011-23340000 , MON - SAT(10 AM - 6 PM) 011-
23345500/4787/4773/5800/8539/8543 , Chennai Customer Care 044 - 25300000.or Mail To: care@irctc.co.in ''')
      f.close()
      
      mail_=request.form.get('mail')
      
      msg = Message(f'Your Ticket of PNR:{Pnr}', sender = 'hk8084262@gmail.com', recipients = [mail_])
      
      with app.open_resource(f"tickets/{Pnr}.txt") as fp:  
           msg.attach(f"{Pnr}.txt","text/plain",fp.read())  
      mail.send(msg)
      os.remove(f'tickets/{Pnr}.txt')
      return f'''<h1 style="background-color:aqua;">ticket Successfully send on {mail_}</h1>'''
if __name__=='__main__':
      
      url = 'http://127.0.0.1:5000'
      webbrowser.open_new(url)
      app.run(debug=True)
