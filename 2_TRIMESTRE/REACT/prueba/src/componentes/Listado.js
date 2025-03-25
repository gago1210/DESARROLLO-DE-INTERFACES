import React from 'react';

//vamos a crear una funcion porque esto es un componente(es la funcion) en el que necesitamos exportarlos al final del todo (export default)
//la funcion listado la genero y ya deja de dar error. 
//esta funcion tiene siempre un return, siempre es la misma estructura: nombre, exportacion y nombre de los elementos que entran
//este listado tiene una inyecccion de 'elementos' de la lista
//dentro del elemento html (ul) estoy metiendo el grupo de elementos que van entrando y los saco de uno en uno
function Listado ({elementos}){
    return (
        <ul>
            <hr></hr>
            {elementos.map(elemento => (
                <p style= {{background:'grey', color: 'black'}}  key={elemento.id}>{elemento.id}.-{elemento.titulo}</p>
            ))}

            <hr></hr>

            
        </ul>
    );
}
    




export default Listado;