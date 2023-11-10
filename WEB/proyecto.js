const API_URL = "http://127.0.0.1:5000/cursos"
const main = document.getElementById('main');
const add_curso = document.getElementById('enviar');
const delete_curso = document.getElementById('eliminar');
const edit_curso = document.getElementById('editar');
var prueba = {"cursos":[{"Codigo":1,"Edad":"15","Nombre":"Juan","Telefono":"12345678"},{"Codigo":2,"Edad":"24","Nombre":"Pepe","Telefono":"12345678"}], "mensaje": "cursos listados"};

const options = {
    method: 'GET',
    headers: {
      accept: 'application/json'
    }
  };

const options_delete = {
    method: 'DELETE',
    headers: {
      accept: 'application/json'
    }
  };

function getCursos(url){
    fetch(url, options)
    .then(response => response.json())
    .then(response => showCursos(response));
}

function showCursos(data){
    main.innerHTML = ``;
    const {cursos} = data
    cursos.forEach(alumno => {
        const {Codigo, Edad, Nombre, Telefono} = alumno;
        const alumnoElement = document.createElement('div');
        alumnoElement.classList.add('alumno');
        alumnoElement.innerHTML = `
            <p id="Codigo">Codigo: ${Codigo}</p>
            <p id="Edad">Edad: ${Edad}</p>
            <p id="Nombre">Nombre: ${Nombre}</p>
            <p id="Telefono">Telefono: ${Telefono}</p>`;
        main.appendChild(alumnoElement);
        })
}

add_curso.addEventListener("submit",function(event){
    event.preventDefault();
    var codigo = document.getElementById('codigo').value;
    var edad = document.getElementById('edad').value;
    var nombre = document.getElementById('nombre').value;
    var telefono = document.getElementById('telefono').value;

    if ((codigo)&&(edad)&&(nombre)&&(telefono)){
        var json_res = {"Codigo":codigo,"Edad":edad,"Nombre":nombre,"Telefono":telefono};
        const options_add = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(json_res),
        };
        fetch(API_URL, options_add).then(response => response.json())
        .then(data => {
            console.log('Respuesta de la API:', data);
        });
    }
    getCursos(API_URL);
    });

edit_curso.addEventListener("submit",function(event){
    event.preventDefault();
    var codigo = document.getElementById('codigo').value;
    var edad = document.getElementById('edad').value;
    var nombre = document.getElementById('nombre').value;
    var telefono = document.getElementById('telefono').value;
    if ((codigo)&&(edad)&&(nombre)&&(telefono)){
        var json_res = {"Edad":edad,"Nombre":nombre,"Telefono":telefono};
        const options_edit = {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(json_res),
        };
        fetch(API_URL + "/" + codigo, options_edit).then(response => response.json())
        .then(data => {
            console.log('Respuesta de la API:', data);
        });
    }
    getCursos(API_URL);
})

delete_curso.addEventListener("submit",function(event){
    event.preventDefault();
    var codigo = document.getElementById('codigo').value;
    if (codigo){
        console.log(codigo);
        fetch(API_URL + "/" + codigo, options_delete);
    }
    getCursos(API_URL);
})

getCursos(API_URL);