df = pd.DataFrame()
for season in range(23):
    season +=1
    d =pd.read_html(f"https://en.wikipedia.org/wiki/The_Bachelor_(season_{season})",header=0)
    for i in d:
        if 'Name' in list(i.columns):
            i['season'] = season
            try:
                i = i.rename(columns={'Eliminated':'Outcome'})
            except:
                pass
            try:
                i = i.rename(columns={'Job':'Occupation'})
            except:
                pass
            df = df.append(i)
del df['Place']
del df['Ref']