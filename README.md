# Particle Swarm Optimization - La Inteligencia Oculta en el Vuelo de las Aves

En la naturaleza hay un orden que nace del aparente caos. Lo que parece azar sigue reglas simples que, al combinarse, crean sistemas organizados sin que nadie los dirija. Este tipo de comportamiento ha inspirado modelos matemáticos que intentan imitar y entender cómo surge esa armonía.

Miles de aves se desplazan como un solo cuerpo, evitando colisiones y generando patrones ondulantes. Cada una ajusta su movimiento según la posición y velocidad de sus vecinas, obedeciendo solo a leyes locales.

Los cardúmenes muestran un comportamiento similar: cada pez responde a fuerzas básicas de atracción, repulsión y alineamiento, formando estructuras fluidas que se adaptan al entorno. Esa coordinación colectiva es un ejemplo claro de inteligencia emergente.

Las semillas del girasol crecen en espiral siguiendo la proporción áurea (). Cada nueva semilla se coloca a un ángulo constante del anterior (aproximadamente ), de modo que llenan el espacio sin superponerse.

Pero ¿por qué todos estos comportamientos están ordenados? ¿Cuál es la razón de ser así? Rara vez nos detenemos a pensar en la utilidad de estos patrones porque convivimos con ellos cotidianamente. Sin embargo, si observamos con atención, encontramos una belleza en la naturaleza similar a la que inspiró a James Kennedy, un psicólogo social que estudió los movimientos de las aves en bandada. Descubrió que su comportamiento social seguía patrones que les permitían, colectivamente, encontrar alimento y sobrevivir. Este principio también se manifiesta en otros seres vivos, incluso en los humanos cuando trabajamos en grupo.

James Kennedy, junto con Russell Eberhart, comprendieron que este comportamiento colectivo permitía a las aves optimizar sus metas en cualquier espacio. Así, modelaron un algoritmo de optimización llamado Particle Swarm Optimization (PSO), en el cual las partículas del enjambre buscan optimizar una función. Este algoritmo fue un éxito: imitando el comportamiento social y cognitivo de las aves, podía aplicarse a problemas matemáticos de optimización, incluso superando métodos diferenciales en ciertos casos, y explorando eficientemente espacios de alta dimensión.

### Descripción del algoritmo PSO

La meta es simple: dada una función objetivo, queremos **minimizar o maximizar su valor**.

En otras palabras, buscamos los valores del dominio \((x, y)\) que producen el menor o mayor resultado. En esta explicación usaremos la formulación de **minimización**:

\[
\hat{p} = \operatorname*{argmin} f(x, y)
\]

Definimos las siguientes variables:

- **\(S\)**: el espacio de búsqueda, el campo donde las partículas pueden explorar.  
- **\(N\)**: el número de partículas.  
- **\(x\)**: las posiciones actuales de las partículas.  
- **\(v\)**: las velocidades de las partículas, generadas de forma aleatoria al inicio.  
- **\(p\)**: las mejores posiciones encontradas por cada partícula (inicialmente \(p = x\)).  
- **\(\hat{p}\)**: el mejor valor global encontrado entre todas las partículas.  

Las posiciones \(x\) se representan en una matriz de \(\mathbb{R}^{D \times N}\), donde \(D\) es el número de dimensiones y \(N\) el número de partículas. De forma análoga, las velocidades \(v\) tienen la misma forma y se inicializan con valores aleatorios:

\[
x = \text{random}(-S, S), \quad 
v = \text{random}(-1, 1), \quad 
p = x, \quad 
\hat{p} = \operatorname*{argmin} f(p)
\]

Estas condiciones iniciales permiten que las partículas cubran todo el espacio de búsqueda, fomentando la exploración desde el principio.

Luego repetimos hasta actualizar \(\hat{p}\) (o hasta cumplir el criterio de parada):

\[
\begin{aligned}
v & = v + (p - x) + (\hat{p} - x) \\
x & = x + v \\
p & = \text{mejor\_entre}(p,\; x) \\
\hat{p} & = \text{mejor\_global}(p)
\end{aligned}
\]

La actualización de velocidad es el corazón del algoritmo:

\[
v = v + (p - x) + (\hat{p} - x)
\]

Queremos **actualizar las velocidades antes de mover las partículas**, porque así cada una “decide” hacia dónde moverse en función de la información actual. Esto sucede antes del cambio de posición, ya que al iniciar el algoritmo cada partícula **ya tiene una posición inicial** y conoce tanto su mejor posición personal \(p\) como el mejor valor global \(\hat{p}\).  
Con esos datos, cada partícula puede ajustar su dirección de movimiento.

El término \((p - x)\) se conoce como el **componente cognitivo**.  
Representa la *experiencia propia* de la partícula, su memoria. Cada partícula recuerda dónde ha encontrado un valor mejor y, naturalmente, tiende a volver hacia allí. En cierto modo, es su “intuición individual”: la fuerza que la impulsa a explorar de nuevo zonas donde le ha ido bien.

Por otro lado, \((\hat{p} - x)\) corresponde al **componente social**.  
Aquí entra en juego la *influencia colectiva*. Cada partícula observa el mejor resultado encontrado por todo el grupo y se ve atraída hacia esa dirección. Este término modela la cooperación: cada partícula aprende no solo de sí misma, sino del éxito de las demás.

La suma de estos dos componentes hace que el enjambre se comporte de manera equilibrada: el componente cognitivo fomenta la **exploración local**, mientras que el social impulsa la **explotación global**.  

El resultado es un sistema dinámico donde cada partícula alterna entre seguir su propio criterio y alinearse con el grupo, un balance clave para que el algoritmo encuentre el mínimo global sin quedar atrapado en soluciones parciales.

...

El artículo completo se encuentra [aquí](https://blog.bernardoolisan.com/posts/pso).