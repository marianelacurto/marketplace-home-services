# Documento de Requisitos de Producto — MVP

## Marketplace de Servicios para el Hogar

## 1. Objetivo del producto

Crear una plataforma digital que conecte personas que necesitan servicios para el hogar con profesionales cercanos, como electricistas, pintores, fontaneros, carpinteros y otros especialistas.

El MVP debe permitir que los clientes encuentren profesionales por categoría y cercanía, consulten sus perfiles, revisen su reputación y contacten con ellos dentro de la plataforma.

Al mismo tiempo, debe permitir que los profesionales creen una presencia digital, muestren su experiencia y trabajos realizados, y reciban nuevas oportunidades de clientes de su zona.

---

## 2. Usuarios

### Cliente

Persona que necesita contratar un servicio para su hogar y busca una forma más sencilla y confiable de encontrar profesionales cercanos.

### Profesional

Persona que ofrece servicios para el hogar y quiere aumentar su visibilidad, mostrar su experiencia, construir reputación y ampliar su red de clientes.

---

## 3. Problemas que resuelve

### Problema del cliente

Encontrar un profesional de confianza suele depender del boca a boca, recomendaciones de vecinos o conocidos y búsquedas dispersas.

Esto hace que sea difícil:

- encontrar rápidamente al profesional adecuado;
- saber si trabaja en la zona;
- conocer su experiencia;
- comparar alternativas;
- saber si otros clientes han quedado satisfechos;
- decidir en quién confiar.

### Problema del profesional

Muchos profesionales dependen principalmente de recomendaciones informales para conseguir nuevos clientes.

Esto limita su capacidad para:

- llegar a nuevos clientes;
- mostrar sus trabajos;
- construir una reputación visible;
- diferenciarse de otros profesionales;
- generar confianza antes del primer contacto.

---

## 4. Propuesta de valor

Una plataforma que reúne profesionales de servicios para el hogar según su especialidad y ubicación, permitiendo a los clientes encontrar opciones cercanas y confiables, y a los profesionales mostrar su trabajo, construir reputación y ampliar su red de clientes.

---

## 5. Hipótesis principal del MVP

Si ofrecemos un lugar donde las personas puedan encontrar profesionales cercanos, comparar su reputación y contactar con ellos fácilmente, los clientes tendrán mayor confianza al contratar y los profesionales podrán ampliar su red de clientes.

---

## 6. Alcance del MVP

El MVP debe validar principalmente si:

- los clientes utilizan la plataforma para encontrar profesionales cercanos;
- la reputación y las reseñas influyen en la decisión;
- los profesionales están dispuestos a crear y mantener un perfil;
- los clientes prefieren iniciar el contacto dentro de la plataforma;
- existe interés suficiente en ambas partes para sostener un marketplace de dos lados.

---

## 7. Flujo mínimo del cliente

1. Registrarse o iniciar sesión.
2. Buscar un servicio por categoría.
3. Ver profesionales cercanos.
4. Consultar el perfil de un profesional.
5. Revisar descripción, trabajos realizados y reseñas.
6. Enviar una solicitud o iniciar una conversación.
7. Contratar el servicio.
8. Marcar el servicio como finalizado.
9. Dejar una reseña.

---

## 8. Flujo mínimo del profesional

1. Registrarse o iniciar sesión.
2. Crear su perfil profesional.
3. Indicar su especialidad.
4. Indicar ubicación o zona de trabajo.
5. Añadir una descripción de sus servicios.
6. Añadir fotografías de trabajos realizados.
7. Aparecer en búsquedas de clientes cercanos.
8. Recibir solicitudes.
9. Aceptar un trabajo.
10. Marcarlo como finalizado.
11. Recibir una reseña del cliente.

---

## 9. Funcionalidades principales del MVP

### Autenticación y usuarios

- Registro de clientes.
- Registro de profesionales.
- Inicio de sesión.
- Roles diferenciados de cliente y profesional.

### Perfil profesional

- Nombre.
- Especialidad o categoría.
- Descripción.
- Ubicación o zona de trabajo.
- Fotografías de trabajos realizados.
- Valoración media.
- Reseñas recibidas.

