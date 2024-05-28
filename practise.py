name = ['Bhavik -', 'Vivek -', '- Kishori']
app = []
for all in name:
    splited_value = all.split('-')
    if len(splited_value[0]) > len(splited_value[1]):
        app.append(splited_value[0])
    else:
        app.append(splited_value[1])

print