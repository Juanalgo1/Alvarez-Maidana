### Información del Data Set

Uso de .describe() y .info():
Utilizando pandas podemos ver rápidamente información importante acerca del data set.
En cuestión, al utilizar .info() podemos ver que la columna "Status" y "S Rank" tienen 674 valores no nulos (non-null). Es decir, faltan valores en esas columna, ya que en total tenemos 721 filas. 

Claramente no podemos eliminar la rareza de nuestro dataset porque es un dato fundamental, podríamos optar por rellenar con valores medios o de última reducir nuestra muestra eliminando las filas que no tienen rareza. Además, si "Status" es un indicador de rareza igual que S Rank pero en texto, directamente podríamos eliminarlo.

Con el resto de columnas no tenemos ningún problema, únicamente el tema de que algunos son de tipo float y demás (eso es lo que me rompió las bolas para poner la línea de pandas).

### Avg Mass
Dato: En las rarezas 1, 2 y 7 prácticamente no hay variación en el Peso Promedio del animal (tiene que ver con la cantidad de muestras de esas rarezas).