### Búsqueda y descubrimiento

- Búsqueda por categoría.
- Visualización de profesionales cercanos.
- Uso de geolocalización o ubicación configurada.
- Orden o filtrado por cercanía.

### Contacto

- Solicitud de servicio.
- Chat interno básico o mensajería dentro de la plataforma.

### Gestión de solicitudes

Estados mínimos:

- pendiente;
- aceptada;
- finalizada.

### Reputación

- Valoración del profesional.
- Reseña después de finalizar un servicio.
- Visualización de reseñas en el perfil.

---

## 10. Historias de usuario

### Cliente

- Como cliente, quiero registrarme para poder utilizar la plataforma.
- Como cliente, quiero buscar profesionales por categoría para encontrar el servicio que necesito.
- Como cliente, quiero ver profesionales cercanos para priorizar opciones de mi zona.
- Como cliente, quiero consultar un perfil profesional para conocer su experiencia antes de contactar.
- Como cliente, quiero ver trabajos realizados para evaluar la calidad del profesional.
- Como cliente, quiero leer reseñas de otros clientes para aumentar mi confianza.
- Como cliente, quiero enviar una solicitud de servicio sin salir de la plataforma.
- Como cliente, quiero saber si mi solicitud fue aceptada.
- Como cliente, quiero dejar una reseña después de finalizar el servicio.

### Profesional

- Como profesional, quiero registrarme para ofrecer mis servicios.
- Como profesional, quiero crear un perfil para mostrar mi experiencia.
- Como profesional, quiero indicar mi categoría para aparecer en búsquedas relevantes.
- Como profesional, quiero indicar mi zona de trabajo para recibir solicitudes cercanas.
- Como profesional, quiero mostrar fotografías de mis trabajos para generar confianza.
- Como profesional, quiero recibir solicitudes de clientes.
- Como profesional, quiero aceptar o rechazar una solicitud.
- Como profesional, quiero acumular reseñas para fortalecer mi reputación.

---

## 11. Requisitos funcionales

### RF-01 — Registro

El sistema debe permitir registrar clientes y profesionales.

### RF-02 — Inicio de sesión

El sistema debe permitir a usuarios registrados iniciar sesión de forma segura.

### RF-03 — Roles

El sistema debe distinguir entre cliente y profesional.

### RF-04 — Perfil profesional

El profesional debe poder crear y editar su perfil.

### RF-05 — Categoría

El profesional debe poder seleccionar una categoría o especialidad.

### RF-06 — Ubicación

El profesional debe poder indicar su ubicación o zona de trabajo.

### RF-07 — Portfolio

El profesional debe poder añadir fotografías de trabajos realizados.

### RF-08 — Búsqueda

El cliente debe poder buscar profesionales por categoría.

### RF-09 — Cercanía

El sistema debe mostrar profesionales según cercanía respecto del cliente.

### RF-10 — Perfil público

El cliente debe poder consultar el perfil público de un profesional.

### RF-11 — Solicitud de servicio

El cliente debe poder enviar una solicitud a un profesional.

### RF-12 — Mensajería

Cliente y profesional deben poder comunicarse dentro de la plataforma mediante un sistema básico de mensajes.

### RF-13 — Estado de solicitud

Una solicitud debe poder tener los estados pendiente, aceptada y finalizada.

### RF-14 — Reseñas

El cliente debe poder dejar una valoración y una reseña después de finalizar el servicio.

### RF-15 — Reputación

El perfil del profesional debe mostrar las valoraciones y reseñas recibidas.

---

## 12. Requisitos no funcionales

### Usabilidad

La interfaz debe ser sencilla y comprensible para usuarios con distintos niveles de experiencia digital.

### Responsive

La aplicación debe funcionar correctamente en escritorio, tablet y móvil.

### Rendimiento

Las búsquedas y consultas principales deben responder de forma rápida en condiciones normales de uso.

### Seguridad

Las contraseñas deben almacenarse de forma segura y las rutas privadas deben requerir autenticación.

### Privacidad

La plataforma debe proteger los datos personales y mostrar únicamente la información necesaria para el funcionamiento del servicio.

