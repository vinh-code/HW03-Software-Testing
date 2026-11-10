import sqlite3,json
from pathlib import Path
c=sqlite3.connect('sut/backend/database.sqlite')
users={}
for label,name in [('main','Task 1 Tester'),('empty','Task 1 Empty'),('other','Task 1 Other')]:
 email=f'task1-{label}@example.test'
 row=c.execute('select id from users where email=?',(email,)).fetchone()
 if row: uid=row[0]; c.execute('delete from orders where user_id=?',(uid,))
 else: uid=c.execute('insert into users (name,email,password,role) values (?,?,?,?)',(name,email,'GuiTest123!','user')).lastrowid
 c.execute('update users set name=?,phone=?,shipping_address=?,login_attempts=0,locked_until=NULL where id=?',(name,'0912345678','123 Test Street',uid))
 users[label]=uid
orders={}
for i,state in enumerate(['pending','confirmed','shipping','delivered','canceled']):
 orders[state]=c.execute('insert into orders (user_id,total_amount,status,shipping_address) values (?,?,?,?)',(users['main'],1234000+i*1000,state,'<b>GUI_ADDRESS</b>')).lastrowid
orders['other']=c.execute('insert into orders (user_id,total_amount,status,shipping_address) values (?,?,?,?)',(users['other'],987654,'pending','Other user address')).lastrowid
c.commit();c.close()
Path('submission/task1/evidence/fixture.json').write_text(json.dumps({'users':users,'orders':orders},indent=2))
print(json.dumps({'users':users,'orders':orders}))
