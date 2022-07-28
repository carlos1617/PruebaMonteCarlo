from flask import Flask,render_template

app = Flask(__name__)
@app.route("/pruebamontecarlo1")
def inicio():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

    datos = pd.DataFrame()
    ventas=[0,1,2,3,4,5,6]
    semana=[0.08,0.12,0.28,0.24,0.14,0.10,0.04]
    datos["Ventas"]=ventas
    datos["Probabilidad"]=semana
    datos
    data=datos.to_html(classes="table table-hover table-striped", justify="justify-all", border=2)
    
    

    aleatorios=pd.DataFrame()
    aleatorios["ri"]=[0.11,0.44,0.9,0.52,0.00,0.54,0.56,0.66,0.52,0.46,0.24,0.31,0.49,0.03,0.50,0.65,0.80,0.74,0.32,0.66]
    aleatorios
    data4=aleatorios.to_html(classes="table table-hover table-striped", justify="justify-all", border=2)

    
    return render_template('inicio.html', data=data,  data4=data4)
@app.route("/resultados")
def resultados():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    datos = pd.DataFrame()
    ventas=[0,1,2,3,4,5,6]
    semana=[0.08,0.12,0.28,0.24,0.14,0.10,0.04]
    datos["Ventas"]=ventas
    datos["Probabilidad"]=semana
    datos
    aleatorios=pd.DataFrame()
    aleatorios["ri"]=[0.11,0.44,0.9,0.52,0.00,0.54,0.56,0.66,0.52,0.46,0.24,0.31,0.49,0.03,0.50,0.65,0.80,0.74,0.32,0.66]
    aleatorios
    x2=np.cumsum(datos["Probabilidad"])
    datos["FPA"]=x2
    datos
    data1=datos.to_html(classes="table table-hover table-striped", justify="justify-all", border=2)

    datos['Min'] = datos['FPA']
    datos['Max'] = datos['FPA']
    datos
    data2=datos.to_html(classes="table table-hover table-striped", justify="justify-all", border=2)

    lis = datos["Min"].values
    lis2 = datos['Max'].values
    lis[0]= 0
    for i in range(1,6):
        lis[i] = lis2[i-1]
    datos['Min'] =lis
    datos
    

    min = datos['Min'].values
    max = datos['Max'].values
    dato=[]
    simulacion=pd.DataFrame()
    for j in range(len(aleatorios)):
        for i in range(len(datos)):
            if(aleatorios["ri"][j]>=datos["Min"][i] and aleatorios["ri"][j]<datos["Max"][i]):
                dato.append(datos["Ventas"][i])
    simulacion["ri"]=aleatorios["ri"]
    simulacion["Ventas"]=dato
    simulacion## RESPUESTA DEL A
    data5=simulacion.to_html(classes="table table-hover table-striped", justify="justify-all", border=2)
    return render_template('resultados.html', data1=data1,  data2=data2, data5=data5)
if __name__ == '__main__':
    app.run(port=4500,debug=True)