### Mantenibilidad

El código debe organizarse de forma modular para facilitar futuras funcionalidades.

### Escalabilidad

La arquitectura debe permitir añadir en el futuro pagos, suscripciones, agenda, vídeo y otras funcionalidades sin requerir una reescritura completa.

---

## 13. Criterios de aceptación del MVP

El MVP podrá considerarse funcional cuando:

- un cliente pueda registrarse e iniciar sesión;
- un profesional pueda registrarse e iniciar sesión;
- el profesional pueda crear su perfil;
- el profesional pueda seleccionar especialidad y zona;
- el cliente pueda buscar por categoría;
- el cliente pueda visualizar profesionales cercanos;
- el cliente pueda consultar el perfil de un profesional;
- el cliente pueda ver reseñas;
- el cliente pueda enviar una solicitud;
- el profesional pueda aceptar una solicitud;
- una solicitud pueda marcarse como finalizada;
- el cliente pueda dejar una reseña después de finalizar el servicio.

---

## 14. Fuera del alcance del MVP

Las siguientes funcionalidades quedan para versiones posteriores:

- pagos dentro de la plataforma;
- comisión por transacción;
- suscripciones premium;
- facturación automática;
- vídeo de presentación;
- agenda y disponibilidad avanzada;
- presupuestos múltiples;
- comparación de presupuestos;
- profesionales promocionados;
- sistema avanzado de disputas;
- analítica avanzada;
- programas de fidelización.

---

## 15. Modelo de negocio inicial

La plataforma podrá evolucionar hacia un modelo híbrido.

### Suscripción para profesionales

Los profesionales podrían pagar una cuota mensual a cambio de funcionalidades adicionales, mayor visibilidad u otros beneficios.

### Comisión por transacción

En una fase posterior, si los pagos se realizan dentro de la plataforma, se podría aplicar una comisión por operación.

### Enfoque inicial

Durante el MVP, la prioridad será validar el uso y la propuesta de valor antes de implementar mecanismos de monetización complejos.

---

## 16. Métricas para validar el MVP

### Adopción

- Número de clientes registrados.
- Número de profesionales registrados.
- Porcentaje de profesionales que completan su perfil.

### Actividad

- Número de búsquedas realizadas.
- Número de perfiles profesionales consultados.
- Número de solicitudes enviadas.
- Número de solicitudes aceptadas.

### Conversión

- Porcentaje de solicitudes que pasan de pendiente a aceptada.
- Porcentaje de solicitudes que llegan a finalizada.

### Reputación

- Número de reseñas generadas.
- Porcentaje de servicios finalizados que reciben reseña.

### Retención

- Usuarios que vuelven a utilizar la plataforma.
- Profesionales que continúan activos después de sus primeras solicitudes.

---

## 17. Preguntas que debe responder el MVP

- ¿Los clientes valoran realmente encontrar profesionales por cercanía?
- ¿Las reseñas influyen en la elección?
- ¿Los profesionales están dispuestos a crear y mantener un perfil?
- ¿Los clientes prefieren iniciar el contacto dentro de la plataforma?
- ¿Qué categorías generan mayor demanda?
- ¿Qué porcentaje de contactos termina en contratación?
- ¿Los profesionales estarían dispuestos a pagar por mayor visibilidad o por recibir clientes?

---

## 18. Evolución futura

Si el MVP valida la propuesta de valor, las siguientes etapas podrán incorporar:

1. contratación formal dentro de la plataforma;
2. pagos integrados;
3. comisiones;
4. suscripciones premium;
5. facturación;
6. agenda y disponibilidad;
7. vídeo de presentación;
8. presupuestos;
9. herramientas de analítica para profesionales;
10. mecanismos avanzados de confianza, soporte y resolución de disputas.

---

## Conclusión

El MVP se enfoca en validar el núcleo del marketplace: conectar clientes que necesitan servicios para el hogar con profesionales cercanos y confiables.

La prioridad no es construir todas las funcionalidades posibles, sino comprobar que ambas partes encuentran valor en la plataforma y que existe un flujo real desde la búsqueda hasta el contacto, la contratación y la reputación posterior.