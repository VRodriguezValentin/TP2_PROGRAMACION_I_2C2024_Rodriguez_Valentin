# 🛒 Sistema de Gestión de Productos Importados

Este proyecto tiene como objetivo el desarrollo de un sistema completo para la **gestión de productos importados**, incluyendo funcionalidades como el manejo de productos, inventario, depósitos, importaciones, ventas, generación de tickets y logs.

---

## 📦 Funcionalidades Principales

- Gestión de productos a importar
- Control de inventario en tiempo real
- Manejo de depósitos de almacenamiento
- Operaciones de importación y venta
- Generación de tickets de venta en ARS
- Sistema de logs para auditoría de acciones

---

## 🧱 PARTE 1 – Gestión de Productos

### 📘 Clase `Producto`

Atributos:
- `CODIGO`: Formato `NNNN-XX` (validar con regex)
- `DETALLE`: Nombre del producto (1 a 25 caracteres)
- `USD_COMPRA`: Precio de importación
- `USD_VENTA`: Precio de comercialización
- `PESO`: En gramos

### 📊 Inventario

- `inventario_codigos`: Lista de códigos
- `inventario_cantidades`: Lista de cantidades (paralela)

---

### 🛠 Funciones

#### 1️⃣ `producto_alta(path: str, inv1: list, inv2: list) -> bool`
- Agrega un nuevo producto si el código no existe
- Inicializa su inventario en 0
- 📛 Error: `[ERROR] Ítem existente.`

#### 2️⃣ `producto_baja(path: str, inv1: list, inv2: list) -> bool`
- Baja del producto solo si su inventario es cero
- 📛 Error: `[ERROR] Ítem con stock.`

#### 3️⃣ `producto_modificar_compra(...) / producto_modificar_venta(...)`
- Permiten modificar los precios de compra o venta
- Valida precios positivos

#### 4️⃣ `producto_listar(path: str, inv1: list, inv2: list)`
- Lista los productos activos con la info clave:
```
[CODIGO] [DETALLE] [PRECIO COMPRA] [PRECIO VENTA] [CANTIDAD EN INVENTARIO]
```

---

## 🧱 PARTE 2 – Gestión de Depósitos e Importación/Venta

### 🏢 Clase `Deposito`

Atributos:
- `ID`: Autoincremental
- `CAPACIDAD`: Total máxima de unidades
- `STOCK`: Lista de diccionarios `{ "ítem": codigo, "cantidad": x }`

🔁 Redefine `__len__()` para retornar **capacidad disponible**

---

### 🧑‍💼 Clase `Gestion`

#### ✅ `importar(...)`
- Elige producto y cantidad a importar
- Actualiza inventario y asigna a depósitos
- Si un depósito no tiene espacio, distribuye el excedente a uno nuevo
- Guarda en `DEPOSITOS.json`

#### 🛍️ `vender(...)`
- Valida CUIT (`NN-NNNNNNNN-N`)
- Actualiza inventario y depósitos
- Elimina depósitos vacíos
- Llama a `generar_ticket(...)`

#### 🧾 `generar_ticket(cotizacion: float, ...)`
- Imprime ticket en consola y lo guarda en `ventas.txt`
- Contenido del ticket:
```
[VENTA dd/mm/yyyy hh:mm]
CUIT COMPRADOR:
DETALLE PRODUCTO:
CANTIDAD VENDIDA:
IMPORTE USD:
IMPORTE ARS:
COTIZACIÓN DEL DÍA:
```

#### 🧠 `log(mensaje: str)`
- Guarda acciones o errores en formato:
```
dd/mm/yyyy hh:mm : mensaje
```

---

## 📋 Funciones Adicionales

### 6️⃣ Importar Producto  
Usa: `Gestion.importar(...)`

### 7️⃣ Vender Producto  
Usa: `Gestion.vender(...)`

### 8️⃣ Listar Depósitos  
`deposito_listar(...)`  
Ejemplo:
```
ID 1000 - 150/1000 - Disponible 850
ID 1001 - 250/900 - Disponible 650
```

### 9️⃣ Producto con Menos Stock
Ejemplo:
```
[PRODUCTO 5547-AF]
TOTAL STOCK: 150
Depósito 1: 75
Depósito 3: 25
Depósito 5: 50
```

### 🔟 Filtrar Productos por Precio Medio
- Lista productos con precio de **compra menor** al promedio de precios de **venta**

### 1️⃣1️⃣ Ordenar Depósitos por Peso Total
- Ordena depósitos según el peso total contenido

---

## 📂 Archivos Utilizados

- `DB_PRODUCTOS.csv`: Base de productos
- `DEPOSITOS.json`: Estado de depósitos
- `ventas.txt`: Histórico de ventas

---

## 🧪 Requisitos Técnicos

- Python 3.10+
- Manejo de archivos CSV / JSON / TXT
- Expresiones regulares para validaciones

Este sistema es modular y puede ser ampliado fácilmente. Ideal para implementar interfaces gráficas o adaptarlo a una base de datos real en el futuro.

---
