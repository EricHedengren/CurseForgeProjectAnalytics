from matplotlib import pyplot as plt
from numpy import arange
from glob import glob
from os import remove
import pandas

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def line(name, color, label, order=2):
    plt.plot_date(display_dates, data[name], color, label=label, zorder=order)

def details_line(name, color, label, order=2, mean=None):
    plt.plot_date(display_dates, data[name], color, label=label, zorder=order)

    if mean == None:
        mean = data[name].mean()
    high = data[name].max()
    style=['dotted','dashed']

    for i, j in enumerate([mean,high]):
        plt.plot_date([begin, end], [j,j], color, ls=style[i], alpha=.5, zorder=1.99)

def subplot(y, z):
    plt.title(y)
    plt.ylabel(z)
    plt.tick_params(labelright=True, right=True)
    plt.legend(loc='upper left')
    plt.xlim([begin, end]); plt.ylim(0)
    plt.xticks(arange(0, date_size, tick_frequency)) # Start, Stop, Steps

data_files = glob('Data/*')
current_projects = []

for i, name in enumerate(data_files):
    if i == len(data_files)-1:
        current_projects.append(name)
        break
    next_name = data_files[i+1]
    if name[:name.index('_overview_v1_')] == next_name[:next_name.index('_overview_v1_')]:
        remove(name)
        continue
    current_projects.append(name)

d='Date'; p='Points'; hd='Historical Download'; dd='Daily Download'
dud='Daily Unique Download'; dtad='Daily Twitch App Download'; dcfd='Daily Curse Forge Download'
columns = [p,hd,dd,dud,dtad,dcfd]

df = pandas.DataFrame()

df[d] = None
for col in columns:
    df[col] = None

dataframe_index = 0
analyt = ' Analytics '

for current_file in current_projects:
    data = pandas.read_csv(current_file)

    dates = pandas.to_datetime(data[d]).dt.strftime('%Y-%m-%d')
    display_dates = pandas.to_datetime(dates).dt.strftime('%y-%m-%d') # Format x axis date display

    for i, date in enumerate(dates):
        if date in df[d].values:
            date_index = df[df[d]==date].index.values
            for column_name in columns:
                df[column_name][date_index] += data[column_name][i] #df.replace({column_name: date_index}, df[column_name][date_index] + data[column_name][i])
        else:
            df.loc[dataframe_index+1] = {d: date, p: data[p][i], hd: data[hd][i],\
            dd: data[dd][i], dud: data[dud][i], dtad: data[dtad][i], dcfd: data[dcfd][i]}
            dataframe_index = df.index.max()

    begin = display_dates[0]; end = display_dates.values[-1]

    date_size = dates.size
    tick_frequency = int(date_size/15)+1

    if tick_frequency < 1:
        tick_frequency = 1

    plt.figure(figsize=(20,11))
    plt.style.use('dark_background')

    if 'Name' in df.columns:
        project_name = data['Name'][0]
        if len(project_name) > 40:
            raise Exception('Project name is way too long')
    else:
        project_name = 'Total Overview'

    plt.suptitle(project_name, fontsize=50)

    t = 3
    if data['Points'].sum() == 0:
        t = 2

    plt.subplot(t,1,1)
    current_total = str(data[hd].values[-1])
    line(hd,'white','Total Downloads\n'+current_total)
    subplot('Total', 'Downloads')

    plt.subplot(t,1,2)
    details_line(dd,'white','Total',2.03)
    details_line(dud,'red','Unique',2.02)
    details_line(dcfd,'green','Curse Forge',2.01)
    details_line(dtad,'#6441a5','Twitch App')
    subplot('Daily Downloads', 'Downloads')

    if t == 3:
        plt.subplot(t,1,3)
        dp = data[p]
        details_line(p,'gold',p+'\n'+'%.2f' % dp.sum(),mean=dp[dp != 0].mean())
        plt.xlabel('Dates')
        subplot(p,p)

    plt.savefig('Graphs/'+ project_name + analyt + dates[0]+'_'+dates.values[-1], dpi=150)

df = df.sort_values(by=['Date'])
df.to_csv('Data/Total Overview_overview_v1_.csv', index=False, header=True)

# save summary graph

graphs = glob('Graphs/*')

for i, name in enumerate(graphs):
    if i == len(graphs)-1:
        break
    next_name = graphs[i+1]
    if name[:name.index(analyt)] == next_name[:next_name.index(analyt)]:
        remove(name)
        continue