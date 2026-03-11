from flask import Flask,render_template,request,session,redirect
from sklearn.ensemble import RandomForestClassifier

from Dbconnection import Db
import random
import datetime
app = Flask(__name__)
path=("D:\\House Price Prediction\\house price prediction\\static\\")
app.secret_key="abc"
@app.route('/',methods=['GET','POST'])
def  login():
    if request.method == "POST":
        u = request.form['username']
        p = request.form['password']
        db = Db()

        ss = db.selectOne("select * from login where username='" + u + "' and password='" + p + "'")
        if ss is not None:
            if ss['usertype'] == 'admin':
                session['lid'] = ss['login_id']
                session['lg'] = '1'
                return redirect('/admin')

            elif ss['usertype'] == 'user':
                session['lg'] = '1'
                session['u_id'] = ss['login_id']

                return redirect('/user')
            else:

                return '<script>alert("invalid ");window.location="/"</script>'
        else:
            return '<script>alert("user not exist");window.location="/"</script>'

    return render_template('login.html')


@app.route('/logout')
def logout():
    session['lg']=""
    return redirect('/')

@app.route('/admin')
def admin():
    if session['lg']=="1":
        return render_template("admin/index.html")
    else:
        return redirect('/')

@app.route('/add_property',methods=['GET','POST'])
def add_property():
    if session['lg'] == "1":
        if request.method=="POST":
            db=Db()
            zone=request.form['zone']
            lotfrontage=request.form['lotfrontage']
            lotarea=request.form['lotarea']
            street=request.form['street']
            alley=request.form['alley']
            lotshape=request.form['lotshape']
            utilities=request.form['utilities']
            house=request.form['house']
            yearbuild=request.form['yearbuild']
            bedroom=request.form['bedroom']
            kitchen=request.form['kitchen']
            price=request.form['price']
            db.insert("insert into property VALUES ('','"+zone+"','"+lotfrontage+"','"+lotarea+"','"+street+"','"+alley+"','"+lotshape+"','"+utilities+"','"+house+"','"+yearbuild+"','"+bedroom+"','"+kitchen+"','"+price+"', '"+str(session['lid'])+"')")
            return '<script>alert("added");window.location="/add_property"</script>'
        else:
            return render_template("admin/property_registration.html")
    else:
        return redirect('/')

@app.route('/user_add_property',methods=['GET','POST'])
def user_add_property():
    if session['lg'] == "1":
        if request.method=="POST":
            db=Db()
            zone=request.form['zone']
            lotfrontage=request.form['lotfrontage']
            lotarea=request.form['lotarea']
            street=request.form['street']
            alley=request.form['alley']
            lotshape=request.form['lotshape']
            utilities=request.form['utilities']
            house=request.form['house']
            yearbuild=request.form['yearbuild']
            bedroom=request.form['bedroom']
            kitchen=request.form['kitchen']
            price=request.form['price']
            db.insert("insert into property VALUES ('','"+zone+"','"+lotfrontage+"','"+lotarea+"','"+street+"','"+alley+"','"+lotshape+"','"+utilities+"','"+house+"','"+yearbuild+"','"+bedroom+"','"+kitchen+"','"+price+"', '"+str(session['u_id'])+"')")
            return '<script>alert("added");window.location="/user_add_property"</script>'
        else:
            return render_template("user/property_registration.html")
    else:
        return redirect('/')

@app.route('/view')
def view():
    if session['lg'] == "1":

        db=Db()
        s=db.select("select * from property")
        print(s)
        return render_template("admin/view_property.html",prop=s)
    else:
        return redirect('/')





@app.route('/delete/<p>')
def delete(p):
    if session['lg'] == "1":
        db=Db()
        s=db.delete("delete  from property where property_id='"+p+"'")
        return '<script>alert("deleted");window.location="/view"</script>'
    return redirect('/')

@app.route('/view_user')
def view_user():
    if session['lg'] == "1":
        db=Db()
        s = db.select("select * from user,login where login.login_id =user.user_id")
        print(s)
        return render_template("admin/view_user.html",user=s)
    return redirect('/')

@app.route('/block_user/<b>')
def block_user(b):
        if session['lg'] == "1":
            db = Db()
            s = db.update("update login set usertype='block' where login_id='"+b+"'")
            print(s)
            return '''<script>alert('user blocked');window.location="/view_user"</script>'''
        return redirect('/')

