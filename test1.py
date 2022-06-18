import pandas as pd
from mpyc.runtime import mpc
from mpyc.seclists import seclist

secint = mpc.SecInt(16)
students = [(1, 13, 145),
           (2, 46, 190),
           (3, 25, 200),
           (4, 33, 222)
           ]
student_df = pd.DataFrame(students, columns=['Id', 'Age', 'Score'])
col0 = student_df.Id.to_list()
col1 = student_df.Age.to_list()
col2 = student_df.Score.to_list()
cols = [col0,col1,col2]
mpc.run( mpc.start())
col0 = mpc.input(list(map(secint,col0)),senders= [0,1])
col1 = mpc.input(list(map(secint,col1)),senders= [0,1])
col2 = mpc.input(list(map(secint,col2)),senders= [0,1])
col0 = [j for sub in col0 for j in sub]
col1 = [j for sub in col1 for j in sub]
col2 = [j for sub in col2 for j in sub]
df = pd.DataFrame(list(zip(col0, col1, col2)),
               columns =['Id', 'Age','Score'])
            

res = mpc.run(mpc.output(mpc.max(df['Age'].to_list()),receivers = [2]))
if mpc.pid in [2]:
    print(res)



mpc.run(mpc.shutdown())
