<h1>Prueba Técnica Lógica</h1>
<small>Tomada de <a href="https://www.youtube.com/watch?v=npfzSC8B3aM">Todo Code</a></small>

Caso real para puesto Trainee / Junior (Java) solucionado con Python básico para probar procesos lógicos. Se divide en dos partes

<div class="container" style="background: gray;">
<h3>Parte 1</h3>
<h5>Tiempo recomendado: 60 minutos</h5>
<article>
    Suponer un sistema de reserva de asientos para un anfiteatro. El teatro cuenta con 10 filas de 10 asientos cada una. Se necesita desarrollar un sistema (sin uso de bases de datos, únicamente con manejo de datos de forma lógica) que permita a cabo llevar lo siguiente
</article>
<ol>
<li>
Cargar el 'mapa' de las filas y asientos. Indicando con una 'X' los asientos ocupados y con una 'L' los asientos libres. Al iniciar el programa todos los asientos deberán estar libres.
</li>
<li>
Manejar la reserva de asientos contemplando que un asiento SOLO PUEDE SER RESERVADO si se encuentra en estado 'L', en caso de que esté en estado 'X', se deberá permitir al comprador elegir otro asiento. Si se encuentra en estado 'L', deberá pasar automáticamente al estado 'X'.
</li>
<li>Para finalizar el programa se deberá ingresar un valor en particular. Contemplar que no existe la cantidad exacta de veces que el programa se puede ejecutar.</li>
<li>Contemplar que SOLO EXISTEN 10 FILAS y 10 ASIENTOS. No se pueden vender asientos fuera de estas numeraciones. No se permite 'sobreventa'</li>
</ol>
<ul>
<li>CONSIDERACIONES: No es necesaria la implementación de Interfaz Gráfica de Usuario (IGU) ni de Bases de Datos. Se evaluará 100% el manejo lógico del desarrollo de la aplicación.</li>
<li>EXTRA: En caso de que un cliente solicite visualizar cuáles son los asientos libres, el sistema deberá permitir mostrar de forma gráfica simple el mapa de asientos. NO UTILIZAR IGU para este caso. Utilizar ÚNICAMENTE lógica y la salida por consola.</li>
</ul>
</div>

<div class="container" style="background: gray;">
<h3>Parte 2</h3>
<h5>Tiempo recomendado: 60 minutos </h5>
<article>
Basándose en el mismo escenario del sistema de reservas de asientos para un anfiteatro, llegó el momento de planear el sistema de 'tickets' que obtendrá cada persona al reservar su asiento. Para ello tener en cuenta lo siguiente
</article>
<ol>
<li>Crea la 'plantilla' necesaria para guardar los siguientes datos por ticket: Número de ticket, fila, asiento, fecha de compra, fecha de validez (evento), precio.</li>
<li>Usar una 'base de datos lógica' (no archivos, no sql, etc.) mediante alguna estructura de datos que permita almacenar un número indeterminado de tickets. Generar una serie de tickets en dicha estructura.</li>
<li>Generar un método que recorra la estructura de datos y SUME los precios de todos los tickets. Mostrar en pantalla el total. No es necesario usar IGU, mostrar en consola.</li>
<li>Solicitar al usuario del programa que ingrese un número de fila. A partir de esto, mostrar en pantalla los datos de los tickets pertenecientes a esta fila. No es necesario usar IGU, mostrar en consola.</li>
</ol>
<ul>
<li>CONSIDERACIONES: No es necesaria la implementación de Interfaz Gráfica de Usuario (IGU) ni de Bases de Datos. Se evaluará 100% el manejo lógico del desarrollo de la aplicación.</li>
<li>EXTRA: En caso de que se desee agregar una 'plantilla' para clientes con los datos: id, número de tarjeta de identificación, nombre, apellido. ¿Cómo se implementaría? ¿De que manera se relacionaría con el ticket para que este integre los datos del cliente que tiene asignado? Realizar implementación</li>
</ul>
</div>
<div>
Esta prueba se puede realizar con la mayoría de lenguajes de programación. Se sugiere optimizar y usar la menor cantidad de código posible para solucionarlo.
</div>