@app.route('/unblock_user/<b>')
def unblock_user(b):
            if session['lg'] == "1":
                db = Db()
                s = db.update("update login set usertype='user' where login_id='" + b + "'")
                print(s)
                return '''<script>alert('user unblocked');window.location="/view_user"</script>'''
            return redirect('/')

        # ---------------------USER-------------
@app.route('/user')
def user():
    if session['lg'] == "1":
        return render_template("user/home.html")
    return redirect('/')


@app.route('/user_registrtion',methods=['GET','POST'])
def user_registration():
    if request.method=="POST":
        db=Db()
        un=request.form['textfield']
        ue=request.form['textfield2']
        uphon=request.form['textfield3']

        pas=request.form['p']
        q2=db.selectOne("select * from login where username='"+ue+"'")
        if q2 is None:
            ss=db.insert("insert into login VALUES ('','"+ue+"','"+str(pas)+"','user')")
            db.insert("insert into user VALUES ('"+str(ss)+"','"+un+"','"+ue+"','"+uphon+"')")
            return '<script>alert("registerd");window.location="/"</script>'
        else:
            return '<script>alert("Already exist!!!");window.location="/"</script>'

    else:
        return render_template("register.html")




@app.route('/view_property',methods=["get","post"])
def view_property():
    if session['lg'] == "1":
        if request.method=='POST':
            n=request.form['textfield4']
            db = Db()
            s = db.select("select * from property  where userid!='"+str(session['u_id'])+"' and zone LIKE '%" + n + "%' ")
            print(s)
            return render_template("user/view_property.html", prop=s)
        db=Db()
        k=[]
        s=db.select("select * from property where userid!='"+str(session['u_id'])+"' ")
        for i in s:
            res={}
            q=db.selectOne("select * from user where user_id='"+str(i['userid'])+"'")
            res['zone']=i['zone']
            res['lotfrontage']=i['lotfrontage']
            res['lotarea']=i['lotarea']
            res['street_type']=i['street_type']
            res['alley_type']=i['alley_type']
            res['lotshape']=i['lotshape']
            res['utilities']=i['utilities']
            res['housestyle']=i['housestyle']
            res['yearbuild']=i['yearbuild']
            res['bedroom']=i['bedroom']
            res['kitchen']=i['kitchen']
            res['price']=i['price']
            if q is not None:
                res['phone']=q['phone']
            else:
                res['phone'] = "9876543210"
            k.append(res)

        return render_template("user/view_property.html", prop=k)
    return redirect('/')



@app.route('/view_my_property',methods=["get","post"])
def view_my_property():
    if session['lg'] == "1":
        if request.method=='POST':
            n=request.form['textfield4']
            db = Db()
            s = db.select("select * from property  where userid='"+str(session['u_id'])+"' and zone LIKE '%" + n + "%' ")

            return render_template("user/view_my_property.html", prop=s)
        db=Db()
        s=db.select("select * from property where userid='"+str(session['u_id'])+"'")

        return render_template("user/view_my_property.html", prop=s)
    return redirect('/')

