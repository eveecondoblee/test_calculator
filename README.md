# Calculadora en Python

Este proyecto es una simple calculadora en **Python** que permite realizar operaciones matemáticas básicas como suma, resta, multiplicación, división, raíz cuadrada y exponencial.
De igual manera cuenta con un conjunto de pruebas unitarias para verificar el correcto funcionamiento de las operaciones, dichas pruebas se realizaron con **pytest**.

## Requisitos

- Python 3.6 o superior.
- pytest (para las pruebas unitarias).

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/eveecondoblee/test_calculator.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd test_calculator
   ```

3. Instala las dependencias (si es necesario):

   ```bash
    pip install pytest
    ```

4. Ejecuta las pruebas unitarias:

   ```bash
   pytest test_calculator.py -v
   ```

## Archivos del Proyecto

- **[calculator.py](calculator.py)**: Contiene las funciones principales de la calculadora.
- **[test_calculator.py](test_calculator.py)**: Contiene las pruebas unitarias para las funciones de la calculadora.
- **[README.md](README.md)**: Este archivo, que contiene la documentación del proyecto.

## Funciones implentadas en `calculator.py`

1. **`add(a, b)`**
   Suma dos números.

   **Ejemplo**

    ```python
    add(2, 3) # Devuelve 5
    ```

2. **`subtract(a, b)`**
   Resta el segundo número al primero.

   ****Ejemplo**

    ```python
    subtract(5, 3) # Devuelve 2
    ```

3. **`multiply(a, b)`**
   Multiplica dos números.

   **Ejemplo**

    ```python
    multiply(2, 3) # Devuelve 6
    ```

4. **`divide(a, b)`**
  Divide el primer número por el segundo. Lanza un `ValueError` si el divisor es cero.

    **Ejemplo**

    ```python
      divide(6, 3) # Devuelve 2.0
      divide(6, 0) # Lanza ValueError: "No se puede dividir por cero."
    ```

5. **`square(n, i=100)`**
   Calcula la raíz cuadrada de un número utilizando el método de aproximación de Newton. Lanza un `ValueError` si el número es negativo.
  
    **Ejemplo**
  
    ```python
        square(4) # Devuelve 2.0
        square(-4) # Lanza ValueError: "No se puede calcular la raíz cuadrada de un número negativo."
    ```

6. **`exponential(x, i=100)`**
   Calcula el valor de e^x utilizando una serie de Taylor.

    **Ejemplo**

      ```python
          exponential(1) # Devuelve 2.7182818284590455
      ```

## Pruebas Unitarias

El archivo `test_calculator.py` utiliza `pytest` para realizar pruebas unitarias de las funciones implementadas en `calculator.py`. A continuación, se describen las pruebas realizadas:

1. `test_add`
Verifica que la función add sume correctamente dos números.

2. `test_subtract`
Verifica que la función subtract reste correctamente dos números.

3. `test_multiply`
Verifica que la función multiply multiplique correctamente dos números.

4. `test_divide`
Verifica que la función divide divida correctamente dos números.

5. `test_divide_by_zero`
Verifica que la función divide lance un ValueError al intentar dividir por cero.

6. `test_square`
Verifica que la función square calcule correctamente la raíz cuadrada de un número.

7. `test_exponential`
Verifica que la función exponential calcule correctamente el valor de e^x.