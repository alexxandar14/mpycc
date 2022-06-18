import pandas as pd
from mpyc.runtime import mpc
from mpyc.seclists import seclist

secint = mpc.SecInt(16)
secflt = mpc.SecFxp(128)
df = pd.read_csv("data.csv")
df = df[0:100]


col0 = df.Id.to_list()
col1 = df["Water Temperature"].to_list()
col2 = df["Turbidity"].to_list()
col3 = df["Wave Height"].to_list()
col4 = df["Wave Period"].to_list()
col5 = df["Battery Life"].to_list()

mpc.run( mpc.start())
col0 = mpc.input(list(map(secint,col0)),senders= [0,1])
col1 = mpc.input(list(map(secflt,col1)),senders= [0,1])
col2 = mpc.input(list(map(secflt,col2)),senders= [0,1])
col3 = mpc.input(list(map(secflt,col3)),senders= [0,1])
col4 = mpc.input(list(map(secint,col4)),senders= [0,1])
col5 = mpc.input(list(map(secflt,col5)),senders= [0,1])
col0 = [j for sub in col0 for j in sub]
col1 = [j for sub in col1 for j in sub]
col2 = [j for sub in col2 for j in sub]
col3 = [j for sub in col3 for j in sub]
col4 = [j for sub in col4 for j in sub]
col5 = [j for sub in col5 for j in sub]
df = pd.DataFrame(list(zip(col0, col1, col2, col3,col4, col5)),
               columns =['Id', 'Water Temperature','Turbidity','Wave Height','Wave Period','Battery Life'])
            

res = mpc.run(mpc.output(mpc.max(df['Wave Height'].to_list()),receivers = [2]))
if mpc.pid in [2]:
    print(res)



mpc.run(mpc.shutdown())
