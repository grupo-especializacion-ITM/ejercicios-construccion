## Principio de apertura y cierre

Este principio establece que una clase debe estar abierta a la extension y cerrada a su modificacion. Cuando se habla de extension se hace referencia a que una clase debe permitir que se le añadan nuevas funcionalidades sin necesidad de modificar su codigo fuente, y cuando se habla de cerrada se hace referencia a que una vez que una clase ha sido implementada, no debe ser modificada con el fin de evitar errores en codigos que hagan uso de esta clase.

En palabras mas coloquiales, tomar una clase base sin modificarla y extenderla para añadir nuevas funcionalidades.

## solucion

Como se puede ver, el metodo "calcularArea" no es muy eficiente en terminos de codigo, ya que estamo obligados a unicamente consultar figuras de tipo circulo o rectangulo, si quisieramos añadir una nueva figura, deberiamos modificar el codigo de la clase, lo cual va en contra del principio de apertura y cierre.

para solucionar esto, creamos una clase "figura" la cual tiene un metodo abstracto "calcularArea" que no lo implementa pero firma el contrato para que las que la utilicen lo hagan. en base a esto, se cren las clases triangulo, circulo y cualquier otra figura, y se hereda de la clase "figura". Cada una de estas va a implementar el metodo "calcularArea" de acuerdo a la formula de cada figura.