@app.route('/prediction',methods=["get","post"])
def prediction():
    if session['lg'] == "1":
        if request.method=='POST':
            zone = request.form['zone']
            lotfrontage = request.form['lotfrontage']
            lotarea = request.form['lotarea']
            street = request.form['street']
            alley = request.form['alley']
            lotshape = request.form['lotshape']
            utilities = request.form['utilities']
            house = request.form['house']
            yearbuild = request.form['yearbuild']
            bedroom = request.form['bedroom']
            kitchen = request.form['kitchen']
            ar=[]
            import numpy as np
            ar.append(zone)
            ar.append(lotfrontage)
            ar.append(lotarea)
            ar.append(street)
            ar.append(alley)
            ar.append(lotshape)
            ar.append(utilities)
            ar.append(house)
            ar.append(yearbuild)
            ar.append(bedroom)
            ar.append(kitchen)
            arr=[]
            test_val=np.array(ar)
            arr.append(test_val)
            # CART Classification
            import pandas
            from sklearn import model_selection
            from sklearn.linear_model import LogisticRegression
            url = "D:\\House Price Prediction\\house price prediction\\train_new.csv"
            # url = "D:\\House Price Prediction\\house price prediction\\train_new.csv"
            dataframe = pandas.read_csv(url)

            array = dataframe.values
            print(array[0])
            X = array[:, 0:11]
            Y = array[:, 11]
            from sklearn.model_selection import train_test_split
            xtrain, xtest, ytrain, ytest = train_test_split(
                X, Y, test_size=0.25, random_state=0)
            from sklearn.preprocessing import StandardScaler
            sc_x = StandardScaler()
            xtrain = sc_x.fit_transform(xtrain)
            xtest = sc_x.transform(xtest)
            from sklearn.linear_model import LogisticRegression
            classifier = LogisticRegression(random_state=0)
            classifier.fit(xtrain, ytrain)
            y_pred = classifier.predict(arr)
            from sklearn.ensemble import RandomForestRegressor
            # create regressor object
            regressor = RandomForestRegressor(n_estimators=100, random_state=42)
            # fit the regressor with x and y data
            regressor.fit(xtrain, ytrain)
            a=regressor.predict(arr)
            import numpy as np
            from sklearn.linear_model import LinearRegression
            model = LinearRegression()
            model.fit(xtrain, ytrain)
            y_pred1 = model.predict(arr)
            y_pred1 =str(abs(y_pred1[0]))[:7]
            j = int(y_pred[0]) + int(a[0]) + int(y_pred1)
            print(j)
            pr= (j)/3
            r=round(pr,2)
            r=round(r*5,2)
            session['zone']=zone1(zone)
            session['lotfrontage']=lotfrontage
            session['lotarea']=lotarea
            session['street']=street1(street)
            session['alley']=alley1(alley)
            session['lotshape']=Lotshape1(lotshape)
            session['utilities']=Utilities(utilities)
            session['house']=House_Style(house)
            session['yearbuild']=yearbuild
            session['bedroom']=bedroom
            session['kitchen']=kitchen
            session['r']=r
            return render_template("user/Prediction.html", r=r)
        db=Db()
        s=db.select("select * from property ")
        return render_template("user/Prediction.html")
    return redirect('/')

@app.route('/insert_prediction')
def insert_prediction():
    if session['lg'] == "1":
        db=Db()
        db.insert("insert into `property`(`property_id`,`zone`,`lotfrontage`,`lotarea`,`street_type`,`alley_type`,`lotshape`,`utilities`,`housestyle`,`yearbuild`,`bedroom`,`kitchen`,`price`,`userid`) values ( '','"+str(session['zone'])+"','"+str(session['lotfrontage'])+"','"+str(session['lotarea'])+"','"+str(session['street'])+"','"+str(session['alley'])+"','"+str(session['lotshape'])+"','"+str(session['utilities'])+"','"+str(session['house'])+"','"+str(session['yearbuild'])+"','"+str(session['bedroom'])+"','"+str(session['kitchen'])+"','"+str(session['r'])+"','"+str(session['u_id'])+"');")
        return '<script>alert("Added ");window.location="/prediction"</script>'
    return redirect('/')

def zone1(i):
    if i=='0':
        return 'Residential Low Density'
    if i=='1':
        return 'Residential Medium Density'
    if i=='2':
        return 'Commercial'
    if i=='Floating Village Residential':
        return '3'
    if i=='Residential High Density':
        return '4'

def street1(i):
    if i=='0':
        return 'Pave'
    if i=='1':
        return 'Grvl'

def alley1(i):
    if i=='0':
        return 'No alley access'
    if i=='2':
        return 'Pave'
    if i=='1':
        return 'Grvl'

def Lotshape1(i):
    if i=='0':
        return 'Regular'
    if i=='1':
        return 'IR1: Slightly irregular'
    if i=='2':
        return 'IR2: Moderately Irregular'
    if i=='3':
        return 'IR3: Irregular'

def Utilities(i):
    if i=='0':
        return 'All Public Utilities (E,G,W,& S)'
    if i=='1':
        return 'NoSeWa: Electricity and Gas Only'

def House_Style(i):
    if i == '0':
        return '1Story'
    if i == '1':
        return '2Story'
    if i == '2':
        return '1.5Story: 2nd level finished'
    if i == '3':
        return '1.5Story: 2nd level unfinished'
    if i == '4':
        return 'Split Foyer'
    if i == '5':
        return 'Split Lvl'
    if i == '6':
        return '2.5Story: 2nd level unfinished'
    if i == '7':
        return '2.5Story: 2nd level finished'























if __name__ == '__main__':
    app.run(debug=True)

