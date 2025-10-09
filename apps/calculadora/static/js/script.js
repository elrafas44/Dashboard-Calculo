const BASE_API_URL = '/'; 

async function realizarOperacion(operacion) {
    // Obtenemos los valores como strings desde los inputs
    let numA = document.getElementById('numA').value;
    let numB = document.getElementById('numB').value;
    const resultadoArea = document.getElementById('resultadoArea');
    
    // Mapeo de tu botón ('sumar') a la ruta de Antonio ('suma')
    const ENDPOINT_MAP = {
        'sumar': 'suma',
        'restar': 'resta',
        'multiplicar': 'multiplicacion',
        'dividir': 'division',
        'raiz': 'raiz',
        'factorial': 'factorial',
        'potencia': 'potencia'
    };
    
    const endpoint = ENDPOINT_MAP[operacion];

    try {
        let url;
        
        // --- Lógica para Rutas Binarias (Suma, Resta, Mult, Div) ---
        // Antonio usa <str:num1>/<str:num2>
        if (['sumar', 'restar', 'multiplicar', 'dividir'].includes(operacion)) {
            // CRUCIAL: Verificamos que ambos campos NO estén vacíos
            if (!numA || !numB) {
                resultadoArea.textContent = 'ERROR: Se necesitan ambos números para esta operación.';
                return;
            }
            // Enviamos los strings tal cual (la vista de Antonio los convertirá a float)
            url = `${BASE_API_URL}${endpoint}/${numA}/${numB}/`;
        } 
        
        // --- Lógica para Rutas Unarias/Int (Raíz, Factorial) ---
        // Antonio usa <int:numero>
        else if (operacion === 'factorial' || operacion === 'raiz') {
            if (!numA) {
                resultadoArea.textContent = 'ERROR: Ingresa el Número A.';
                return;
            }
            // Forzamos a entero, ya que la ruta <int:...> de Antonio fallaría con un decimal.
            let n = parseInt(numA);
            if (isNaN(n) || n === null) {
                 resultadoArea.textContent = 'ERROR: Entrada inválida. Debe ser un número entero.';
                 return;
            }
            url = `${BASE_API_URL}${endpoint}/${n}/`;
        }
        
        // --- Lógica para Potencia (Antonio usa <int:base>/<int:exponente>) ---
        else if (operacion === 'potencia') {
            if (!numA || !numB) {
                resultadoArea.textContent = 'ERROR: Se necesitan dos números enteros para la potencia.';
                return;
            }
            let n = parseInt(numA);
            let e = parseInt(numB);
            
            if (isNaN(n) || isNaN(e)) {
                resultadoArea.textContent = 'ERROR: Se necesitan dos números enteros para la potencia.';
                return;
            }
            url = `${BASE_API_URL}${endpoint}/${n}/${e}/`;
        }
        
        // --- Ejecución de la Petición (Método GET) ---
        const respuesta = await fetch(url);

        if (!respuesta.ok) {
            throw new Error(`Error ${respuesta.status}. No se pudo conectar o el ruteo falló.`);
        }

        // --- Procesamiento de la Respuesta JSON de Antonio ---
        const datos = await respuesta.json();
        
        if (datos.resultado !== undefined) {
            resultadoArea.textContent = datos.resultado;
        } else if (datos.error) {
             // Error devuelto por la vista de Antonio (ej: división por cero, o valor no numérico)
             resultadoArea.textContent = `ERROR: ${datos.error}`;
        } else {
             resultadoArea.textContent = 'ERROR: Respuesta del servidor inválida.';
        }

    } catch (error) {
        console.error("Fallo la conexión o la URL:", error);
        resultadoArea.textContent = `ERROR de conexión/API: ${error.message}`;
    }
}