import matplotlib as plt

def grafico_barras_plt(datos,datosx,datosy,titulo):
    
    x= datos[datosx]
    y = datos[datosy]
    total= sum(y)

    plt.figure(figsize=(5,5))
    bars = plt.bar(x,y)
    plt.title(titulo)
    plt.xlabel("Tipo de sexo")
    plt.ylabel("cantidad")

    # Agregar valores a las barras
    for bar, value in zip(bars,y):
        porcentaje = (value/total) *100
        plt.text(
            bar.get_x() + bar.get_width() / 2,  # Coordenada x centrada en la barra
            bar.get_height() + 0.5,
            f"{value} ({porcentaje:,.2f}%)",     # Coordenada y ligeramente encima de la barra
            #str(bar.get_height()),             # Texto que muestra la altura de la barra
            ha='center',                       # Centrar el texto horizontalmente
            va='bottom'                        # Alinear el texto verticalmente con la parte inferior
        )

    plt.show()