inmuebles = [
    {
        "casa": "Casa 1",
        "año": 2000,
        "metros": 100,
        "habitaciones": 3,
        "garaje": True,
        "zona": "A",
    },
    {
        "casa": "Casa 2",
        "año": 2012,
        "metros": 60,
        "habitaciones": 2,
        "garaje": True,
        "zona": "B",
    },
    {
        "casa": "Casa 3",
        "año": 1980,
        "metros": 120,
        "habitaciones": 4,
        "garaje": False,
        "zona": "A",
    },
    {
        "casa": "Casa 4",
        "año": 2005,
        "metros": 75,
        "habitaciones": 3,
        "garaje": True,
        "zona": "B",
    },
    {
        "casa": "Casa 5",
        "año": 2015,
        "metros": 90,
        "habitaciones": 2,
        "garaje": False,
        "zona": "A",
    },
]


def antiguedad_inmueble(years):
    if years <= 10:
        return 50000000
    elif years > 10 and years <= 20:
        return 40000000
    elif years > 20 and years <= 30:
        return 30000000
    else:
        return 20000000


user_budget = float(input("ingrese el valor de su presupuesto: "))

actual_year = 2023

## Calcular el precio del inmueble y antiguedad
for propiedad in inmuebles:
    if propiedad.get("zona") == "A":
        propiedad["antiguedad"] = actual_year - propiedad.get("año")
        precio_A = propiedad.get("metros") * 100000
        +propiedad.get("habitaciones") * 500000
        +int(propiedad.get("garaje")) * 1500000
        +antiguedad_inmueble(propiedad.get("antiguedad"))
        propiedad["precio"] = precio_A
        print(precio_A)
    else:
        propiedad["antiguedad"] = actual_year - propiedad.get("año")
        precio_B = propiedad.get("metros") * 200000
        +propiedad.get("habitaciones") * 600000
        +int(propiedad.get("garaje")) * 2500000
        +antiguedad_inmueble(propiedad.get("antiguedad"))
        propiedad["precio"] = precio_B
print(inmuebles)

## Hacer la busqueda

for propiedad in inmuebles:
    if propiedad.get("precio") <= user_budget:
        print(
            """
         Puede comprar la %s que tiene %s metros, 
         %s habitaciones, %s cuenta con garaje, 
         tiene %s años de antiguedad y un valor de $ %s pesos.
         """
            % (
                propiedad.get("casa"),
                propiedad.get("metros"),
                propiedad.get("habitaciones"),
                "Si" if propiedad.get("garaje") else "No",
                propiedad.get("antiguedad"),
                propiedad.get("precio"),
            )
        )
    else:
        print("Lastimosamente, con ese presupuesto no puede comprar ninguna vivienda")
