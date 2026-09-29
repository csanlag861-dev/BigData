# Selection Sort

## 💡 Idea

**Selection Sort** es un algoritmo básico de ordenamiento que busca el elemento más pequeño de una lista y lo coloca al principio, repitiendo el proceso para el resto de los elementos.

## 🔄 ¿Cómo funciona?

1. Divide la lista en dos partes:

   * Una parte **ordenada** a la izquierda.
   * Una parte **no ordenada** a la derecha.
2. Busca el valor más pequeño en la parte no ordenada.
3. Intercambia ese valor con el primer elemento de la parte no ordenada.
4. Mueve el límite de la parte ordenada un espacio a la derecha.
5. Repite el proceso hasta que toda la lista esté ordenada.

## 📊 Complejidad

| Caso          | Complejidad |
| ------------- | ----------- |
| Mejor caso    | `O(n²)`     |
| Caso promedio | `O(n²)`     |
| Peor caso     | `O(n²)`     |

La complejidad temporal es siempre **O(n²)**, independientemente de cómo esté ordenada la lista de entrada.

Esto ocurre porque el algoritmo recorre **siempre toda la parte no ordenada** para encontrar el elemento mínimo. Por ello, no obtiene una ventaja significativa cuando la lista ya está parcialmente ordenada, a diferencia de algoritmos como **Insertion Sort**.

### 💾 Uso de memoria

Selection Sort tiene como ventaja que realiza un número reducido de intercambios.

* Espacio adicional: `O(1)`
* Número máximo de intercambios: `n - 1`
* Número de escrituras: `O(n)`

Esto puede ser interesante cuando las operaciones de escritura en memoria tienen un coste elevado.

## ⚠️ Selection Sort y Big Data

Selection Sort **no es adecuado para grandes volúmenes de datos**.

Su complejidad temporal de `O(n²)` provoca que el número de operaciones crezca cuadráticamente a medida que aumenta el tamaño de la entrada.

Por ejemplo, si el tamaño de la entrada se duplica:

```text
n → 2n

O(n²) → O((2n)²) = O(4n²)
```

Por tanto, aproximadamente se cuadruplica el trabajo.

## 🛠️ ¿Cuándo es útil Selection Sort?

Aunque no es eficiente para grandes cantidades de datos, puede ser útil en determinadas situaciones:

1. **Cuando el coste de escribir en memoria es elevado**, ya que realiza como máximo `n - 1` intercambios.
2. **En listas muy pequeñas**, donde la sencillez del algoritmo puede compensar el uso de algoritmos más sofisticados.
3. **Con fines educativos**, ya que su funcionamiento es sencillo de entender y permite estudiar conceptos básicos de algoritmos de ordenamiento.

## 🖼️ Demostración gráfica

<!-- Añadir aquí la imagen de la demostración -->

![Demostración de Selection Sort](./images/selection-sort.png)

## 🎥 Vídeos

* [Selection Sort Visualization - AI](https://www.youtube.com/watch?v=Iccmrk2ZWoc)
* [Ordenación por selección en 3 minutos](https://www.youtube.com/watch?v=g-PGLbMth_g)

## 🐍 Ejemplo de implementación en Python

```python
def ordenar(lista: list[int]) -> list[int]:
    n = len(lista)

    for i in range(n - 1):
        minimo = i

        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j

        if minimo != i:
            lista[i], lista[minimo] = lista[minimo], lista[i]

    return lista


if __name__ == "__main__":
    print(ordenar([3, 1, 4, 1, 5]))
    # [1, 1, 3, 4, 5]
```

## 📚 Bibliografía

* [Visualización de Selection Sort | Coddy](https://coddy.tech/visualize/sorting/selection-sort?lang=es&view=array&speed=2&size=14)
* [Selection Sort — Visualizador de algoritmos](https://www.alg0.dev/es/selection-sort)
* [▷ Selection sort en Python — explicado paso a paso (con animación) 2026](https://elpythonista.com/selection-sort-en-python)
* [Ordenamiento por selección — Wikipedia](https://es.wikipedia.org/wiki/Ordenamiento_por_selecci%C3%B3n)
